import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
dataset = pd.read_csv('/content/AirQuality.csv', sep=';', engine='python')
dataset = dataset.loc[:, ~dataset.columns.str.contains('^Unnamed')]

# Convert comma to dot safely
dataset = dataset.applymap(lambda x: str(x).replace(',', '.') if isinstance(x, str) else x)

# Convert to numeric
numeric_cols = dataset.columns.drop(['Date', 'Time'])
dataset[numeric_cols] = dataset[numeric_cols].apply(pd.to_numeric, errors='coerce')

dataset = dataset.dropna()

print(dataset.head())
print(dataset.shape)

# Create the AQHI
def ehr(beta, C):
    return np.exp(beta * C) - 1

dataset["AQHI"] = (
    ehr(0.000446, dataset["NO2(GT)"]) +
    ehr(0.000995, dataset["PT08.S5(O3)"]) +
    ehr(0.000871, dataset["C6H6(GT)"]) +
    ehr(0.000431, dataset["PT08.S2(NMHC)"]) +
    ehr(0.000488, dataset["PT08.S3(NOx)"])
)


aqhi_values = dataset["AQHI"].values.reshape(-1, 1)


from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range=(0, 1))
aqhi_scaled = sc.fit_transform(aqhi_values)


def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(seq_length, len(data)):
        X.append(data[i-seq_length:i, 0])
        y.append(data[i, 0])
    return np.array(X), np.array(y)

SEQ_LENGTH = 60
X, y = create_sequences(aqhi_scaled, SEQ_LENGTH)

# Reshape for LSTM input [samples, time steps, features]
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

print(f"X shape: {X.shape}")
print(f"y shape: {y.shape}")

# Split into train and test sets (use last 20% for testing)
split_idx = int(len(X) * 0.8)
X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

print(f"Training samples: {X_train.shape[0]}")
print(f"Testing samples: {X_test.shape[0]}")

# Build LSTM model (similar to stock prediction model)
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout

model = Sequential()

model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
model.add(Dropout(0.2))

model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(units=50))
model.add(Dropout(0.2))

model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.summary()

# Train the model
history = model.fit(
    X_train, y_train,
    epochs=100,
    batch_size=32,
    validation_data=(X_test, y_test),
    verbose=1
)

# Save model
model.save('models/aqhi_prediction_model.h5')

# Make predictions
predicted_aqhi_scaled = model.predict(X_test)
predicted_aqhi = sc.inverse_transform(predicted_aqhi_scaled)

# Get actual values (inverse transform)
actual_aqhi_scaled = y_test.reshape(-1, 1)
actual_aqhi = sc.inverse_transform(actual_aqhi_scaled)

# Calculate RMSE
from sklearn.metrics import mean_squared_error, mean_absolute_error
rmse = np.sqrt(mean_squared_error(actual_aqhi, predicted_aqhi))
mae = mean_absolute_error(actual_aqhi, predicted_aqhi)

print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")

# Plot training history
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(actual_aqhi, color='green', label='Actual AQHI', alpha=0.7)
plt.plot(predicted_aqhi, color='red', label='Predicted AQHI', alpha=0.7)
plt.title('AQHI Prediction')
plt.xlabel('Time')
plt.ylabel('AQHI Value')
plt.legend()

plt.tight_layout()
plt.show()

# Plot actual vs predicted
plt.figure(figsize=(10, 6))
plt.plot(actual_aqhi, color='green', label='Actual AQHI', linewidth=2)
plt.plot(predicted_aqhi, color='red', label='Predicted AQHI', linewidth=1.5, linestyle='--')
plt.title('AQHI Time Series Prediction')
plt.xlabel('Time Steps')
plt.ylabel('AQHI Value')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

def classify_aqhi(score):
    if score <= 3: return 1
    if score <= 6: return 2
    if score <= 7: return 3
    return 4

# Classify actual and predicted values
actual_classes = [classify_aqhi(val[0]) for val in actual_aqhi]
predicted_classes = [classify_aqhi(val[0]) for val in predicted_aqhi]

# Calculate classification accuracy
from sklearn.metrics import accuracy_score
classification_accuracy = accuracy_score(actual_classes, predicted_classes)
print(f"Classification Accuracy: {classification_accuracy:.4f}")

# Plot confusion matrix for classification
from sklearn.metrics import confusion_matrix
import seaborn as sns

cm = confusion_matrix(actual_classes, predicted_classes, labels=[1, 2, 3, 4])
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Low', 'Moderate', 'High', 'Very High'],
            yticklabels=['Low', 'Moderate', 'High', 'Very High'])
plt.title('AQHI Classification Confusion Matrix')
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()
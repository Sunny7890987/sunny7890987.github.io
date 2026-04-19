# SDD4007 E-Portfolio — Software Development Student

> **Course:** SDD4007 Enhancing Competencies in the 21st Century Workplace (AY2025/26)
> **Assignment:** CA (40%) — Preparation of E-portfolio
> **Platform:** GitHub Pages (free hosting)

---

## How to Use This Template

This is a complete, deployable E-portfolio template built for a Higher Diploma in Software Development student. Follow the steps below to customise it and publish it live on GitHub Pages — for free.

---

## Quick Start

### Step 1: Replace All Placeholders

Open `index.html` and replace every `[placeholder]` text with your real information:

| Find... | Replace with... |
|---|---|
| `[Your Full Name]` | Your actual full name |
| `[Your College/Institution Name]` | e.g., IVE, HKDI |
| `[Year Started]` | e.g., 2024 |
| `[your-github-username]` | Your GitHub username |
| `[your.email@example.com]` | Your email address |
| `[your-linkedin-username]` | Your LinkedIn username |
| `[Current Year]` | e.g., 2026 |
| `[YN]` | Your initials (shown in avatar) |

### Step 2: Add Your Profile Photo (Optional)

Replace the avatar placeholder in the hero section with your own photo:

```html
<!-- Find this in index.html -->
<div class="avatar-placeholder">
  <span>[YN]</span>
</div>

<!-- Replace with -->
<img src="assets/profile.jpg" alt="Your Name" class="avatar-photo" style="width:110px;height:110px;border-radius:50%;object-fit:cover;border:3px solid #58a6ff;box-shadow:0 0 0 6px rgba(88,166,255,0.15);">
```

Then save your photo as `assets/profile.jpg` in the same folder.

### Step 3: Fill In Your Projects

In the `#projects` section, replace the placeholder content with your actual project details. Update:
- Project name
- Description of what it does
- Your role
- Technologies used
- GitHub link (if you have one)
- Live demo link (if you have one)

### Step 4: Fill In Your Activities

In the `#activities` section, replace the placeholder activities with your real extracurricular experiences.

### Step 5: Fill In Your Career Goal (Part B)

Customise the career goal quote and roadmap in the `#career` section to reflect your real career aspirations and timeline.

---

## Deploying to GitHub Pages

### If You Haven't Pushed to GitHub Yet

1. **Create a GitHub repository**
   - Go to [github.com](https://github.com) → New Repository
   - Name it `e-portfolio` (or any name you like)
   - Set it to **Public**
   - Do NOT initialise with a README

2. **Push your files to GitHub**

   ```bash
   # In your project folder (E-portfolio), run:
   git init
   git add .
   git commit -m "Initial commit — SDD4007 E-portfolio"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/e-portfolio.git
   git push -u origin main
   ```

3. **Enable GitHub Pages**
   - Go to your repository on GitHub
   - Click **Settings** → **Pages** (in the left sidebar)
   - Under "Source", select **Deploy from a branch**
   - Branch: **main**, folder: **/ (root)**
   - Click **Save**
   - Wait 1–2 minutes — your site will be live at:
     **`https://YOUR-USERNAME.github.io/e-portfolio/`**

### If You Already Have the Repository

```bash
git add .
git commit -m "Add SDD4007 E-portfolio files"
git push
```

Then make sure GitHub Pages is enabled as above.

---

## File Structure

```
E-portfolio/
├── index.html      ← Main portfolio page (edit this!)
├── styles.css      ← All styling (don't need to edit)
├── script.js       ← Interactions & animations (don't need to edit)
├── SPEC.md         ← Design specification
└── README.md       ← This file
```

---

## Customising Colours & Fonts

All colours and settings are stored as CSS variables in `styles.css`. Edit the `:root` section to quickly change the entire look:

```css
:root {
  --bg-primary:   #0f1117;    /* Main background */
  --accent-blue:  #58a6ff;    /* Primary accent colour */
  --accent-green: #3fb950;    /* Secondary accent */
  --accent-coral: #f78166;    /* Tertiary accent */
  --text-primary: #e6edf3;    /* Main text */
  /* ... see styles.css for all variables */
}
```

---

## Key Features

- **Dark professional theme** — designed to look polished and developer-focused
- **Fully responsive** — works on desktop, tablet, and mobile
- **Animated skill bars** — fill up on scroll with count-up percentages
- **Scroll-reveal animations** — sections fade in as you scroll
- **Sticky navigation** — with active section highlighting
- **Mobile hamburger menu** — clean navigation on small screens
- **Print-ready** — clean layout when printed

---

## Grading Checklist (SDD4007 CA)

Use this to make sure you've covered everything:

### Part A – About Me (15%)
- [ ] Self-introduction with background, interests, and career-relevant info
- [ ] Key competencies listed
- [ ] Evidence: at least 2 projects with descriptions, your role, and outcomes
- [ ] Evidence: extracurricular activities with achievements

### Part B – Career Goal & Plan (15%)
- [ ] Clear career goal statement with detailed explanation
- [ ] Specific steps to reach the goal (education, experience, networking)
- [ ] Skills to learn identified with how and when you plan to acquire them

### Part C – Portfolio Design & Presentation (10%)
- [ ] Clear labelled sections in logical order
- [ ] Easy-to-read fonts (Inter / Arial / Calibri) throughout
- [ ] Bullet points and short paragraphs
- [ ] Visual elements: profile photo, project screenshots, skill charts

### General
- [ ] Entire portfolio is in **English**
- [ ] Published on an **online platform** (GitHub Pages ✓)
- [ ] Original work — no AI-generated content, no plagiarism

---

## Need Help?

- **GitHub Pages Docs:** https://docs.github.com/en/pages
- **HTML/CSS learning:** https://developer.mozilla.org
- **Free images for projects:** https://unsplash.com
- **Git basics:** https://git-scm.com/docs/gittutorial

---

*Replace this README with your own after customisation!*

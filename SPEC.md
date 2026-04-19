# E-Portfolio — SDD4007 CA Specification

## 1. Concept & Vision

A professional, dark-themed personal E-portfolio for a Higher Diploma in Software Development student. The portfolio presents a polished, developer-focused identity — clean and readable, with confident use of color and typography that signals technical competence without being intimidating. It feels like a senior student's work: intentional, structured, and ready to show an employer.

## 2. Design Language

**Aesthetic direction:** Dark professional developer portfolio — inspired by modern open-source developer profiles (GitHub Dark + linear.app). Deep backgrounds with cool-toned accents. Confident, precise, and calm.

**Color palette:**
- Background primary: `#0f1117`
- Background secondary: `#161b22`
- Background card: `#1c2128`
- Accent primary: `#58a6ff` (cool blue — links, highlights)
- Accent secondary: `#3fb950` (green — success, progress bars)
- Accent tertiary: `#f78166` (coral — badges, tags)
- Text primary: `#e6edf3`
- Text secondary: `#8b949e`
- Border: `#30363d`

**Typography:**
- Headings: `'Inter', sans-serif` (Google Fonts) — weights 600, 700
- Body: `'Inter', sans-serif` — weight 400, 500
- Code/tech tags: `'JetBrains Mono', monospace` (Google Fonts)

**Spatial system:**
- Base unit: 8px
- Section padding: 80px vertical
- Card padding: 24px
- Border radius: 12px for cards, 8px for tags

**Motion philosophy:**
- Entrance: fade-in + translateY(20px) → translateY(0), 500ms ease-out
- Staggered card reveals: 100ms delay between each
- Hover: scale(1.02) + shadow lift on cards, 200ms ease
- Skill bars animate width from 0% to target on scroll into view
- Navigation: smooth scroll behavior

**Visual assets:**
- Icons: Lucide icons (CDN, SVG inline)
- Profile photo: circular crop placeholder with initials fallback
- Decorative: subtle gradient blob behind hero section

## 3. Layout & Structure

**Page structure:**
```
[Sticky Navigation Bar]
[Hero Section] — name, title, tagline, CTA buttons
[About Me] — self-introduction + photo
[Skills] — technical skill bars + soft skills tags
[Projects] — 2 project cards (placeholder)
[Activities] — 2 activity cards (placeholder)
[Career Goal & Plan] — goal statement + roadmap
[Footer] — contact links
```

**Responsive strategy:**
- Desktop: max-width 1100px centered, 2-column grids
- Tablet (768px): single column, adjusted font sizes
- Mobile (<480px): full-width cards, compact nav

## 4. Features & Interactions

- **Smooth scroll navigation** — clicking nav links scrolls to sections
- **Active nav highlighting** — current section highlighted in nav bar
- **Scroll-reveal animations** — sections animate in on scroll
- **Skill bar animation** — bars fill when section enters viewport
- **Project/Activity cards** — hover lift effect with shadow
- **Mobile hamburger menu** — slides in from right on small screens
- **Print styles** — clean print layout without animations

## 5. Component Inventory

| Component | States |
|---|---|
| Nav bar | Default, scrolled (adds shadow), active link highlighted |
| Hero section | Animated gradient blob background |
| Section heading | Centered, with decorative underline accent |
| Profile card | Photo + bio text, circular photo with border |
| Skill bar | Animated fill on scroll, label + percentage |
| Tech tag | Small pill badge, monospace font |
| Project card | Default, hover (scale + shadow), image, title, tags, description |
| Activity card | Default, hover (scale + shadow), icon, title, role, description |
| Timeline item | Left border accent, year badge, content |
| CTA button | Primary (blue fill), secondary (outlined), hover states |
| Footer | Icon links (GitHub, LinkedIn, Email) |

## 6. Technical Approach

- **Platform:** GitHub Pages (static HTML/CSS/JS)
- **No build step required** — single `index.html` + linked assets
- **Fonts:** Google Fonts (Inter, JetBrains Mono)
- **Icons:** Lucide CDN or inline SVG
- **JavaScript:** Vanilla JS, no frameworks — handles nav, scroll animations, skill bars

---

## Content Summary (Placeholder)

### Part A — About Me
- Name: [YOUR FULL NAME] (placeholder)
- Programme: Higher Diploma in Software Development
- Skills: Python, Java, JavaScript, HTML/CSS, SQL, C#
- Projects: 2 placeholder projects (web app + desktop app)
- Activities: 2 placeholder extracurricular activities

### Part B — Career Goal
- Goal: Full-Stack Developer
- Steps: Further education, certifications, internships, networking
- Skills to learn: React, Node.js, Docker, Cloud platforms, Git advanced

### Part C — Design
- Clear labeled sections in logical order
- Inter font (easy to read), bullet points throughout
- Visual elements: photo placeholder, skill bars, project screenshots (placeholder images)

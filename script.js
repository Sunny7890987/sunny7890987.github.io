/**
 * E-Portfolio — SDD4007 — script.js
 * Handles: sticky nav, mobile menu, scroll reveal, skill bar animation,
 *          active nav highlighting, Lucide icon initialisation.
 */

document.addEventListener('DOMContentLoaded', () => {

  // ── Initialise Lucide icons ──────────────────────────────
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }

  // ── DOM references ───────────────────────────────────────
  const navbar       = document.getElementById('navbar');
  const navToggle    = document.getElementById('navToggle');
  const navLinks     = document.getElementById('navLinks');
  const navLinkItems = document.querySelectorAll('.nav-link');
  const revealEls    = document.querySelectorAll('.reveal');
  const skillFills   = document.querySelectorAll('.skill-bar-fill');

  // ── Sticky navbar: add shadow on scroll ─────────────────
  function handleNavbarScroll() {
    if (window.scrollY > 20) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }
  window.addEventListener('scroll', handleNavbarScroll, { passive: true });
  handleNavbarScroll();

  // ── Mobile hamburger menu ────────────────────────────────
  navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('open');
    const isOpen = navLinks.classList.contains('open');
    navToggle.setAttribute('aria-expanded', String(isOpen));
  });

  // Close mobile menu when a link is clicked
  navLinkItems.forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
      navToggle.setAttribute('aria-expanded', 'false');
    });
  });

  // ── Active nav link highlighting on scroll ────────────────
  const sections = document.querySelectorAll('section[id]');

  function highlightActiveNav() {
    const scrollPos = window.scrollY + 100;

    sections.forEach(section => {
      const sectionTop    = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      const sectionId     = section.getAttribute('id');

      if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
        navLinkItems.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === `#${sectionId}`) {
            link.classList.add('active');
          }
        });
      }
    });
  }

  window.addEventListener('scroll', highlightActiveNav, { passive: true });
  highlightActiveNav();

  // ── Scroll-reveal animations ──────────────────────────────
  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
          // Stagger sibling reveals slightly
          const siblings = entry.target.parentElement.querySelectorAll('.reveal');
          const idx = Array.from(siblings).indexOf(entry.target);
          setTimeout(() => {
            entry.target.classList.add('visible');
          }, idx * 80);
          revealObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
  );

  revealEls.forEach(el => revealObserver.observe(el));

  // ── Skill bar fill animation ─────────────────────────────
  const skillObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const fill = entry.target;
          const width = fill.getAttribute('data-width');
          const pct   = fill.closest('.skill-item').querySelector('.skill-pct');

          // Animate width
          setTimeout(() => {
            fill.style.width = width + '%';
          }, 200);

          // Count up percentage
          if (pct) {
            let current = 0;
            const step = Math.ceil(parseInt(width) / 30);
            const timer = setInterval(() => {
              current = Math.min(current + step, parseInt(width));
              pct.textContent = current + '%';
              if (current >= parseInt(width)) clearInterval(timer);
            }, 40);
          }

          skillObserver.unobserve(fill);
        }
      });
    },
    { threshold: 0.3 }
  );

  skillFills.forEach(fill => skillObserver.observe(fill));

});

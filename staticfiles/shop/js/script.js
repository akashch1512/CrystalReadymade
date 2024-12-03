'use strict';

// Modal functionality
const modal = document.querySelector('[data-modal]');
const modalCloseBtn = document.querySelector('[data-modal-close]');
const modalCloseOverlay = document.querySelector('[data-modal-overlay]');

if (modal && modalCloseBtn && modalCloseOverlay) {
  const modalCloseFunc = () => modal.classList.add('closed');
  modalCloseOverlay.addEventListener('click', modalCloseFunc);
  modalCloseBtn.addEventListener('click', modalCloseFunc);
}

// Notification toast functionality
const notificationToast = document.querySelector('[data-toast]');
const toastCloseBtn = document.querySelector('[data-toast-close]');

if (notificationToast && toastCloseBtn) {
  toastCloseBtn.addEventListener('click', () => {
    notificationToast.classList.add('closed');
  });
}

// Mobile menu functionality
const mobileMenuOpenBtns = document.querySelectorAll('[data-mobile-menu-open-btn]');
const mobileMenus = document.querySelectorAll('[data-mobile-menu]');
const mobileMenuCloseBtns = document.querySelectorAll('[data-mobile-menu-close-btn]');
const overlay = document.querySelector('[data-overlay]');

if (mobileMenuOpenBtns.length && mobileMenus.length && mobileMenuCloseBtns.length && overlay) {
  mobileMenuOpenBtns.forEach((btn, i) => {
    const mobileMenuCloseFunc = () => {
      mobileMenus[i]?.classList.remove('active');
      overlay.classList.remove('active');
    };

    btn.addEventListener('click', () => {
      mobileMenus[i]?.classList.add('active');
      overlay.classList.add('active');
    });

    mobileMenuCloseBtns[i]?.addEventListener('click', mobileMenuCloseFunc);
    overlay.addEventListener('click', mobileMenuCloseFunc);
  });
}

// Accordion functionality
const accordionBtns = document.querySelectorAll('[data-accordion-btn]');
const accordions = document.querySelectorAll('[data-accordion]');

if (accordionBtns.length && accordions.length) {
  accordionBtns.forEach((btn) => {
    btn.addEventListener('click', function () {
      const isActive = this.nextElementSibling?.classList.contains('active');

      if (!isActive) {
        accordions.forEach((acc, idx) => {
          acc.classList.remove('active');
          accordionBtns[idx].classList.remove('active');
        });
      }

      this.nextElementSibling?.classList.toggle('active');
      this.classList.toggle('active');
    });
  });
}

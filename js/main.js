// ===== KOPQO AI — SHARED UTILITIES =====

// Toast notifications
function showToast(message, type = 'success') {
  let container = document.querySelector('.toast-container');
  if (!container) {
    container = document.createElement('div');
    container.className = 'toast-container';
    document.body.appendChild(container);
  }
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  const icon = type === 'success' ? '✓' : type === 'error' ? '✕' : 'i';
  toast.innerHTML = `<span style="color:${type==='success'?'#34C759':type==='error'?'#FF453A':'var(--accent)'}">${icon}</span> ${message}`;
  container.appendChild(toast);
  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(8px)';
    toast.style.transition = '200ms ease-out';
    setTimeout(() => toast.remove(), 200);
  }, 2800);
}

// Copy to clipboard
async function copyText(text, btn) {
  try {
    await navigator.clipboard.writeText(text);
    const orig = btn.textContent;
    btn.textContent = 'Copied';
    setTimeout(() => { btn.textContent = orig; }, 1800);
    showToast('Copied to clipboard');
  } catch (e) {
    showToast('Copy failed', 'error');
  }
}

// Mobile menu toggle
function toggleMenu() {
  const menu = document.getElementById('mobileMenu');
  if (menu) menu.classList.toggle('open');
}

// Highlight active nav link
function setActiveNav() {
  const path = window.location.pathname;
  document.querySelectorAll('.nav-links a, .mobile-menu a').forEach(a => {
    if (path.includes(a.getAttribute('href'))) {
      a.style.color = 'var(--white)';
      a.style.background = 'var(--glass-bg)';
    }
  });
}
document.addEventListener('DOMContentLoaded', setActiveNav);

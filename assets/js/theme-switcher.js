// Add preload class to body initially
document.body.classList.add('preload');

function setTheme(theme) {
  // Apply theme immediately
  document.documentElement.setAttribute('data-theme', theme);
  document.body.style.backgroundColor = theme === 'dark' ? '#1a1a1a' : '#fdfdfd';
  document.body.style.color = theme === 'dark' ? '#f5f5f5' : '#111';

  // Store theme
  localStorage.setItem('theme', theme);
}

function toggleTheme() {
  const currentTheme = localStorage.getItem('theme') || 'light';
  const newTheme = currentTheme === 'light' ? 'dark' : 'light';
  setTheme(newTheme);
}

// Initialize theme
const savedTheme = localStorage.getItem('theme') || 'light';
setTheme(savedTheme);

// Remove preload class after page load
window.addEventListener('load', () => {
  requestAnimationFrame(() => {
    document.body.classList.remove('preload');
  });
});

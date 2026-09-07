// Set the theme before the page paints. Storage can be unavailable in private browsers.
try{const saved=localStorage.getItem('deepak-theme');document.documentElement.dataset.theme=saved==='light'||saved==='dark'?saved:(matchMedia('(prefers-color-scheme: light)').matches?'light':'dark')}catch{}

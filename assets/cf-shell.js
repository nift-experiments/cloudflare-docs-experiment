(()=>{const K='ui-mode',m=matchMedia('(prefers-color-scheme: dark)'),read=()=>{try{let v=localStorage.getItem(K);return /^(light|dark|auto)$/.test(v||'')?v:'auto'}catch{return'auto'}},apply=()=>{let p=read(),v=p==='auto'?(m.matches?'dark':'light'):p,r=document.documentElement;if(v==='dark')r.setAttribute('data-mode','dark');else r.removeAttribute('data-mode');r.dataset.theme=v;r.dataset.nbPref=p;r.dataset.nbState=v;r.style.colorScheme=v};window.__nbApplyTheme=apply;apply();m.addEventListener('change',()=>{if(read()==='auto')apply()});addEventListener('storage',e=>{if(e.key===K)apply()});addEventListener('DOMContentLoaded',()=>{document.querySelector('[data-theme-toggle]')?.addEventListener('click',()=>{let p=read();localStorage.setItem(K,p==='auto'?'light':p==='light'?'dark':'auto');apply()});let d=document.querySelector('[data-mobile-sidebar]');document.querySelector('[data-menu-btn]')?.addEventListener('click',()=>d?.showModal());document.querySelector('[data-close-sidebar]')?.addEventListener('click',()=>d?.close())})})();

// CP5 delegated compatibility behaviours.
document.addEventListener('click', (event) => {
  const tab = event.target.closest('[role="tab"][data-tab-target]');
  if (tab) {
    const root = tab.closest('.nb-tabs');
    root.querySelectorAll('[role="tab"]').forEach(x => x.setAttribute('aria-selected', x === tab ? 'true' : 'false'));
    root.querySelectorAll('.nb-tab-panel').forEach(x => x.hidden = x.id !== tab.dataset.tabTarget);
  }
  const feedback = event.target.closest('[data-feedback]');
  if (feedback) { feedback.textContent = 'Thanks for the feedback'; feedback.disabled = true; }
});

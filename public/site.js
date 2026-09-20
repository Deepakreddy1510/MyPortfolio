const toggle=document.querySelector('.theme-toggle');
function labelTheme(){toggle?.setAttribute('aria-label',`Switch to ${document.documentElement.dataset.theme==='light'?'dark':'light'} mode`)}
labelTheme();toggle?.addEventListener('click',()=>{const theme=document.documentElement.dataset.theme==='light'?'dark':'light';document.documentElement.dataset.theme=theme;try{localStorage.setItem('deepak-theme',theme)}catch{}labelTheme()});
const time=document.querySelector('[data-clock]');
function updateClock(){if(time)time.textContent=new Intl.DateTimeFormat('en-GB',{hour:'2-digit',minute:'2-digit',timeZone:'Asia/Kolkata'}).format(new Date())+' / IST'}
updateClock();if(time)setInterval(updateClock,60000);
// Replace null with '/assets/resume.pdf' when the real resume has been supplied.
const RESUME_URL=null;
for(const link of document.querySelectorAll('[data-resume]')){if(RESUME_URL){link.href=RESUME_URL;link.removeAttribute('aria-controls')}else link.addEventListener('click',e=>{e.preventDefault();const note=document.querySelector('#resume-note');if(note){note.hidden=false;note.focus();note.scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth',block:'center'})}})}
const heatmap=document.querySelector('#heatmap');
if(heatmap){
  const endpoint='https://github-contributions-api.jogruber.de/v4/Deepakreddy1510?y=last';
  const status=document.querySelector('#activity-loading');
  let refreshing=false;
  let lastChecked=0;
  async function refreshActivity(){
    if(refreshing)return;
    refreshing=true;
    const controller=new AbortController();
    const timeout=setTimeout(()=>controller.abort(),15000);
    try{
      const response=await fetch(endpoint,{signal:controller.signal});
      if(!response.ok)throw Error('unavailable');
      const data=await response.json();
      if(!Array.isArray(data.contributions)||!data.contributions.length)throw Error('empty');
      const days=data.contributions;
      if(!days.every(d=>/^\d{4}-\d{2}-\d{2}$/.test(d.date)&&Number.isInteger(d.count)&&d.count>=0&&Number.isInteger(d.level)&&d.level>=0&&d.level<=4))throw Error('invalid');
      days.sort((a,b)=>a.date.localeCompare(b.date));
      const total=days.reduce((sum,d)=>sum+d.count,0);
      document.querySelector('#activity-total').textContent=total.toLocaleString();
      document.querySelector('#activity-best').textContent=Math.max(...days.map(d=>d.count));
      document.querySelector('#activity-days').textContent=days.filter(d=>d.count>0).length;
      document.querySelector('#activity-period').textContent='LAST 12 MONTHS';
      lastChecked=Date.now();
      const checked=new Intl.DateTimeFormat(undefined,{dateStyle:'medium',timeStyle:'short'}).format(new Date(lastChecked));
      document.querySelector('#activity-updated').textContent='Auto-updating · Checked '+checked+' · Source updates hourly';
      heatmap.setAttribute('aria-label',`${total} GitHub contributions from ${days[0].date} to ${days.at(-1).date}. Automatically updated.`);
      const offset=new Date(days[0].date+'T12:00:00Z').getUTCDay();
      const weeks=Math.ceil((days.length+offset)/7);
      const months=document.querySelector('#calendar-months');
      months.style.setProperty('--weeks',weeks);
      heatmap.replaceChildren();months.replaceChildren();
      let previousMonth='';
      for(let i=0;i<weeks*7;i++){
        const day=days[i-offset];
        const cell=document.createElement('i');cell.dataset.level=day?.level??0;
        cell.title=day?`${day.count} contribution${day.count===1?'':'s'} on ${day.date}`:'Outside displayed period';
        cell.setAttribute('aria-hidden','true');heatmap.appendChild(cell);
        if(day){
          const month=day.date.slice(0,7);
          if(month!==previousMonth){
            const label=document.createElement('span');
            label.textContent=new Intl.DateTimeFormat('en',{month:'short',timeZone:'UTC'}).format(new Date(day.date+'T12:00:00Z'));
            label.style.gridColumn=String(Math.floor(i/7)+1);label.style.gridRow='1';
            months.appendChild(label);previousMonth=month;
          }
        }
      }
      status.hidden=true;document.querySelector('#activity-content').hidden=false;
    }catch{
      status.hidden=false;
      status.textContent=lastChecked?'Could not refresh. Showing the last loaded activity; retrying automatically.':'Activity is temporarily unavailable. Retrying automatically; you can also view it on GitHub.';
    }finally{clearTimeout(timeout);refreshing=false;}
  }
  refreshActivity();
  setInterval(()=>{if(!document.hidden)refreshActivity()},5*60*1000);
  document.addEventListener('visibilitychange',()=>{if(!document.hidden&&Date.now()-lastChecked>=5*60*1000)refreshActivity()});
}

// Both projects remain readable without JavaScript; enhance into a compact selector.
const picker=document.querySelector('.project-picker');
const panels=[...document.querySelectorAll('.project-panel')];
const projectControls=[...document.querySelectorAll('[data-project-select]')];
let selectedProject=0;
function selectProject(index){
  if(!Number.isInteger(index)||index<0||index>=panels.length)return;
  selectedProject=index;
  panels.forEach((panel,i)=>{panel.hidden=i!==index});
  projectControls.forEach(control=>{const active=Number(control.dataset.projectSelect)===index;control.setAttribute('aria-selected',String(active));control.tabIndex=active?0:-1});
  const number=String(index+1).padStart(2,'0');
  document.querySelector('#selected-project-title').textContent=panels[index].querySelector('h3').textContent;
  document.querySelector('#selected-project-count').textContent=`${number}/02`;
  document.querySelector('#project-position').textContent=`${number} OF 02`;
  picker.open=false;
}
if(picker&&panels.length){
  selectProject(location.hash==='#project-02'?1:0);
  projectControls.forEach(control=>{
    control.addEventListener('click',()=>{selectProject(Number(control.dataset.projectSelect));if(control.getAttribute('role')==='option')picker.querySelector('summary').focus()});
    control.addEventListener('keydown',event=>{
      const role=control.getAttribute('role');
      const group=projectControls.filter(c=>c.getAttribute('role')===role);
      let index=group.indexOf(control);
      if(['ArrowDown','ArrowRight'].includes(event.key))index=(index+1)%group.length;
      else if(['ArrowUp','ArrowLeft'].includes(event.key))index=(index+group.length-1)%group.length;
      else if(event.key==='Home')index=0;
      else if(event.key==='End')index=group.length-1;
      else return;
      event.preventDefault();
      if(role==='tab')selectProject(index);
      group.forEach((c,i)=>{c.tabIndex=i===index?0:-1});group[index].focus();
    });
  });
  picker.querySelector('summary').addEventListener('keydown',event=>{
    if(event.key==='ArrowDown'){event.preventDefault();picker.open=true;picker.querySelector(`[data-project-select="${selectedProject}"]`).focus()}
  });
  picker.addEventListener('keydown',event=>{if(event.key==='Escape'&&picker.open){event.preventDefault();picker.open=false;picker.querySelector('summary').focus()}});
  document.addEventListener('click',event=>{if(!picker.contains(event.target))picker.open=false});
  window.addEventListener('hashchange',()=>{if(location.hash==='#project-01'||location.hash==='#project-02')selectProject(location.hash==='#project-02'?1:0)});
}
const ticker=document.querySelector('.tools-ticker');
const tickerToggle=document.querySelector('.ticker-toggle');
tickerToggle?.addEventListener('click',()=>{
  const paused=ticker.classList.toggle('paused');
  tickerToggle.setAttribute('aria-pressed',String(paused));
  tickerToggle.setAttribute('aria-label',paused?'Play moving tools':'Pause moving tools');
  tickerToggle.title=paused?'Play moving tools':'Pause moving tools';
});

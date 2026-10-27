// ---- core: helpers, store, perms, modals, forms, router, shell ----
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const SK='toolii-'+V.id+'-state',LK='toolii-'+V.id+'-layout';
const ld=k=>{try{return JSON.parse(localStorage.getItem(k))}catch(e){return null}},sv=(k,v)=>{try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}};
let S=ld(SK);if(!S||S.v!==3){S=seed();S.role=V.role||'gp'}let L=ld(LK)||{};const T0=Date.now();
const persist=()=>sv(SK,S),ACT={},ON={};
const now=()=>620+Math.floor((Date.now()-T0)/60000);
const hm=m=>String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0');
const money=c=>'$'+(c/100).toFixed(2);
const P=id=>S.pts.find(p=>p.id==id),AP=id=>S.appts.find(a=>a.id==id);
const nm=p=>p?p.fn+' '+p.ln:'Unmatched';
const MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
const dobS=d=>{const[y,m,dd]=d.split('-');return +dd+' '+MON[m-1]+' '+y};
const age=d=>{const t=new Date(),b=new Date(d);let a=t.getFullYear()-b.getFullYear();if(t<new Date(t.getFullYear(),b.getMonth(),b.getDate()))a--;return a};
const mcm=p=>'0••• ••••• '+p.mc.slice(-3);
const inv$=i=>i.items.reduce((s,x)=>s+x[1],0);
const bal=pid=>S.inv.filter(i=>i.p==pid&&i.st!=='void'&&i.st!=='draft').reduce((s,i)=>s+inv$(i)-i.paid,0);
const ROLE={reception:'Reception',gp:'Doctor',manager:'Practice manager'};
const PERM={reception:['appt','patient','billing','recall','comms'],gp:['appt','patient','clin.view','clin.write','results','rx','comms','recall','bill.view'],manager:['appt','patient','billing','billing.waive','recall','reports','admin','audit','comms','bill.view']};
const can=p=>PERM[S.role].includes(p);
const audit=(a,e)=>{S.audit.unshift({t:hm(now()),r:ROLE[S.role],a,e});S.audit.length=Math.min(S.audit.length,200);persist()};
function need(p,what){if(can(p))return true;
 openModal({title:'Not permitted for '+ROLE[S.role],body:`<p>${esc(what||'This action')} needs the <b>${p}</b> permission.</p><p class="muted">Illustrative only. A real build enforces this on the server (policies, tenant-scoped) and keeps need-to-know: reception does not see clinical notes.</p>`,foot:'<button class="btn" data-act="close">Close</button>'});return false}
// ---- chips & pipes ----
const chip=(k,t)=>`<span class="chip c-${k}">${esc(t)}</span>`;
const ST={local:['neu','Saved locally'],sent:['info','Sent, awaiting acknowledgement'],ack:['ok','Acknowledged'],review:['warn','Needs review'],fail:['bad','Failed, retry available'],off:['neu','Not connected (simulated)'],unc:['warn','Outcome uncertain']};
const stChip=s=>chip(...ST[s]);
const pipe=a=>`<ol class="pipe">${a.map(([l,s,sub])=>`<li class="${s}"><b>${l}</b><span class="sr"> (${{done:'done',cur:'in progress',pend:'not yet',rev:'needs review',fail:'failed'}[s]})</span><small>${sub}</small></li>`).join('')}</ol>`;
const SC={booked:['neu','Booked'],online:['neu','Online booked'],arrived:['warn','Waiting'],with:['info','With doctor'],billing:['warn','At billing'],invoiced:['info','Invoiced'],paid:['ok','Paid'],done:['neu','Completed'],dna:['bad','Did not attend'],cancelled:['neu','Cancelled']};
const stOf=a=>V.stOf?V.stOf(a):SC[a.st],sk=a=>V.sk?V.sk(a):a.st;
const scChip=a=>chip(...stOf(a));
// ---- toast / modal / forms ----
let tt;function toast(m,k){const t=$('#toast');t.textContent=m;t.className='toast '+(k||'');t.hidden=false;clearTimeout(tt);tt=setTimeout(()=>t.hidden=true,4200)}
let MODAL=null;
function openModal(m){MODAL=m;const d=$('#dlg');d.className=m.size||'';d.innerHTML=`<form method="dialog" data-form="1" novalidate><header><h2 id="dlgT">${esc(m.title)}</h2><button class="x" type="button" data-act="close" aria-label="Close">×</button></header><div class="mb">${m.body}</div><footer>${m.foot||''}</footer></form>`;d.setAttribute('aria-labelledby','dlgT');if(!d.open)d.showModal();const f=$('input:not([type=hidden]),select,textarea',d);m.focus!==false&&f&&f.focus()}
const closeModal=()=>{const d=$('#dlg');d.open&&d.close();MODAL=null};
function confirmDlg(title,msg,ok,fn,danger){openModal({title,body:`<p>${msg}</p>`,foot:`<button class="btn" type="button" data-act="close">Cancel</button><button class="btn ${danger?'bad':'pri'}" type="button" id="okb">${ok}</button>`});$('#okb').onclick=()=>{closeModal();fn()}}
function fld(f,vals,errs){const v=vals[f.k]??f.v??'',id='f-'+f.k,er=errs&&errs[f.k],d=er?` aria-invalid="true" aria-describedby="e-${f.k}"`:'';let c;
 if(f.t==='select')c=`<select id="${id}" name="${f.k}"${d}>${f.o.map(o=>`<option value="${esc(o[0])}"${o[0]==v?' selected':''}>${esc(o[1])}</option>`).join('')}</select>`;
 else if(f.t==='textarea')c=`<textarea id="${id}" name="${f.k}" rows="${f.r||3}"${d}>${esc(v)}</textarea>`;
 else if(f.t==='checkbox')return `<div class="fld chk"><label><input type="checkbox" id="${id}" name="${f.k}"${v?' checked':''}${d}> <span>${f.l}</span></label>${er?`<div class="err" id="e-${f.k}">${esc(er)}</div>`:''}</div>`;
 else c=`<input id="${id}" name="${f.k}" type="${f.t||'text'}" value="${esc(v)}"${f.ph?` placeholder="${esc(f.ph)}"`:''}${f.list?` list="${f.list}"`:''}${d}>`;
 return `<div class="fld"><label for="${id}">${f.l}${f.req?' <span class="req">(required)</span>':''}</label>${c}${f.hint?`<div class="hint">${f.hint}</div>`:''}${er?`<div class="err" id="e-${f.k}">${esc(er)}</div>`:''}</div>`}
function formModal({title,fields,submit,save,size,extra,foot}){let vals={},sf;const draw=(errs)=>{
 openModal({title,size,body:(extra||'')+(errs&&errs._&&`<div class="notice bad" role="alert">${esc(errs._)}</div>`||'')+fields.map(f=>f.h?`<h3 class="sh">${f.h}</h3>`:fld(f,vals,errs)).join(''),foot:(foot||'')+`<button class="btn" type="button" data-act="close">Cancel</button><button class="btn pri" type="submit">${submit||'Save'}</button>`,focus:!errs});MODAL.submit=()=>sf();
 if(errs){const e=$('[aria-invalid]',$('#dlg'));e&&e.focus()}};
 draw();sf=()=>{const fd=new FormData($('#dlg form'));vals={};fields.forEach(f=>f.k&&(vals[f.k]=f.t==='checkbox'?fd.has(f.k):(fd.get(f.k)??'').toString().trim()));
  const errs={};fields.forEach(f=>{if(!f.k)return;if(f.req&&!vals[f.k])errs[f.k]=f.l.replace(/ \(.*/,'')+' is required.';if(!errs[f.k]&&f.chk){const r=f.chk(vals[f.k],vals);if(r)errs[f.k]=r}});
  if(!Object.keys(errs).length){const r=save(vals);if(r){if(typeof r==='string')errs._=r;else if(r.k)errs[r.k]=r.m}}
  if(Object.keys(errs).length){draw(errs);return}closeModal()}}
document.addEventListener('submit',e=>{if(e.target.dataset.form){e.preventDefault();MODAL&&MODAL.submit&&MODAL.submit()}});
// ---- panels (collapsible, remembered) ----
function pnl(id,title,body,meta,cls){const o=L[id]!==false;return `<section class="panel ${cls||''}" data-p="${id}"><h2><button class="ph" aria-expanded="${o}" aria-controls="${id}-b" data-act="pnl" data-id="${id}"><svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6l4 4 4-4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="pt">${title}</span><span class="pm">${meta||''}</span></button></h2><div class="pb" id="${id}-b"${o?'':' hidden'}>${body}</div></section>`}
ACT.pnl=el=>{const id=el.dataset.id,o=el.getAttribute('aria-expanded')!=='true';el.setAttribute('aria-expanded',o);$('#'+id+'-b').hidden=!o;L[id]=o;sv(LK,L)};
// ---- router ----
const LAND='book';
let CUR=location.hash.slice(2)||LAND;
const rt=()=>{const p=CUR.split('/');return{v:p[0]||LAND,a:p[1],b:p[2],c:p[3]}};
const go=h=>{CUR=h;closeModal();try{history.replaceState(null,'','#/'+h)}catch(e){}R();scrollTo(0,0)};
addEventListener('hashchange',()=>{const h=location.hash.slice(2)||LAND;if(h!==CUR)go(h)});
document.addEventListener('click',e=>{const a=e.target.closest('a[href^="#/"]');if(a&&!a.dataset.act){e.preventDefault();go(a.getAttribute('href').slice(2))}});
const NAV0=[['book','Appointments','M4 5h16v15H4zM4 10h16M9 3v4M15 3v4'],['wait','Waiting room','M12 7v5l3 2M12 3a9 9 0 100 18 9 9 0 000-18z'],['pts','Patients','M12 12a4 4 0 100-8 4 4 0 000 8zM4 21c0-4 4-6 8-6s8 2 8 6'],['res','Results','M7 3h10v18H7zM10 8h4M10 12h4M10 16h2'],['bill','Billing','M4 6h16v12H4zM4 10h16M8 15h3'],['rec','Recalls and reminders','M5 12a7 7 0 0112-5l2-2v6h-6l2.5-2.5A4.5 4.5 0 007.5 12M19 12a7 7 0 01-12 5l-2 2v-6h6l-2.5 2.5A4.5 4.5 0 0016.5 12'],['inbox','Messages and tasks','M4 6h16v12H4zM4 7l8 6 8-6'],['comp','Compliance and integrations','M12 3l8 3v6c0 5-4 8-8 9-4-1-8-4-8-9V6zM9 12l2 2 4-4'],['set','Settings','M4 7h10M18 7h2M4 17h2M10 17h10M14 5v4M8 15v4']];
const NAV=V.nav?V.nav(NAV0):V.cal?[['today','Today','M3 11l9-8 9 8M5 9v11h14V9'],NAV0[0],NAV0[2],NAV0[3],NAV0[4],NAV0[1],NAV0[5],NAV0[6],NAV0[7],NAV0[8]]:NAV0;
const ico=d=>`<svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><path d="${d}" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
const badge=k=>{const n={today:S.appts.filter(a=>a.d===0&&a.st==='arrived').length,res:S.results.filter(r=>r.st!=='reviewed').length,wait:S.appts.filter(a=>a.d===0&&a.st==='arrived').length,inbox:S.msgs.filter(m=>m.st==='unread'||m.st==='fail').length+S.tasks.filter(t=>!t.done&&t.who===S.role).length}[k];return n?`<span class="nb" aria-label="${n} pending">${n}</span>`:''};
const LBL=k=>(V.labels&&V.labels[k])||NAV.find(n=>n[0]===k)[1];
const CHV='<svg class="gc" width="14" height="14" viewBox="0 0 16 16" aria-hidden="true"><path d="M6 4l4 4-4 4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
const navA=(k,cur)=>{const i=NAV.findIndex(n=>n[0]===k),[kk,,d]=NAV[i],l=LBL(kk);return `<a href="#/${kk}" ${cur===kk||(kk==='pts'&&cur==='consult')?'aria-current="page"':''} class="${i<5?'pri':'sec'}" title="${l}">${ico(d)}<span class="nl">${l}</span>${badge(kk)}</a>`};
function navHTML(r){if(!V.groups)return NAV.map(n=>navA(n[0],r.v)).join('');const cv=r.v==='consult'?'pts':r.v;return V.groups.map(g=>{const links=g.items.map(k=>navA(k,r.v)).join('');if(!g.label)return `<div class="grp flat">${links}</div>`;const open=g.items.includes(cv)||L['g-'+g.key]!==false;return `<div class="grp"><button class="grp-h" type="button" data-act="grpT" data-id="${g.key}" aria-expanded="${open}">${g.label}${CHV}</button><div class="grp-b"${open?'':' hidden'}>${links}</div></div>`}).join('')}
ACT.grpT=el=>{const k='g-'+el.dataset.id,o=el.getAttribute('aria-expanded')==='true';L[k]=!o;sv(LK,L);R()};
const pageTitle=r=>{const n=NAV.find(x=>x[0]===(r.v==='consult'?'pts':r.v));return n?LBL(n[0]):'Today'};
function topHTML(r){if(V.topHtml)return V.topHtml(r);if(!V.pms)return `<header class="top"><button class="cmd" type="button" data-act="palette"><svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><circle cx="7" cy="7" r="4.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M10.5 10.5L14 14" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg><span>Search a patient or run an action</span><span class="kbd">Ctrl K</span></button><span class="who chip c-neu">${ROLE[S.role]}</span></header>`;
 return `<header class="top pms"><button class="trig" type="button" data-act="railT" aria-label="Show or hide the menu"><svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v14H4zM9 5v14" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg></button><span class="crumb">${pageTitle(r)}</span><div class="mid"><button class="cmd" type="button" data-act="palette"><svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><circle cx="7" cy="7" r="4.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M10.5 10.5L14 14" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg><span>Search patients, press / or Ctrl K</span></button></div><span class="clinic">Harbour Street Medical (demo)</span><button class="cmdk" type="button" data-act="palette" aria-label="Search and commands (Ctrl K)"><svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 9V6a3 3 0 10-3 3zm0 0h6m-6 0v6m6-6V6a3 3 0 113 3zm0 0v6m0 0h3a3 3 0 11-3 3zm0 0H9m0 0v3a3 3 0 11-3-3z" fill="none" stroke="currentColor" stroke-width="1.6"/></svg><kbd>Ctrl K</kbd></button><button class="btn pri newpt" type="button" data-act="newPt"><svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg><span>New patient</span></button></header>`}
function shell(inner){const r=rt();return `<a class="skip" href="#main" data-act="skip">Skip to main content</a><div class="demo"><a href="index.html">All variants</a><span>Look-and-feel mockup. Synthetic data, simulated integrations, nothing is sent.</span><span class="sp"></span><label>Role <select id="roleSel" data-on="role">${Object.keys(ROLE).map(k=>`<option value="${k}"${S.role===k?' selected':''}>${ROLE[k]}</option>`).join('')}</select></label><button type="button" data-act="expandAll">Expand panels</button><button type="button" data-act="resetDemo">Reset demo data</button></div>
<div class="app"><nav class="navb" aria-label="Main"><div class="logo">${V.logo||'PMS'}<small>${DOCS.nair.n}, Harbour St (demo)</small></div>${navHTML(r)}<button class="more" type="button" data-act="more" aria-haspopup="dialog">${ico('M5 12h.01M12 12h.01M19 12h.01')}<span>More</span></button>${V.rail&&!V.pms?`<button class="railt" type="button" data-act="railT" aria-pressed="${!!L.rail}">${L.rail?'Collapse menu':'Pin menu open'}</button>`:''}${V.pms?`<div class="usr"><span class="av">${ini(DOCS.nair.n)}</span><span class="un"><b>${S.role==='gp'?'Priya Nair':S.role==='reception'?'Alex Morgan':'Sam Okoro'}</b><small>${ROLE[S.role]}</small></span></div>`:`<div class="foot">Demo clock ${hm(now())}. <span class="kbd">Ctrl K</span> for any action.</div>`}</nav>
<main class="main" id="main" tabindex="-1">${topHTML(r)}${(V.pms||V.pg)?`<div class="pg">${V.bar?V.bar():''}${inner}</div>`:`${V.bar?V.bar():''}${inner}`}</main></div>`}
ACT.more=()=>openModal({title:'More',size:'sm',body:`<ul class="morel">${NAV.slice(5).map(([k,l,d])=>`<li><a href="#/${k}">${ico(d)} ${LBL(k)}</a></li>`).join('')}</ul>`,foot:'<button class="btn" data-act="close">Close</button>'});
ACT.skip=()=>{const m=$('#main');m&&m.focus()};ACT.railT=()=>{L.rail=V.railOpen?(L.rail===false):!L.rail;sv(LK,L);R()};ACT.close=closeModal;ACT.expandAll=()=>{L={};sv(LK,L);R()};
ACT.resetDemo=()=>confirmDlg('Reset demo data','This restores the synthetic data. Nothing else is affected.','Reset',()=>{S=seed();S.role=V.role||'gp';persist();go(LAND);toast('Demo data reset.')});
ON.role=el=>{S.role=el.value;persist();audit('Switched demo role',ROLE[S.role]);R();toast('Role: '+ROLE[S.role]+'. Landing screen and permissions changed.')};
// ---- render loop (keeps focus and caret) ----
const VIEWS={};
function R(){const a=document.activeElement,k=a&&a!==document.body?(a.id?'#'+a.id:a.dataset&&a.dataset.act?`[data-act="${a.dataset.act}"][data-id="${a.dataset.id||''}"]`:null):null,cp=a&&a.selectionStart!=null?a.selectionStart:null;
 const cb0=$('.calbox');if(cb0)UI.cy=cb0.scrollTop;const r=rt(),f=VIEWS[r.v]||VIEWS[LAND];$('#app').innerHTML=shell(f(r));typeof afterR==='function'&&afterR();
 if(k){const n=$(k);if(n){n.focus({preventScroll:true});if(cp!=null)try{n.setSelectionRange(cp,cp)}catch(e){}}}}
document.addEventListener('click',e=>{const t=e.target.closest('[data-act]');if(!t)return;if(t.tagName==='A')e.preventDefault();const f=ACT[t.dataset.act];f&&f(t,e)});
document.addEventListener('input',e=>{const t=e.target.closest('[data-on="input"]');t&&ON[t.dataset.fn]&&ON[t.dataset.fn](t)});
document.addEventListener('change',e=>{const t=e.target.closest('[data-on]');t&&t.dataset.on!=='input'&&ON[t.dataset.on]&&ON[t.dataset.on](t)});
// ---- command palette ----
let PAL=[];function palette(q=''){const C=[...NAV.map(([k])=>({l:'Go to '+LBL(k),f:()=>go(k)})),{l:'New appointment',f:()=>ACT.newAppt()},{l:'New patient',f:()=>ACT.newPt()},...S.pts.map(p=>({l:'Open patient: '+nm(p),f:()=>go('pts/'+p.id)}))].filter(c=>c.l.toLowerCase().includes(q.toLowerCase())).slice(0,8);PAL=C;
 $('#palList').innerHTML=C.map((c,i)=>`<li><button type="button" data-i="${i}">${esc(c.l)}</button></li>`).join('')||'<li class="muted" style="padding:10px">No match.</li>';$$('#palList button').forEach(b=>b.onclick=()=>{$('#pal').close();PAL[b.dataset.i].f()})}
ACT.palette=()=>{$('#pal').showModal();$('#palIn').value='';palette()};
addEventListener('keydown',e=>{if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k'){e.preventDefault();ACT.palette()}else if(e.key==='/'&&!e.ctrlKey&&!e.metaKey&&!/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)&&!$('#dlg').open&&!$('#pal').open){e.preventDefault();ACT.palette()}});

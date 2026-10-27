import os,sys,base64;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from build import D, build
# Look and structure follow /home/shajib/Documents/PMS (resources/css/app.css, DESIGN.md, app-sidebar, dashboard).
NM='/home/shajib/Documents/PMS/node_modules/'
def font(face,path,weight,style='normal'):
    p=NM+path
    if not os.path.exists(p):return ''
    b=base64.b64encode(open(p,'rb').read()).decode()
    return f"@font-face{{font-family:'{face}';font-style:{style};font-weight:{weight};font-display:swap;src:url(data:font/woff2;base64,{b}) format('woff2')}}\n"
FONTS=(font('Schibsted Grotesk','@fontsource-variable/schibsted-grotesk/files/schibsted-grotesk-latin-wght-normal.woff2','400 900')
 +font('Instrument Sans','@fontsource-variable/instrument-sans/files/instrument-sans-latin-wght-normal.woff2','400 700')
 +font('DM Mono','@fontsource/dm-mono/files/dm-mono-latin-400-normal.woff2','400')
 +font('DM Mono','@fontsource/dm-mono/files/dm-mono-latin-500-normal.woff2','500'))
tokens=FONTS+""":root{
--bg:oklch(0.972 0.008 85);--surface:oklch(1 0.002 85);--surface-2:oklch(0.948 0.01 85);--hover:oklch(0.935 0.035 298 / .55);--line:oklch(0.895 0.012 85);--line-strong:oklch(0.6 0.02 285);
--text:oklch(0.22 0.025 290);--muted:oklch(0.45 0.025 285);--brand:oklch(0.48 0.17 295);--brand-hover:oklch(0.43 0.17 295);--on-brand:oklch(1 0.004 295);--link:oklch(0.4 0.15 295);--focus:oklch(0.5 0.17 295);
--nav-bg:oklch(0.953 0.012 85);--nav-fg:oklch(0.3 0.03 290);--nav-hi:oklch(0.32 0.13 295);--nav-active:oklch(1 0.002 85);--nav-focus:oklch(0.48 0.17 295);--nav-line:oklch(0.89 0.014 85);
--sel:oklch(0.935 0.035 298);--sel-line:oklch(0.48 0.17 295);--warn-solid:oklch(0.48 0.17 295);--warn-solid-fg:oklch(1 0.004 295);--closed:oklch(0.945 0.008 85);
--demo-bg:oklch(0.22 0.03 290);--demo-fg:oklch(0.95 0.02 298);--toast-bg:oklch(0.22 0.025 290);--toast-fg:oklch(1 0 0);--ai-bg:oklch(0.96 0.025 298);--ai-fg:oklch(0.32 0.13 295);--ai-line:oklch(0.62 0.13 295);
--r:.875rem;--rc:.625rem;--navw:16rem;--ease-out:cubic-bezier(.16,1,.3,1);
--font:'Instrument Sans',ui-sans-serif,system-ui,sans-serif;--head:'Schibsted Grotesk','Instrument Sans',ui-sans-serif,system-ui,sans-serif;--headw:600;--mono:'DM Mono',ui-monospace,'SF Mono',Menlo,monospace}"""
skin="""
:root{--ok-bg:oklch(0.95 0.04 160);--ok-fg:oklch(0.42 0.1 160);--ok-line:oklch(0.8 0.08 160);--warn-bg:oklch(0.96 0.06 85);--warn-fg:oklch(0.45 0.11 70);--warn-line:oklch(0.82 0.09 85);--bad-bg:oklch(0.95 0.04 25);--bad-fg:oklch(0.45 0.17 25);--bad-line:oklch(0.8 0.09 25);--info-bg:oklch(0.95 0.025 250);--info-fg:oklch(0.4 0.12 250);--info-line:oklch(0.8 0.06 250);--neu-bg:oklch(0.935 0.01 85);--neu-fg:oklch(0.42 0.03 285);--danger:oklch(0.5 0.19 27)}
html{scrollbar-width:thin;scrollbar-color:color-mix(in oklch,var(--brand) 26%,transparent) transparent}
body{font-size:15px;text-rendering:optimizeLegibility}h1,h2,h3,dialog h2{font-family:var(--head);letter-spacing:-.02em;text-wrap:balance}
th{font-weight:500}.mono,.book .t,.ct,.kbd,kbd{font-family:var(--mono);font-variant-numeric:tabular-nums}
::selection{background:var(--sel);color:var(--nav-hi)}
.skip{background:var(--brand)}
.app{background:var(--nav-bg)}
@media (min-width:900px){
.navb{padding:12px 0;display:flex;flex-direction:column;gap:2px}
.navb .logo{display:flex;align-items:center;gap:10px;font:600 1.2rem var(--head);letter-spacing:-.02em;color:var(--nav-hi);padding:6px 20px 16px}
.navb .logo::before{content:"T";display:grid;place-items:center;width:32px;height:32px;border-radius:10px;background:var(--brand);color:var(--on-brand);font:600 17px var(--head);flex:none;box-shadow:inset 0 1px 0 oklch(1 0 0/.2)}
.navb .logo small{display:none}
.grp{padding:2px 12px}.grp-h{color:var(--nav-fg)}
.navb a{height:40px;gap:12px;padding:0 12px;border-radius:.5rem;font-size:.9375rem;transition:background-color .15s ease-out,color .15s ease-out}
.navb a svg{width:18px;height:18px;color:color-mix(in oklch,var(--nav-fg) 60%,transparent)}
.navb a:hover{background:color-mix(in oklch,var(--nav-active) 70%,transparent);color:var(--nav-fg)}
.navb a[aria-current]{background:var(--nav-active);color:var(--nav-hi);font-weight:500;box-shadow:0 1px 2px oklch(0.3 0.04 290/.1),0 0 0 1px var(--nav-line)}
.navb a[aria-current] svg{color:var(--brand)}
}
.nb{background:var(--brand);color:var(--on-brand);font-size:11px;font-weight:500;line-height:18px;padding:0 6px}
.usr{margin-top:auto;display:flex;gap:10px;align-items:center;padding:12px 20px 4px;border-top:1px solid var(--nav-line)}.usr .av{background:var(--sel);color:var(--nav-hi);width:34px;height:34px}.usr b{display:block;font-size:14px;font-weight:500}.usr small{display:block;font-size:12px;color:color-mix(in oklch,var(--nav-fg) 70%,transparent)}
@media (max-width:899px){.usr,.trig{display:none}}
@media (min-width:900px){
.app{padding:8px 8px 8px 0;min-height:calc(100vh - 38px)}
.navb{height:calc(100vh - 54px);top:46px}
.main{background:var(--bg);border-radius:var(--r);box-shadow:0 1px 3px oklch(0.3 0.04 290/.08);padding:0;background-image:radial-gradient(58rem 26rem at 8% -6%,color-mix(in oklch,var(--brand) 8%,transparent),transparent 70%);background-repeat:no-repeat;min-height:calc(100vh - 54px);overflow:clip}
body.rail-c .app{grid-template-columns:4.5rem minmax(0,1fr)}}
.top.pms{display:flex;align-items:center;gap:12px;height:64px;margin:0;padding:0 16px;border-bottom:1px solid var(--line);background:color-mix(in oklch,var(--bg) 88%,transparent)}
@media (min-width:900px){.top.pms{padding:0 24px;position:sticky;top:0;z-index:30;backdrop-filter:blur(8px)}}
.trig{flex:none;width:36px;height:36px;display:grid;place-items:center;border:0;background:none;border-radius:8px;color:var(--muted);margin-left:-4px}.trig:hover{background:var(--sel);color:var(--nav-hi)}
.crumb{display:none;font-weight:500;color:var(--text)}@media (min-width:1100px){.crumb{display:block}}
.top.pms .mid{flex:1;display:flex;justify-content:center;min-width:0}
.top.pms .cmd{flex:0 1 30rem;height:40px;min-height:40px;border-radius:999px;border-color:var(--line-strong);background:var(--surface);font-size:14px;margin:0}
.clinic{display:none;max-width:12rem;font-size:14px;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}@media (min-width:1280px){.clinic{display:block}}
.cmdk{height:40px;display:inline-flex;align-items:center;gap:6px;padding:0 12px;border:1px solid var(--line-strong);border-radius:.5rem;background:var(--surface);color:var(--muted);font-size:14px}.cmdk:hover{background:var(--sel);color:var(--nav-hi)}.cmdk kbd{font-size:12px;display:none}@media (min-width:900px){.cmdk kbd{display:inline}}
.newpt{height:40px;padding:0 14px;border-radius:.5rem;margin:0;box-shadow:inset 0 1px 0 oklch(1 0 0/.18),0 1px 2px oklch(0.3 0.1 295/.3)}
@media (max-width:620px){.newpt span{display:none}.newpt{padding:0 12px}.top.pms .cmd span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
.pg{max-width:80rem;margin:0 auto;padding:16px 16px 40px}@media (min-width:900px){.pg{padding:24px 24px 48px}}
.vh h1{font-size:1.5rem;font-weight:600}
.panel{border-radius:var(--r);box-shadow:none}.ph{border-radius:var(--r)}.pt{font-weight:600}
.btn{height:40px;border-radius:var(--rc);font-weight:500;transition:background-color .15s ease-out,border-color .15s ease-out,transform .15s ease-out}.btn.sm{height:34px;min-height:34px}
.btn.pri{box-shadow:inset 0 1px 0 oklch(1 0 0/.18),0 1px 2px oklch(0.3 0.1 295/.3)}
.chip{font-weight:500;font-size:12px}
.fld input:not([type=checkbox]),.fld select,.fld textarea{border-radius:var(--rc)}
.tbl th{font-weight:500}
.cap{border-radius:8px}.cs.closed{background:var(--closed)}.calbox{border-radius:var(--r)}
.pms .seg [aria-pressed=true]{background:var(--brand);color:var(--on-brand);box-shadow:none}.seg{border-radius:var(--rc)}.btn-group .btn:first-child{border-radius:var(--rc) 0 0 var(--rc)}
.calbar{display:none}.chead .kbd{display:none}.cdin{width:8.6rem}.cdsel{width:10rem}
body.pmsv .calbox{height:calc(100vh - 342px);min-height:420px}body.pmsv.fullcal .calbox{height:calc(100vh - 170px)}
@media (max-width:899px){body.pmsv .calbox{height:calc(100vh - 520px);min-height:320px}}.chead .btn.pri{height:36px;min-height:36px}.chead .btn{height:36px;min-height:36px}
/* Today */
.rise{animation:rise .7s var(--ease-out) both;animation-delay:calc(var(--i,0)*70ms)}
@keyframes rise{from{opacity:0;transform:translateY(12px);filter:blur(6px)}to{opacity:1;transform:none;filter:none}}
.dh{display:flex;flex-wrap:wrap;gap:16px;align-items:flex-end;justify-content:space-between;padding-bottom:24px}
.dh h1{font:600 clamp(1.9rem,4.5vw,2.5rem)/1.05 var(--head);letter-spacing:-.02em;margin:0}.dh p{margin-top:6px;font-size:14px;color:var(--muted)}
.pulse{display:flex;gap:4px;margin-bottom:6px}.pulse span{flex:1;height:10px;border-radius:999px;background:color-mix(in oklch,var(--sc,var(--st-booked)) 24%,var(--surface-2));min-width:6px}
.pulse span.s-done,.pulse span.s-paid,.pulse span.s-invoiced,.pulse span.s-billing{background:var(--sc)}.pulse span.s-with{background:var(--brand)}.pulse span.s-arrived{background:var(--warn-fg)}.pulse span.nx{box-shadow:0 0 0 2px var(--surface),0 0 0 3px var(--brand)}
.pulsel{font-size:13px;color:var(--muted);margin-bottom:16px}
.pills{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 28px;font-size:14px}.pills a{display:inline-flex;gap:8px;align-items:center;min-height:36px;padding:0 14px;border:1px solid var(--line);border-radius:999px;background:var(--surface);text-decoration:none;color:var(--text);transition:transform .2s ease-out,border-color .2s ease-out,background-color .2s ease-out}.pills a:hover{transform:translateY(-1px);border-color:color-mix(in oklch,var(--brand) 40%,transparent);background:color-mix(in oklch,var(--sel) 50%,transparent)}.pills .w{background:var(--warn-bg);color:var(--warn-fg);border-color:var(--warn-line)}.pills b{font-weight:600}
.dg{display:grid;gap:24px;grid-template-columns:minmax(0,1fr)}@media (min-width:1280px){.dg{grid-template-columns:minmax(0,1fr) 24rem}}
.dp{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:20px;margin:0}.dp>header{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:12px}.dp h2{font-size:1rem;font-weight:600;margin:0}
.link-s{font-size:13px;color:var(--link);text-decoration:none;display:inline-flex;align-items:center;gap:2px}.link-s:hover{text-decoration:underline}
.tlx{position:relative;display:grid;gap:4px;margin:0;padding:0;list-style:none}.tlx::before{content:"";position:absolute;top:8px;bottom:8px;left:calc(4.5rem + 12px + .6rem);width:1px;background:linear-gradient(to bottom,color-mix(in oklch,var(--brand) 40%,transparent),var(--line),transparent)}
.tlx li{position:relative;display:grid;grid-template-columns:4.5rem 1.2rem minmax(0,1fr);gap:4px 12px;align-items:start;padding:10px 0;border-radius:12px;transition:background-color .2s ease-out}.tlx li:hover{background:color-mix(in oklch,var(--sel) 40%,transparent)}
.tt{text-align:right;font-size:14px;font-weight:500;padding-top:1px}
.dotx{position:relative;z-index:1;width:10px;height:10px;margin:6px auto 0;border-radius:50%;border:2px solid var(--sc,var(--st-booked));background:var(--surface);transition:background-color .5s ease-out,box-shadow .5s ease-out}
.dotx.s-done,.dotx.s-paid,.dotx.s-invoiced,.dotx.s-billing{background:var(--sc)}.dotx.s-with{background:var(--brand);border-color:var(--brand);box-shadow:0 0 0 4px color-mix(in oklch,var(--brand) 22%,transparent)}.dotx.s-arrived{background:var(--warn-fg);border-color:var(--warn-fg)}
.tc{min-width:0}.tn{font-weight:500;color:var(--text);text-decoration:none}.tn:hover{text-decoration:underline}.tc p{margin:0;font-size:14px;color:var(--muted)}.tc .row-actions{margin-top:6px}.tlx .dim{opacity:.6}
.tlx .nowm{padding:2px 0;align-items:center;background:none!important}.nowm .tt{color:var(--brand);font-size:12px}.nowd{position:relative;z-index:1;width:10px;height:10px;margin:0 auto;border-radius:50%;background:var(--brand)}.nowl2{font-size:12px;font-weight:600;color:var(--brand);display:flex;align-items:center;gap:10px}.nowl2::after{content:"";flex:1;height:1px;background:color-mix(in oklch,var(--brand) 45%,transparent)}
.upnext{background:var(--brand);color:var(--on-brand);border-radius:var(--r);padding:20px;margin:0}.upnext h2{font-size:.875rem;font-weight:600;color:color-mix(in oklch,var(--on-brand) 85%,transparent);margin:0}.upnext .big{font:500 2.25rem/1.1 var(--mono);letter-spacing:-.02em;margin-top:12px}.upnext p{margin:2px 0 0;font-size:14px;color:color-mix(in oklch,var(--on-brand) 85%,transparent)}.upnext .who2{font:500 1.125rem var(--font);color:var(--on-brand);margin-top:16px}
.upnext .btn{margin-top:16px;background:var(--surface);color:var(--nav-hi);border-color:transparent}.upnext .btn:hover{background:var(--sel)}
.uf{display:grid;gap:2px;margin:0;padding:0;list-style:none;font-size:14px}.uf a{display:flex;justify-content:space-between;gap:8px;padding:10px 8px;margin:0 -8px;border-radius:8px;color:var(--text);text-decoration:none;transition:background-color .2s ease-out}.uf a:hover{background:color-mix(in oklch,var(--sel) 50%,transparent)}.uf .n{background:var(--warn-bg);color:var(--warn-fg);border-radius:999px;padding:0 8px;font-size:12px;font-variant-numeric:tabular-nums}
.tk{display:grid;margin:0;padding:0;list-style:none}.tk li{display:flex;gap:10px;align-items:flex-start;padding:10px 0;font-size:14px}.tk input{appearance:none;flex:none;width:18px;height:18px;margin:2px 0 0;border:1px solid var(--line-strong);border-radius:50%;background:var(--surface);transition:transform .2s ease-out,border-color .2s ease-out,background-color .2s ease-out;cursor:pointer}.tk input:hover{transform:scale(1.1);border-color:var(--brand);background:var(--sel)}.tk input:checked{background:var(--brand);border-color:var(--brand)}
.dp .empty{padding:12px 0}
@media (max-width:620px){.tlx li{grid-template-columns:3.4rem 1rem minmax(0,1fr);gap:4px 8px}.tlx::before{left:calc(3.4rem + 8px + .5rem)}}
"""
vjs="const V={id:'halaxy',cal:true,pms:true,rail:true,railOpen:true,sheet:true,ptTable:true,cs:420,ce:1140,title:'Today',groups:[{key:'home',items:['today','pts']},{key:'schedule',label:'Schedule',items:['book','wait','rec','inbox']},{key:'clinical',label:'Clinical',items:['res']},{key:'finance',label:'Finance',items:['bill']},{key:'compliance',label:'Compliance',items:['comp']},{key:'settings',label:'Settings',items:['set']}],home:()=>hxHome()};\n"
post=r"""
S.req=S.req||[{id:1,p:7,when:'Tomorrow 14:00',doc:'hendry',st:'pending'},{id:2,p:null,name:'Priyanka Sethi',when:'Friday 14:00',st:'review'}];
const reqPanel=()=>pnl('hx-b','Online booking requests',S.req.map(r=>`<div class="q"><span><b>${esc(r.p?nm(P(r.p)):r.name)}</b><br><span class="muted">${r.when}</span></span><span>${r.st==='pending'?`<button class="btn pri sm" type="button" data-act="reqOk" data-id="${r.id}">Confirm</button><button class="btn sm" type="button" data-act="reqNo" data-id="${r.id}">Decline</button>`:r.st==='review'?chip('warn','Needs review: new patient, not matched')+`<button class="btn sm" type="button" data-act="newPt">Register patient</button>`:r.st==='ok'?chip('ok','Confirmed, SMS simulated'):chip('neu','Declined')}</span></div>`).join(''),S.req.filter(r=>r.st==='pending'||r.st==='review').length+' need you');
ACT.reqOk=el=>{if(!need('appt'))return;const r=S.req.find(x=>x.id==el.dataset.id);r.st='ok';S.appts.push({id:++S.next,p:r.p,doc:r.doc,d:1,t:840,dur:20,ty:'std',st:'online',why:'Booked online'});audit('Confirmed online booking',nm(P(r.p)));persist();R();toast('Confirmed. Confirmation SMS simulated, nothing sent.')};
ACT.reqNo=el=>{S.req.find(x=>x.id==el.dataset.id).st='no';persist();R()};
function hxHome(){const nowM=now(),hr=Math.floor(nowM/60),first=S.role==='gp'?'Priya':S.role==='reception'?'Alex':'Sam';
 const day=S.appts.filter(a=>a.d===0&&a.st!=='cancelled').sort((a,b)=>a.t-b.t),live=day.filter(a=>a.st!=='dna');
 const open=a=>['booked','online','arrived'].includes(a.st),next=live.find(a=>open(a)&&a.t>=nowM-15)||live.find(open);
 const waiting=day.filter(a=>a.st==='arrived').length,rev=S.results.filter(r=>r.st!=='reviewed').length,sentence=`${live.length} appointments, ${waiting} waiting${can('results')?', '+rev+' results to review':''}`;
 const owing=S.pts.reduce((s,p)=>s+bal(p.id),0),drafts=S.notes.filter(n=>n.st==='draft').length,toIssue=S.inv.filter(i=>i.st==='draft').length;
 let marked=false;const rows=day.map(a=>{let m='';if(!marked&&a.t>=nowM){marked=true;m=`<li class="nowm" aria-label="Now ${hm(nowM)}"><span class="tt mono">${hm(nowM)}</span><span class="nowd"></span><span class="nowl2">Now</span></li>`}
  const p=P(a.p),dim=['dna'].includes(a.st)?' dim':'';
  return m+`<li class="${dim}"><span class="tt mono">${hm(a.t)}</span><span class="dotx s-${a.st}" aria-hidden="true"></span><div class="tc"><a class="tn" href="#/pts/${a.p}" data-act="openPt" data-id="${a.p}" data-ctx="${a.id}">${esc(nm(p))}</a> ${scChip(a)}<p>${TYPES[a.ty][0]}, ${a.dur} min${a.why?', '+esc(a.why):''}, ${DOCS[a.doc].s}</p>${open(a)||a.st==='with'?`<div class="row-actions">${a.st==='booked'||a.st==='online'?`<button class="btn sm" type="button" data-act="arrive" data-id="${a.id}">Arrive</button>`:''}${open(a)?`<button class="btn pri sm" type="button" data-act="start" data-id="${a.id}">Start visit</button>`:`<button class="btn pri sm" type="button" data-act="open" data-id="${a.id}">Back to consult</button>`}</div>`:''}</div></li>`}).join('')+(marked?'':`<li class="nowm"><span class="tt mono">${hm(nowM)}</span><span class="nowd"></span><span class="nowl2">Now</span></li>`);
 const mins=next?next.t-nowM:0,cd=!next?'':next.st==='arrived'?'In the building, waiting':mins>0?'In '+mins+' min':mins===0?'Starting now':(-mins)+' min ago';
 return `<div class="dh rise" style="--i:0"><div><h1>Good ${hr<12?'morning':hr<17?'afternoon':'evening'}, ${first}</h1><p>${dayFull(0)}, <span class="num">${hm(nowM)}</span>, ${sentence}</p></div><div class="row-actions" style="margin:0"><a class="btn" href="#/book">Open calendar</a><button class="btn pri" type="button" data-act="newAppt">New appointment</button></div></div>
 <div class="rise" style="--i:1"><div class="pulse" role="img" aria-label="${sentence}">${live.map(a=>`<span class="s-${a.st}${a===next?' nx':''}" title="${hm(a.t)} ${esc(nm(P(a.p)))}, ${SC[a.st][1]}"></span>`).join('')}</div><p class="pulsel">${sentence}</p></div>
 <ul class="pills rise" style="--i:2" aria-label="Quick links"><li><a href="#/wait">Waiting room <b class="num">${waiting}</b></a></li><li><a class="${owing>0?'w':''}" href="#/bill/debt">Outstanding <b class="num">${money(owing)}</b></a></li><li><a class="${drafts?'w':''}" href="#/pts">Notes to sign <b class="num">${drafts}</b></a></li><li><a href="#/rec">Recalls due <b class="num">${S.recalls.filter(r=>r.st==='due').length}</b></a></li></ul>
 <div class="dg"><section class="dp rise" style="--i:3" aria-labelledby="sch"><header><h2 id="sch">Today's schedule</h2><a class="link-s" href="#/book">Open calendar &rsaquo;</a></header>${day.length?`<ol class="tlx">${rows}</ol>`:'<p class="empty muted">Nothing booked today. Book from the calendar.</p>'}</section>
 <div style="display:grid;gap:24px;align-content:start"><section class="upnext rise" style="--i:4" aria-labelledby="un"><h2 id="un">Up next</h2>${next?`<p class="big">${hm(next.t)}</p><p>${cd}</p><p class="who2">${esc(nm(P(next.p)))}</p><p>${esc(next.why||TYPES[next.ty][0])}</p><a class="btn" href="#/pts/${next.p}" data-act="openPt" data-id="${next.p}">Open record &rsaquo;</a>`:'<p style="margin-top:12px">No more appointments today.</p>'}</section>
 <section class="dp rise" style="--i:5" aria-labelledby="uf"><header><h2 id="uf">Unfinished</h2></header><ul class="uf">${can('clin.view')?`<li><a href="#/pts"><span>Notes to sign</span><span class="n">${drafts}</span></a></li>`:''}${can('results')?`<li><a href="#/res"><span>Results to review</span><span class="n">${rev}</span></a></li>`:''}<li><a href="#/bill"><span>Invoices to issue</span><span class="n">${toIssue}</span></a></li></ul></section>
 <section class="dp rise" style="--i:6" aria-labelledby="tk"><header><h2 id="tk">Tasks</h2><a class="link-s" href="#/inbox">All tasks &rsaquo;</a></header><ul class="tk">${S.tasks.filter(t=>!t.done&&t.who===S.role).map(t=>`<li><input type="checkbox" id="t${t.id}" data-on="task" data-id="${t.id}" aria-label="Done: ${esc(t.t)}"><label for="t${t.id}">${esc(t.t)}<br><span class="muted num">${esc(t.due)}</span></label></li>`).join('')||'<li class="muted">Nothing to do.</li>'}</ul></section></div></div>
 <div class="dg" style="margin-top:24px"><div class="rise" style="--i:7">${reqPanel()}${aiPanelHome()}</div><div class="rise" style="--i:8">${integHome()}</div></div>`}
"""
build('halaxy','PMS vs Halaxy, friendly and online-first',tokens,skin,vjs,os.path.join(D,'..','toolii-vs-halaxy.html'),post)

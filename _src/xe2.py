import os,sys;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from build import D
from build import build
tokens=""":root{
--bg:#F0F4F4;--surface:#FFFFFF;--surface-2:#E7EDED;--hover:#EAF3F3;--line:#D6E0E0;--line-strong:#6F7C7C;
--text:#1C2626;--muted:#4F5B5B;--brand:#0B6B6B;--brand-hover:#085454;--on-brand:#FFFFFF;--link:#085454;--focus:#0B6B6B;
--nav-bg:#0B2E2E;--nav-fg:#CFE6E6;--nav-hi:#FFFFFF;--nav-active:#14494A;--nav-focus:#FFFFFF;--nav-line:#1F4A4A;
--sel:#D9EEEE;--sel-line:#0B6B6B;--warn-solid:#F5B301;--warn-solid-fg:#1A1200;--ok-solid:#15803D;--bad-solid:#B91C1C;--info-solid:#1D4ED8;
--demo-bg:#061A1A;--demo-fg:#CFE6E6;--toast-bg:#0B2E2E;--toast-fg:#FFFFFF;--ai-bg:#F3F0FF;--ai-fg:#4B2E83;--ai-line:#7C5CD6;
--r:10px;--rc:8px;--navw:230px;--font:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;--head:var(--font);--headw:700;--mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace}"""
skin="""
.num,.kpi b{font-variant-numeric:tabular-nums}
.kpis{display:grid;gap:10px;grid-template-columns:repeat(2,minmax(0,1fr));margin-bottom:14px}
@media (min-width:900px){.kpis{grid-template-columns:repeat(4,minmax(0,1fr))}}
.kpi{display:block;background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:12px 14px;text-decoration:none;color:var(--text);border-top:4px solid var(--brand)}
.kpi:hover{background:var(--hover)}.kpi b{display:block;font-size:26px;line-height:1.2}.kpi span{font-size:13px;color:var(--muted)}
.kpi.bad{border-top-color:var(--bad-solid)}.kpi.warn{border-top-color:var(--warn-solid)}
.fn{display:grid;grid-template-columns:minmax(90px,150px) minmax(0,1fr) 40px;gap:6px 10px;align-items:center;padding:5px 0;font-size:14px}
.fn .tr{height:14px;border-radius:99px;background:var(--surface-2);overflow:hidden}.fn .fi{height:100%;border-radius:99px;background:var(--brand);min-width:2px}
.fn .f-ok{background:var(--ok-solid)}.fn .f-warn{background:var(--warn-solid)}.fn .f-bad{background:var(--bad-solid)}.fn .f-info{background:var(--info-solid)}
.xg{display:grid;gap:0 14px;grid-template-columns:minmax(0,1fr)}
@media (min-width:1100px){.xg{grid-template-columns:repeat(2,minmax(0,1fr))}.xg .wide{grid-column:1/-1}}
.locrow[aria-current=true] td{background:var(--sel)}
.xlocs{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:12px}
"""
vjs="""const V={id:'xestro',cal:true,role:'manager',logo:'PMS',title:'Practice overview',home:()=>xeHome(),
nav:N=>{const g=k=>N.find(n=>n[0]===k)||[k,k,''];const ic={adm:'M4 20V8l8-5 8 5v12zM9 20v-6h6v6',lists:'M5 4h14v16H5zM9 9h6M9 13h6M9 17h3',tele:'M4 7h11v10H4zM15 11l5-3v8l-5-3',quote:'M6 3h9l4 4v14H6zM9 12h7M9 16h5',letters:'M4 6h16v12H4zM4 7l8 6 8-6',auto:'M13 3L5 14h6l-1 7 8-11h-6z',rep:'M5 20V10M12 20V4M19 20v-7'};
 const n=(k,l)=>[k,l,ic[k]];return [['today','Practice overview','M3 11l9-8 9 8M5 9v11h14V9'],g('book'),g('pts'),n('adm','Admissions'),g('bill'),g('wait'),n('lists','Theatre and delivery lists'),n('tele','Telehealth'),n('letters','Letters and forms'),g('res'),g('inbox'),n('auto','Automations'),n('quote','Quotes'),g('rec'),n('rep','Reports'),g('comp'),g('set')]},
labels:{today:'Practice overview',book:'Appointments',res:'Secure messaging',bill:'Billing and claims',inbox:'Messages and tasks',rec:'Recalls and lists',comp:'Compliance'},
groups:[{key:'main',items:['today']},{key:'pm',label:'Patient management',items:['book','wait','pts','adm','lists','tele']},{key:'co',label:'Correspondence',items:['letters','res','inbox','auto']},{key:'pr',label:'Practice management',items:['bill','quote','rec','rep']},{key:'ad',label:'Admin',items:['comp','set']}]};
"""
post=r"""
UI.loc='all';UI.xp=5;
const LOCS=[['Harbour Street','82%','6%',4250,3],['Northside','74%','9%',6120,5],['Telehealth hub','68%','4%',980,1]];
const fnRow=(l,n,max,k)=>`<div class="fn"><span>${l}</span><span class="tr" aria-hidden="true"><span class="fi f-${k||''}" style="display:block;width:${Math.max(2,Math.round(n/Math.max(max,1)*100))}%"></span></span><b class="num">${n}</b></div>`;
function xeHome(){const iss=S.inv.filter(i=>i.st==='issued'),billed=iss.reduce((s,i)=>s+inv$(i),0)+S.inv.filter(i=>i.st==='paid').reduce((s,i)=>s+inv$(i),0),owing=S.pts.reduce((s,p)=>s+bal(p.id),0);
 const cl=S.inv.filter(i=>i.claim),cn=k=>cl.filter(i=>i.claim.st===k).length,fix=cn('rej')+cn('unc')+integ().filter(x=>x[2]==='fail').length;
 const mx=Math.max(S.inv.length,5),p=P(UI.xp),ci=S.inv.filter(i=>i.p===p.id).slice(-1)[0];
 const sum=`This week (demo figures): ${money(billed)} billed, ${money(owing)} owing, ${cl.length} claims in flight, ${S.rem.filter(r=>r.st==='failed').length} reminders failed to send, ${S.appts.filter(a=>a.st==='dna').length} did not attend.`;
 return `<div class="xlocs" role="group" aria-label="Location"><span class="seg">${['all',...LOCS.map(l=>l[0])].map(l=>`<button type="button" aria-pressed="${UI.loc===l}" data-act="xLoc" data-id="${l}">${l==='all'?'All locations':l}</button>`).join('')}</span></div>
 <div class="kpis"><a class="kpi" href="#/bill"><b class="num">${money(billed)}</b><span>Billed, demo figures</span></a><a class="kpi warn" href="#/bill/debt"><b class="num">${money(owing)}</b><span>Owing from patients</span></a><a class="kpi" href="#/bill/claims"><b class="num">${cn('sent')}</b><span>Claims awaiting a reply</span></a><a class="kpi ${fix?'bad':''}" href="#/comp/integ"><b class="num">${fix}</b><span>Need fixing: rejected, uncertain, failed</span></a></div>
 <div class="fld" style="max-width:340px"><label for="xp">Patient, billing view only</label><select id="xp" data-on="xp">${S.pts.map(x=>`<option value="${x.id}"${x.id===UI.xp?' selected':''}>${esc(nm(x))}</option>`).join('')}</select></div>
 <section class="pstrip" aria-label="Selected patient"><div><h1>${esc(nm(p))}</h1><span class="muted">Medicare ${mcm(p)} (masked)</span></div><div class="ctx">${chip(bal(p.id)>0?'bad':'neu','Balance '+money(bal(p.id)))}${ci?ivst(ci)+(ci.claim?claimChip(ci.claim):''):chip('neu','No invoices')}${chip('neu','Clinical notes hidden: need-to-know')}</div><div class="acts"><a class="btn sm" href="#/bill">Open billing</a></div></section>
 <div class="xg"><div class="col">${pnl('x-c','Claims pipeline, simulated',fnRow('Drafts to issue',S.inv.filter(i=>i.st==='draft').length,mx,'')+fnRow('Issued, unpaid',iss.length,mx,'warn')+fnRow('Claim saved locally',cn('local'),mx,'')+fnRow('Claim sent',cn('sent'),mx,'info')+fnRow('Paid',S.inv.filter(i=>i.st==='paid').length,mx,'ok')+fnRow('Rejected or uncertain',cn('rej')+cn('unc'),mx,'bad')+`<p class="hint">Saved locally, sent and acknowledged are separate stages.</p>${cl.filter(i=>['local','rej','unc'].includes(i.claim.st)).map(i=>`<div class="q"><span><b>Invoice ${i.id}</b>, ${esc(nm(P(i.p)))} ${claimChip(i.claim)}</span><span>${i.claim.st==='local'?`<button class="btn pri sm" type="button" data-act="clmLodge" data-id="${i.id}">Lodge (simulated)</button>`:i.claim.st==='unc'?`<button class="btn sm" type="button" data-act="clmSim" data-id="${i.id}" data-r="ack">Check status</button>`:`<button class="btn sm" type="button" data-act="clmFix" data-id="${i.id}">Fix and resubmit</button>`}</span></div>`).join('')}`,'')}
 ${pnl('x-ad','Admissions and lists',(()=>{const x=X(),o=x.adm.filter(a=>a.st==='open');return fnRow('Obstetric, open',o.filter(a=>a.kind==='preg').length,6,'')+fnRow('Procedures booked',o.filter(a=>a.kind==='surg').length,6,'info')+fnRow('Consent missing',o.filter(a=>a.kind==='surg'&&!a.consent).length,6,'warn')+fnRow('Quotes awaiting reply',x.quotes.filter(q=>q.st==='sent').length,6,'warn')+`<div class="row-actions"><a class="btn sm" href="#/adm">Admissions</a><a class="btn sm" href="#/lists">Theatre list</a><a class="btn sm" href="#/quote">Quotes</a></div>`})(),'')}
 ${pnl('x-b','Bookings and recalls',fnRow('Online requests waiting',(S.req||[]).filter(r=>r.st==='pending'||r.st==='review').length,6,'warn')+fnRow('Booked tomorrow',S.appts.filter(a=>a.d===1&&a.st!=='cancelled').length,8,'')+fnRow('Recalls due',S.recalls.filter(r=>r.st==='due').length,6,'warn')+fnRow('Recalls contacted',S.recalls.filter(r=>r.st==='contacted').length,6,'info')+fnRow('Recalls booked',S.recalls.filter(r=>r.st==='booked').length,6,'ok')+fnRow('Did not attend today',S.appts.filter(a=>a.d===0&&a.st==='dna').length,6,'bad')+`<div class="row-actions"><a class="btn sm" href="#/rec">Open recalls</a><a class="btn sm" href="#/rec/reminders">SMS reminders (${S.rem.filter(r=>r.st==='failed').length} failed)</a></div>`,'')}</div>
 <div class="col">${pnl('x-l','Locations, demo figures',`<div class="scroll-x"><table class="tbl"><thead><tr><th>Location</th><th>Rooms used</th><th>Did not attend</th><th>Owing</th><th>Claims open</th></tr></thead><tbody>${LOCS.map(l=>`<tr class="locrow" aria-current="${UI.loc===l[0]}"><td><b>${l[0]}</b></td><td class="num">${l[1]}</td><td class="num">${l[2]}</td><td class="num">${money(l[3]*100)}</td><td class="num">${l[4]}</td></tr>`).join('')}</tbody></table></div>`,'compare')}
 ${pnl('x-a','Audit and compliance centre',`<ul class="tasks">${S.audit.slice(0,5).map(a=>`<li><span class="num muted">${a.t}</span><span>${a.r}: ${esc(a.a)}${a.e?', '+esc(a.e):''}</span></li>`).join('')}</ul><div class="row-actions">${chip('ok','Access review done 30 days ago')}${chip('warn','Backup check due (simulated)')}${chip((S.inc||[]).length?'warn':'neu',(S.inc||[]).length+' open incidents')}</div><div class="row-actions"><a class="btn sm" href="#/comp/audit">Audit log</a><a class="btn sm" href="#/comp/inc">Incidents</a><a class="btn sm" href="#/comp/access">Who can do what</a></div>`,'audited')}
 ${pnl('x-i','Integration status',integRows(['air','erx','clm','mhr','path','ref','sms']),'simulated')}
 <section class="panel wide" style="margin-bottom:14px"><div class="pb" style="padding-top:12px"><div class="ai"><span class="chip c-ai">AI draft, needs manager review</span><p>${esc(sum)}</p><p class="src">Built from the figures above by a simulated model. It is not shared until you approve it.</p><label><input type="checkbox" id="xai" data-on="xai" ${UI.xai?'checked':''}> <span>I have checked these figures.</span></label><div class="row-actions"><button class="btn pri" type="button" data-act="xaiOk" ${UI.xai?'':'disabled'}>Approve for owners (simulated)</button></div></div></div></section></div></div>`}
ACT.xLoc=el=>{UI.loc=el.dataset.id;R()};ON.xp=el=>{UI.xp=+el.value;R()};ON.xai=el=>{UI.xai=el.checked;R()};
ACT.xaiOk=()=>{if(!need('reports','Sharing the summary'))return;UI.xai=false;audit('Approved AI weekly summary (simulated)','');R();toast('Approved. Sharing is simulated, nothing was sent.')};
"""
post+=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'xe_views.js')).read()
build('xestro','PMS vs Xestro, practice manager',tokens,skin,vjs,os.path.join(D,'..','toolii-vs-xestro.html'),post)

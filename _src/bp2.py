import os,sys;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from build import D
from build import build
tokens="""/* tokens */:root{
--bg:#F3F4F8;--surface:#FFFFFF;--surface-2:#EEF0F5;--hover:#ECEEF5;--line:#E0E3EA;--line-strong:#7C8597;
--text:#151A24;--muted:#566074;--brand:#2540C9;--brand-hover:#1B31A3;--brand-ink:#1B31A3;--on-brand:#FFFFFF;--link:#2540C9;--focus:#2540C9;
--nav-bg:#12161F;--nav-fg:#C9D0DC;--nav-hi:#FFFFFF;--nav-active:#262E42;--nav-focus:#FFFFFF;--nav-line:#2B3347;
--sel:#E4E9FF;--sel-line:#2540C9;--warn-solid:#F5B301;--warn-solid-fg:#1A1200;
--demo-bg:#0B0E14;--demo-fg:#D5DBE6;--toast-bg:#151A24;--toast-fg:#FFFFFF;--ai-bg:#F3EEFF;--ai-fg:#4C2A9A;--ai-line:#7C5CD6;
--r:12px;--rc:8px;--navw:216px;--font:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",sans-serif;--head:var(--font);--headw:700;--mono:ui-monospace,"SF Mono","Cascadia Mono",Menlo,Consolas,monospace}"""
skin=""".navb .kbd{display:none}.book .t,.navb .foot .kbd{font-family:var(--mono)}.navb .foot .kbd{display:inline;background:transparent;color:var(--nav-fg);border-color:#4A5470}"""
vjs="""const V={id:'bp',cal:true,labels:{inbox:'In-tray'},logo:'PMS',home:()=>`${UI.sel&&AP(UI.sel)?strip(P(AP(UI.sel).p),`<button class="btn pri sm" type="button" data-act="openPt" data-id="${AP(UI.sel).p}">Open record</button>`):'<div class="pstrip"><span class="muted">Select an appointment to see the patient here.</span></div>'}<div class="hgrid"><div class="col">${bookHome()}${resHome()}</div><div class="col">${waitHome()}${aiPanelHome()}${integHome()}${recHome()}${taskHome()}</div></div>`};
"""
build('bp','PMS vs Best Practice, GP at speed',tokens,skin,vjs,os.path.join(D,'..','toolii-vs-bp.html'))

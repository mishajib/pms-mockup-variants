import sys
import os
D=os.path.dirname(os.path.abspath(__file__))+'/'
rd=lambda f:open(D+f).read()
def build(v,title,tokens,skin_css,vjs,out,post=''):
    js=vjs+rd('data.js')+rd('core.js')+rd('s1.js')+rd('s2.js')+rd('s3.js')+rd('s4.js')+post+rd('boot.js')
    html=f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; img-src data:; font-src data:; connect-src 'none'">
<title>{title}</title>
<style>
{tokens}
{rd('engine.css')}
{skin_css}
</style></head><body>
<div id="app"></div>
<dialog id="dlg"></dialog><dialog id="pal" aria-label="Command palette"><input id="palIn" type="text" placeholder="Type an action or patient name" autocomplete="off" aria-controls="palList"><ul id="palList"></ul></dialog>
<div id="ctx" role="menu" hidden></div><div class="toast" id="toast" role="status" aria-live="polite" hidden></div>
<noscript>This mockup needs JavaScript. It makes no network calls.</noscript>
<script>
(()=>{{
{js}
}})();
</script></body></html>
"""
    open(out,'w').write(html)

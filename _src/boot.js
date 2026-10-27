// boot
$('#palIn').oninput=e=>palette(e.target.value);$('#palIn').onkeydown=e=>{if(e.key==='Enter'&&PAL[0]){$('#pal').close();PAL[0].f()}};
document.getElementById('pal').addEventListener('click',e=>{if(e.target.id==='pal')e.target.close()});
document.getElementById('dlg').addEventListener('click',e=>{if(e.target.id==='dlg')closeModal()});
R();

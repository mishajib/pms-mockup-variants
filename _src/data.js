// ---- synthetic seed (no real people, Medicare numbers start with 0) ----
const DOCS={nair:{n:'Dr Priya Nair',s:'Nair',principal:true},hendry:{n:'Dr Tom Hendry',s:'Hendry'}};
const TYPES={std:['Standard consult',20],long:['Long consult',40],imm:['Immunisation',15],tele:['Telehealth',20],rev:['Review',20],ha:['Health assessment',40]};
const FEES={std:8200,long:14900,imm:3800,tele:7600,rev:8200,ha:14900};
const DRUGS=['Atorvastatin 20 mg tablet','Perindopril 4 mg tablet','Metformin 500 mg tablet','Paracetamol 500 mg tablet','Amoxicillin 500 mg capsule','Salbutamol 100 mcg inhaler','Sertraline 50 mg tablet','Levothyroxine 50 mcg tablet'];
const seed=()=>({v:3,role:'gp',next:100,
pts:[
{id:1,fn:'Marcus',ln:'Ellery',dob:'1971-08-02',sex:'M',ph:'0400 000 101',mc:'0123 45601 1',al:[],meds:[['Metformin','500 mg twice daily','reg'],['Perindopril','4 mg daily','reg']],flags:['Diabetes review due'],
 imm:[],obs:[['Weight','88.2','kg','12 Sep','Nurse'],['Blood pressure','132/84','mmHg','12 Sep','Nurse']]},
{id:2,fn:'Hana',ln:'Okafor',dob:'1995-01-19',sex:'F',ph:'0400 000 102',mc:'0123 45602 1',al:[],meds:[],flags:[],imm:[],obs:[]},
{id:3,fn:'Leo',ln:'Brandt',dob:'2019-06-11',sex:'M',ph:'0400 000 103',mc:'0123 45603 1',al:[],meds:[],flags:['Childhood schedule'],imm:[{id:1,v:'MMR dose 2',d:'Today 09:48',air:'sent',at:'09:49'}],obs:[['Weight','24.1','kg','Today','Nurse']]},
{id:4,fn:'Sofia',ln:'Marchetti',dob:'1957-03-14',sex:'F',ph:'0400 000 104',mc:'0123 45604 1',al:['Penicillin'],meds:[['Atorvastatin','20 mg daily','reg'],['Perindopril','4 mg daily','reg'],['Metformin','500 mg twice daily','reg'],['Paracetamol','500 mg up to 4 times daily','prn'],['Amlodipine','5 mg daily (ceased 02 Jun, patient request)','off']],flags:['GPMP review due'],
 imm:[{id:2,v:'Shingles dose 1',d:'12 Sep',air:'ack',at:'12 Sep'}],obs:[['Blood pressure','138/82','mmHg','12 Sep','Nurse'],['Weight','71.4','kg','12 Sep','Nurse'],['Pulse','72','bpm','12 Sep','Nurse'],['Height','162','cm','02 Jun','Nurse']]},
{id:5,fn:'Dev',ln:'Patel',dob:'1983-11-03',sex:'M',ph:'0400 000 105',mc:'0123 45605 1',al:[],meds:[],flags:[],imm:[],obs:[]},
{id:6,fn:'Ruth',ln:'Calloway',dob:'1946-09-27',sex:'F',ph:'0400 000 106',mc:'0123 45606 1',al:['Sulfonamide'],meds:[['Perindopril','4 mg daily','reg']],flags:['Flu vaccine due'],imm:[],obs:[]},
{id:7,fn:'Jin',ln:'Zhao',dob:'2001-02-08',sex:'M',ph:'0400 000 107',mc:'0123 45607 1',al:[],meds:[],flags:[],imm:[],obs:[]},
{id:8,fn:'Amara',ln:'Lindqvist',dob:'1989-04-21',sex:'F',ph:'0400 000 108',mc:'0123 45608 1',al:[],meds:[],flags:['Screening recall due'],imm:[],obs:[]},
{id:9,fn:'Tom',ln:'Reilly',dob:'1965-07-30',sex:'M',ph:'0400 000 109',mc:'0123 45609 1',al:[],meds:[['Metformin','500 mg daily','reg']],flags:[],imm:[],obs:[]},
{id:10,fn:'Ines',ln:'Duarte',dob:'2022-12-15',sex:'F',ph:'0400 000 110',mc:'0123 45610 1',al:[],meds:[],flags:['Childhood schedule'],imm:[],obs:[]}],
// d: 0 today, 1 tomorrow. st: booked online arrived with billing invoiced paid done dna cancelled
appts:[
{id:1,p:1,doc:'nair',d:0,t:540,dur:20,ty:'std',st:'paid',why:'Diabetes review'},
{id:2,p:2,doc:'hendry',d:0,t:540,dur:20,ty:'std',st:'done',why:'Skin check'},
{id:3,p:3,doc:'nair',d:0,t:580,dur:15,ty:'imm',st:'invoiced',why:'MMR dose 2'},
{id:4,p:4,doc:'nair',d:0,t:600,dur:40,ty:'long',st:'with',why:'GPMP review',arr:592},
{id:5,p:5,doc:'hendry',d:0,t:600,dur:20,ty:'std',st:'arrived',arr:592,why:'Back pain'},
{id:6,p:6,doc:'nair',d:0,t:640,dur:20,ty:'std',st:'arrived',arr:616,why:'Cough follow-up'},
{id:7,p:7,doc:'hendry',d:0,t:620,dur:20,ty:'tele',st:'booked',why:'Telehealth review'},
{id:8,p:8,doc:'nair',d:0,t:660,dur:20,ty:'rev',st:'online',why:'Booked online: review'},
{id:9,p:9,doc:'hendry',d:0,t:660,dur:20,ty:'rev',st:'booked',why:'Review'},
{id:10,p:10,doc:'nair',d:0,t:680,dur:15,ty:'imm',st:'booked',why:'Immunisation'},
{id:11,p:2,doc:'hendry',d:1,t:540,dur:20,ty:'std',st:'booked',why:'Follow-up'},
{id:12,p:5,doc:'nair',d:1,t:560,dur:20,ty:'std',st:'booked',why:'Review'},
{id:13,p:9,doc:'nair',d:1,t:600,dur:20,ty:'rev',st:'booked',why:'Blood pressure review'},
{id:14,p:7,doc:'hendry',d:1,t:620,dur:20,ty:'tele',st:'booked',why:'Telehealth'}],
results:[
{id:1,p:1,test:'HbA1c',kind:'Pathology',at:'08:12',flag:'Flagged by lab: outside reference range',st:'review'},
{id:2,p:6,test:'Chest X-ray report',kind:'Radiology',at:'08:40',flag:'Report received',st:'review'},
{id:3,p:null,test:'Urine MC&S',kind:'Pathology',at:'09:05',flag:'Patient match uncertain (surname only)',st:'unmatched'},
{id:4,p:4,test:'Lipid panel',kind:'Pathology',at:'Yesterday',flag:'Report received',st:'reviewed',by:'Dr Nair'},
{id:5,p:2,test:'Full blood count',kind:'Pathology',at:'Yesterday',flag:'Report received',st:'reviewed',by:'Dr Hendry'}],
recalls:[
{id:1,p:8,why:'Cervical screening',due:'This week',st:'due'},{id:2,p:6,why:'Influenza vaccine',due:'This week',st:'due'},
{id:3,p:4,why:'GPMP review',due:'Overdue 2 weeks',st:'contacted',last:'Sent SMS 20 Oct (simulated)'},{id:4,p:1,why:'Diabetes annual cycle',due:'Next week',st:'due'}],
rem:[{id:1,a:11,st:'queued'},{id:2,a:12,st:'queued'},{id:3,a:13,st:'failed'},{id:4,a:14,st:'failed'},{id:5,a:6,st:'yes'},{id:6,a:7,st:'no'}],
inv:[
{id:1,p:1,a:1,items:[['Standard consult (demo item)',8200]],paid:8200,st:'paid',mth:'Card',claim:null},
{id:2,p:3,a:3,items:[['Immunisation (demo item)',3800]],paid:0,st:'issued',claim:null},
{id:3,p:5,a:null,items:[['Standard consult (demo item)',8500]],paid:0,st:'issued',claim:null,old:true},
{id:4,p:2,a:2,items:[['Standard consult (demo item)',8200]],paid:0,st:'issued',mth:'Bulk bill',claim:{st:'sent',at:'09:51'}}],
notes:[
{id:1,p:4,a:4,date:'Today',au:'Dr Nair',st:'draft',S:'Here for GPMP review. Asks about flu vaccine timing.',O:'BP and weight recorded by nurse.',A:'',P:'',ai:{st:'pending',text:'Discussed GP management plan review and the upcoming cardiology visit. Patient asked when to book the flu vaccine. Medicines list reviewed with patient.'}},
{id:2,p:4,a:null,date:'12 Sep',au:'Dr Nair',st:'signed',S:'Shingles vaccine today.',O:'Observations recorded.',A:'Routine.',P:'Next review in 3 months.'},
{id:3,p:1,a:1,date:'Today',au:'Dr Nair',st:'signed',S:'Diabetes review.',O:'Weight and BP recorded.',A:'Review done.',P:'Repeat pathology ordered.'}],
rx:[{id:1,p:1,drug:'Metformin 500 mg tablet',qty:100,rep:5,st:'sent',at:'09:12'}],
ref:[{id:1,p:4,to:'Cardiology (demo specialist)',why:'Review requested',st:'fail',at:'3 days ago',offline:true}],
orders:[],
tasks:[{id:1,t:'Phone pharmacy about Marcus E. script',who:'gp',due:'11:00',done:false},{id:2,t:'Sign GPMP for Sofia M.',who:'gp',due:'After visit',done:false},{id:3,t:'Chase unmatched urine result',who:'reception',due:'Today',done:false}],
msgs:[{id:1,from:'Pathology (simulated)',sub:'Report notification',p:null,st:'unread',body:'1 result could not be matched to a patient.',dir:'in'},{id:2,from:'Reception',sub:'Patient asks about test results',p:1,st:'unread',body:'Marcus E. phoned asking about his blood test. Please advise.',dir:'in'},{id:3,from:'To Cardiology (demo specialist)',sub:'Referral for Sofia M.',p:4,st:'fail',body:'Referral letter attached. Delivery failed.',dir:'out'}],
audit:[{t:'09:48',r:'Nurse',a:'Opened record',e:'Sofia Marchetti'},{t:'10:00',r:'GP',a:'Started visit',e:'Sofia Marchetti'}],
users:[['Priya Nair','GP, principal','Today 08:02'],['Tom Hendry','GP','Today 08:30'],['Alex Morgan','Reception','Today 07:55'],['Sam Okoro','Practice manager','Yesterday']],
tmpl:{rem:'Hi {first}, reminder: appointment with {doctor} on {date} at {time}. Reply YES to confirm.',recall:'Hi {first}, you are due for {reason}. Call us or book online.'},
amb:{air:'sent'},ib:{}});

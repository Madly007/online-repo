import subprocess,os
CH='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
ICON={
'legal':'<path d="M600 250v300M470 550h260M600 270l-150 120h300z" stroke="#fff" stroke-width="14" fill="none" stroke-linejoin="round"/><path d="M450 390l-60 110h120zM750 390l-60 110h120z" stroke="#fff" stroke-width="12" fill="none"/>',
'money':'<circle cx="600" cy="400" r="130" stroke="#fff" stroke-width="14" fill="none"/><path d="M640 350c-20-25-80-25-80 15 0 45 80 25 80 70 0 40-60 45-85 15M600 320v-25M600 480v25" stroke="#fff" stroke-width="14" fill="none" stroke-linecap="round"/>',
'house':'<path d="M450 420L600 290l150 130v150H450z" stroke="#fff" stroke-width="14" fill="none" stroke-linejoin="round"/><rect x="560" y="470" width="80" height="100" stroke="#fff" stroke-width="12" fill="none"/>',
'building':'<rect x="490" y="300" width="220" height="270" stroke="#fff" stroke-width="14" fill="none"/><path d="M530 350h40M630 350h40M530 410h40M630 410h40M530 470h40M630 470h40M580 570v-50h40v50" stroke="#fff" stroke-width="12"/>',
'health':'<rect x="470" y="300" width="260" height="260" rx="30" stroke="#fff" stroke-width="14" fill="none"/><path d="M600 350v160M520 430h160" stroke="#fff" stroke-width="22" stroke-linecap="round"/>',
'shop':'<path d="M470 360h260l-20 60H490z" stroke="#fff" stroke-width="14" fill="none" stroke-linejoin="round"/><path d="M490 420v140h220V420M570 560v-70h60v70" stroke="#fff" stroke-width="14" fill="none"/>',
'school':'<path d="M600 290l190 90-190 90-190-90z" stroke="#fff" stroke-width="14" fill="none" stroke-linejoin="round"/><path d="M500 430v70c60 50 140 50 200 0v-70" stroke="#fff" stroke-width="14" fill="none"/>',
'headset':'<path d="M480 460v-50a120 120 0 0 1 240 0v50" stroke="#fff" stroke-width="16" fill="none"/><rect x="455" y="445" width="55" height="100" rx="20" fill="#fff"/><rect x="690" y="445" width="55" height="100" rx="20" fill="#fff"/><path d="M717 545c0 60-60 70-120 70" stroke="#fff" stroke-width="12" fill="none"/>',
'team':'<circle cx="530" cy="380" r="45" stroke="#fff" stroke-width="12" fill="none"/><circle cx="670" cy="380" r="45" stroke="#fff" stroke-width="12" fill="none"/><path d="M450 540c0-70 160-70 160 0M590 540c0-70 160-70 160 0" stroke="#fff" stroke-width="14" fill="none"/>',
'cloud':'<path d="M500 520a70 70 0 0 1 10-140 110 110 0 0 1 210-10 75 75 0 0 1 0 150z" stroke="#fff" stroke-width="14" fill="none" stroke-linejoin="round"/>'}
POSTS=[('01','NORTH EAST','Darlington, Durham, Newcastle','legal'),
('02','SCOTLAND','Edinburgh, Glasgow, Aberdeen','money'),
('03','LONDON AND SOUTH EAST','London, Kent, Surrey','house'),
('04','WALES','Cardiff, Swansea, Newport','building'),
('05','NORTHERN IRELAND','Belfast, Derry, Lisburn','health'),
('06','NORTH WEST','Manchester, Liverpool, Lancaster','shop'),
('07','MIDLANDS','Birmingham, Nottingham, Leicester','school'),
('08','YORKSHIRE','Leeds, Sheffield, York','headset'),
('09','SOUTH WEST','Bristol, Exeter, Plymouth','team'),
('10','NORTH EAST','Teesside, Sunderland, Newcastle','health')]
for n,reg,towns,ic in POSTS:
    svg=f'''<html><body style="margin:0"><svg xmlns="http://www.w3.org/2000/svg" width="1200" height="900" viewBox="0 0 1200 900" font-family="Carlito,Calibri,Arial,sans-serif">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0070B0"/><stop offset="1" stop-color="#123052"/></linearGradient></defs>
<rect width="1200" height="900" fill="url(#g)"/>
<g fill="none" stroke="#fff" stroke-opacity=".18" stroke-width="3"><circle cx="600" cy="420" r="230"/><circle cx="600" cy="420" r="300"/><circle cx="600" cy="420" r="370"/></g>
<circle cx="600" cy="420" r="190" fill="#0090C0" fill-opacity=".35"/>
{ICON[ic]}
<text x="600" y="705" text-anchor="middle" font-size="72" font-weight="700" fill="#fff">{reg}</text>
<text x="600" y="765" text-anchor="middle" font-size="38" fill="#cfe9f6">{towns}</text>
<rect x="0" y="830" width="1200" height="70" fill="#902080"/>
<text x="600" y="878" text-anchor="middle" font-size="34" font-weight="700" fill="#fff">BLAKE TELECOM  |  Business phone systems</text>
</svg></body></html>'''
    open(f'/tmp/p{n}.html','w').write(svg)
    subprocess.run([CH,'--headless','--no-sandbox','--disable-gpu','--hide-scrollbars',f'--screenshot=/tmp/p{n}.png','--window-size=1200,1100',f'file:///tmp/p{n}.html'],capture_output=True)
    from PIL import Image
    Image.open(f'/tmp/p{n}.png').convert('RGB').crop((0,0,1200,900)).save(f'post{n}.jpg',quality=90)
print(sorted(os.listdir('.')))

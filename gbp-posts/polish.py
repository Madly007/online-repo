import subprocess
from PIL import Image,ImageEnhance,ImageFilter
CH='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
INFO={1:("NORTH EAST","Darlington, Durham, Newcastle"),2:("SCOTLAND","Edinburgh, Glasgow, Aberdeen"),3:("LONDON AND SOUTH EAST","London, Kent, Surrey"),4:("WALES","Cardiff, Swansea, Newport"),5:("NORTHERN IRELAND","Belfast, Derry, Lisburn"),6:("NORTH WEST","Manchester, Liverpool, Lancaster"),7:("MIDLANDS","Birmingham, Nottingham, Leicester"),8:("YORKSHIRE","Leeds, Sheffield, York"),9:("SOUTH WEST","Bristol, Exeter, Plymouth"),10:("NORTH EAST","Teesside, Sunderland, Newcastle")}
import base64,io
for n in range(2,11):
    im=Image.open(f'photos/post{n:02d}.jpg').convert('RGB')
    im=ImageEnhance.Contrast(im).enhance(1.06); im=ImageEnhance.Color(im).enhance(.92); im=im.filter(ImageFilter.UnsharpMask(2,60,3))
    b=io.BytesIO(); im.save(b,'JPEG',quality=93); u='data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
    r,t=INFO[n]
    html=f'''<html><body style="margin:0"><svg xmlns="http://www.w3.org/2000/svg" width="1200" height="900" font-family="Carlito,Calibri,Arial,sans-serif">
<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset=".45" stop-color="#123052" stop-opacity="0"/><stop offset="1" stop-color="#123052" stop-opacity=".94"/></linearGradient>
<linearGradient id="t" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#123052" stop-opacity=".55"/><stop offset=".6" stop-color="#123052" stop-opacity="0"/></linearGradient></defs>
<image href="{u}" x="0" y="0" width="1200" height="900" preserveAspectRatio="xMidYMid slice"/>
<rect width="1200" height="900" fill="#0070B0" opacity=".10"/><rect width="1200" height="900" fill="url(#t)"/><rect width="1200" height="900" fill="url(#g)"/>
<rect x="60" y="600" width="8" height="160" fill="#0090C0"/>
<text x="92" y="665" font-size="30" font-weight="700" letter-spacing="6" fill="#7fd0f0">BUSINESS PHONE SYSTEMS</text>
<text x="92" y="735" font-size="68" font-weight="700" fill="#fff">{r}</text>
<text x="92" y="785" font-size="34" fill="#dcecf7">{t}</text>
<rect x="0" y="830" width="1200" height="70" fill="#902080"/>
<text x="60" y="877" font-size="32" font-weight="700" fill="#fff">BLAKE TELECOM</text>
<text x="1140" y="877" text-anchor="end" font-size="28" fill="#fff">blake-telecom.co.uk</text>
</svg></body></html>'''
    open(f'/tmp/q{n}.html','w').write(html)
    subprocess.run([CH,'--headless','--no-sandbox','--disable-gpu','--hide-scrollbars',f'--screenshot=/tmp/q{n}.png','--window-size=1200,1100',f'file:///tmp/q{n}.html'],capture_output=True)
    Image.open(f'/tmp/q{n}.png').convert('RGB').crop((0,0,1200,900)).save(f'polished{n:02d}.jpg',quality=92)
sheet=Image.new('RGB',(1200,720),'white')
for k,n in enumerate(range(2,11)):
    sheet.paste(Image.open(f'polished{n:02d}.jpg').resize((400,300)),((k%3)*400,(k//3)*240 if False else (k//3)*240))
sheet=Image.new('RGB',(1200,900),'white')
for k,n in enumerate(range(2,11)): sheet.paste(Image.open(f'polished{n:02d}.jpg').resize((400,300)),((k%3)*400,(k//3)*300))
sheet.save('polished_montage.jpg')

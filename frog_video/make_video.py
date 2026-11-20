import math, random, subprocess, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
SRC='/root/.claude/uploads/a5244dae-31cc-567a-85cf-42e3cc4fa7d0/16ac08e4-image.png'
OUT='/home/user/CFD-academy/frog_video/frog_pancakes.mp4'
SCR='/tmp/claude-0/-home-user-CFD-academy/a5244dae-31cc-567a-85cf-42e3cc4fa7d0/scratchpad/'
W,H,FPS,SCENE=1080,1920,30,5.0
img=Image.open(SRC).convert('RGB')
P=[img.crop(b) for b in [(0,0,625,625),(629,0,1254,625),(0,629,625,1254),(629,629,1254,1254)]]
FONT=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',62)
TITLES=['Маленький шеф-повар','Большой прыжок','Блинная шапка','Кулинарный триумф']
ease=lambda t:0.5-0.5*math.cos(math.pi*max(0,min(1,t)))
lerp=lambda a,b,t:a+(b-a)*t
def cam(s,t):
    # returns cx,cy,h (panel coords) and shake amplitude
    if s==0:
        k=ease(t/5); return lerp(232,222,k),lerp(330,300,k),lerp(610,520,k),0
    if s==1:
        k=ease((t-0.6)/1.8); sh=4 if 2.3<t<3.0 else 0
        return lerp(235,300,k),lerp(390,312,k),lerp(430,624,k),sh
    if s==2:
        k=ease(t/0.35); sh=6*max(0,1-(t-0.3)/0.6) if t>0.3 else 0
        h=lerp(624,470,k)-12*ease((t-1)/4)
        return lerp(270,250,k),lerp(312,300,k),h,sh
    k=ease(t/5); return lerp(250,235,k),lerp(320,330,k),lerp(610,530,k),0
def frame_base(s,t,rng):
    tq=math.floor(t*12)/12  # stop-motion "on twos"
    cx,cy,h,sh=cam(s,tq)
    w=h*9/16
    jx,jy=rng.uniform(-1,1)*(0.8+sh),rng.uniform(-1,1)*(0.8+sh)
    x0=min(max(cx-w/2+jx,0),625-w); y0=min(max(cy-h/2+jy,0),625-h)
    return P[s].resize((W,H),Image.LANCZOS,box=(x0,y0,x0+w,y0+h))
def heart(d,x,y,r,fill):
    d.ellipse([x-r,y-r,x,y],fill=fill); d.ellipse([x,y-r,x+r,y],fill=fill)
    d.polygon([(x-r,y-r/2+2),(x+r,y-r/2+2),(x,y+r)],fill=fill)
def overlay(im,s,t):
    o=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(o)
    if s==0:  # little flour sparkles
        for i in range(10):
            ph=(t*0.6+i/10)%1; x=150+i*80+20*math.sin(t*2+i); y=1500-ph*700
            a=int(200*math.sin(math.pi*ph)); d.ellipse([x-6,y-6,x+6,y+6],fill=(255,250,235,a))
    if False:  # surprise marks
        k=min(1,(t-2.2)/0.25)
        for ang in (-60,-30,0):
            a=math.radians(ang-90); x1,y1=760+90*math.cos(a)*k,520+90*math.sin(a)*k
            d.line([(760+40*math.cos(a),520+40*math.sin(a)),(x1+60*math.cos(a)*k,y1+60*math.sin(a)*k)],fill=(255,255,255,240),width=14)
    if s==2 and t>0.35:
        k=min(1,(t-0.35)/0.2); b=1+0.15*math.sin(t*10)*max(0,1-(t-0.35))
        d.text((70,330),'?!',font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',int(120*k)),fill=(255,255,255,230),stroke_width=6,stroke_fill=(180,60,60,230))
    if s==3:
        for i in range(7):
            st=0.8+i*0.55
            if t>st:
                ph=(t-st)/2.2
                if ph<1:
                    x=180+(i*137)%720+25*math.sin(ph*6+i); y=1250-ph*800
                    heart(d,x,y,int(28+10*(i%3)),(255,120,150,int(255*(1-ph))))
        if False:
            k=min(1,(t-3.2)/0.3); heart(d,840,430,int(70*k*(1+0.08*math.sin(t*8))),(255,245,235,240))
    return Image.alpha_composite(im.convert('RGBA'),o)
def caption(im,s,t):
    a=min(1,t/0.4)*min(1,(SCENE-t)/0.3)
    if a<=0: return im
    o=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(o)
    tw=d.textlength(TITLES[s],font=FONT); y=170-30*(1-a)
    d.rounded_rectangle([W/2-tw/2-45,y-25,W/2+tw/2+45,y+95],radius=55,fill=(255,248,235,int(225*a)))
    d.text((W/2,y+35),TITLES[s],font=FONT,anchor='mm',fill=(120,170,60,int(255*a)))
    return Image.alpha_composite(im,o)
ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
    '-i',SCR+'audio.wav','-c:v','libx264','-preset','medium','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',OUT],stdin=subprocess.PIPE)
# ---- audio: music-box melody + simple sfx
SR=44100; N=int(SR*20); A=np.zeros(N)
def tone(f,st,dur,vol,decay=4):
    t=np.arange(int(dur*SR))/SR; s=(np.sin(2*np.pi*f*t)+0.3*np.sin(4*np.pi*f*t))*np.exp(-decay*t)*vol
    i=int(st*SR); A[i:i+len(s)]+=s[:N-i]
notes=[523,659,784,659,587,698,880,698,523,659,784,1047,988,784,659,587]
for b in range(40):
    tone(notes[b%16],b*0.5,0.6,0.12); 
    if b%2==0: tone(notes[b%16]/2,b*0.5,0.9,0.08,2)
def sweep(st,f0,f1,dur,vol):
    t=np.arange(int(dur*SR))/SR; f=np.geomspace(f0,f1,len(t)); s=np.sin(2*np.pi*np.cumsum(f)/SR)*vol*np.exp(-2*t)
    i=int(st*SR); A[i:i+len(s)]+=s
sweep(5+0.7,250,1400,0.7,0.35)       # whoosh up (toss)
sweep(5+2.3,900,1800,0.25,0.2)       # surprise
sweep(10+0.25,500,90,0.35,0.5)       # plop on head
for k,f in enumerate([1319,1568,2093]): tone(f,15+3.2+k*0.12,1.2,0.25,3)  # triumph ding
A=np.clip(A/np.max(np.abs(A))*0.8,-1,1); fade=np.ones(N); fade[-SR:]=np.linspace(1,0,SR); A*=fade
with wave.open(SCR+'audio.wav','wb') as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((A*32767).astype(np.int16).tobytes())
# ---- video
XF=0.35; rng=random.Random(1)
for fi in range(int(20*FPS)):
    T=fi/FPS; s=min(3,int(T//SCENE)); t=T-s*SCENE
    if fi%(FPS//12)==0: seed=rng.random()
    im=caption(overlay(frame_base(s,t,random.Random(seed)),s,t),s,t)
    if s<3 and t>SCENE-XF:  # crossfade into next scene
        n=caption(overlay(frame_base(s+1,0,random.Random(seed)),s+1,0.0),s+1,0.0)
        im=Image.blend(im,n,(t-(SCENE-XF))/XF)
    ff.stdin.write(im.convert('RGB').tobytes())
ff.stdin.close(); ff.wait(); print('done',ff.returncode)

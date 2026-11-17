import sys, numpy as np, colorsys
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB'); a=np.asarray(im).astype(float)
def hx(c): return '#%02x%02x%02x'%tuple(int(round(v)) for v in c)
def reg(n,x0,y0,x1,y1):
    r=a[y0:y1,x0:x1].reshape(-1,3); print(n,hx(np.median(r,0)),hx(r.mean(0)))
reg('topbar',0,0,640,40); reg('topbar2',0,10,640,60)
reg('botbar',0,590,640,640); reg('botbar2',0,600,640,630)
reg('frame-left-dark',0,80,20,560); reg('center-dark',300,100,360,260)
L=a@[.2126,.7152,.0722]; flat=a.reshape(-1,3); l=L.ravel()
for p in (1,5,15,30,50,70,85,95,99):
    t=np.percentile(l,p); m=np.abs(l-t)<4; print('P',p,hx(np.median(flat[m],0)))
# title letters: cream pixels in title strip
t=a[35:75,130:610].reshape(-1,3); tl=t@[.2126,.7152,.0722]
m=tl>np.percentile(tl,96); print('title light',hx(np.median(t[m],0)))
# saturated reds / copper lines
hsv=np.array([colorsys.rgb_to_hsv(*(p/255)) for p in flat[::37]])
for n,(h0,h1) in {'red':(0,.03),'orange':(.03,.08)}.items():
    s=hsv[(hsv[:,0]>=h0)&(hsv[:,0]<h1)&(hsv[:,1]>.5)&(hsv[:,2]>.3)]
    print(n,len(s),hx(np.array(colorsys.hsv_to_rgb(*np.median(s,0)))*255))
# vivid brightest copper
v=np.array([colorsys.rgb_to_hsv(*(p/255)) for p in flat[::11]]); 
b=flat[::11][(v[:,1]>.35)&(v[:,2]>.75)]; print('bright copper',len(b),hx(np.median(b,0)))

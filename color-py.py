#!/usr/bin/env python3
"""Color space conversions: RGB, HSL, HSV, HEX, CMYK."""
import sys

def rgb_to_hex(r,g,b):return f"#{r:02x}{g:02x}{b:02x}"
def hex_to_rgb(h):h=h.lstrip('#');return tuple(int(h[i:i+2],16)for i in(0,2,4))
def rgb_to_hsl(r,g,b):
    r,g,b=r/255,g/255,b/255;mx,mn=max(r,g,b),min(r,g,b);d=mx-mn;l=(mx+mn)/2
    if d==0:h=s=0
    else:
        s=d/(2-mx-mn) if l>0.5 else d/(mx+mn)
        if mx==r:h=((g-b)/d)%6
        elif mx==g:h=(b-r)/d+2
        else:h=(r-g)/d+4
        h*=60
    return round(h),round(s*100),round(l*100)
def hsl_to_rgb(h,s,l):
    s,l=s/100,l/100;c=(1-abs(2*l-1))*s;x=c*(1-abs((h/60)%2-1));m=l-c/2
    if h<60:r,g,b=c,x,0
    elif h<120:r,g,b=x,c,0
    elif h<180:r,g,b=0,c,x
    elif h<240:r,g,b=0,x,c
    elif h<300:r,g,b=x,0,c
    else:r,g,b=c,0,x
    return round((r+m)*255),round((g+m)*255),round((b+m)*255)
def rgb_to_cmyk(r,g,b):
    if r==g==b==0:return 0,0,0,100
    c,m,y=1-r/255,1-g/255,1-b/255;k=min(c,m,y)
    return round((c-k)/(1-k)*100),round((m-k)/(1-k)*100),round((y-k)/(1-k)*100),round(k*100)

def main():
    if len(sys.argv)>1 and sys.argv[1]=="--test":
        assert rgb_to_hex(255,128,0)=="#ff8000"
        assert hex_to_rgb("#ff8000")==(255,128,0)
        assert rgb_to_hsl(255,0,0)==(0,100,50)
        assert hsl_to_rgb(0,100,50)==(255,0,0)
        assert hsl_to_rgb(120,100,50)==(0,255,0)
        assert rgb_to_cmyk(0,0,0)==(0,0,0,100)
        r,g,b=hsl_to_rgb(*rgb_to_hsl(100,150,200))
        assert abs(r-100)<=1 and abs(g-150)<=1 and abs(b-200)<=1
        print("All tests passed!")
    else:
        r,g,b=100,150,200;print(f"RGB({r},{g},{b}) = HEX:{rgb_to_hex(r,g,b)} HSL:{rgb_to_hsl(r,g,b)}")
if __name__=="__main__":main()

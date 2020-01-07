f="pic001 - Copy.png"
c = Image.open(f)
c = c.convert("RGBA")
w, h = c.size
cnt = -1
for px in c.getdata():
    cnt+=1
    r,g,b,a=px
    if r==255 and g==255 and b==255 and a==0:
        c.putpixel((int(cnt % w), int(cnt / w)), (255, 255, 255, 255))
    elif a!=255:
        c.putpixel((int(cnt % w), int(cnt / w)), (r+int((255-r)*(1-a/255.)), g+int((255-g)*(1-a/255.)), b+int((255-b)*(1-a/255.)), 255))
        
    
c.save("_"+f)
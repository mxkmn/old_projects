from math import *
from tkinter import *
root = Tk()

w, h = 1250, 950 #size of window (width and height)
zoom = 50 #pixels in one distance
dw, dh = 1, 0.2 #real distance between {zoom} pixels (width and height)
accuracy = 0.5 #number of checks per pixel
lineMode = False #draw line, not dots
thickness = 1 #thickness of line
halfw, halfh, f = w//2, h//2, input('Write function: y=') #other variables

canv = Canvas(root, width=w, height=h, bg="white") #new window
canv.create_line(halfw, h, halfw, 0, width=2, arrow=LAST) #vertical line
canv.create_line(0, halfh, w, halfh, width=2, arrow=LAST) #horizonlal line
tmp = max(halfw, halfh)
for i in range(-tmp//zoom, tmp//zoom+1): #draw nums every {zoom} pixels
    if i!=0:
        k = i*zoom
        if 5<k+halfw<w-5: #horizontal lines and numbers
            canv.create_line(halfw+k, halfh-3, halfw+k, halfh+3, fill='purple')
            canv.create_text(halfw+k, halfh-12, text = str(round(i*dw, 10)), fill='purple', font=('Helvectica', '10'))
        if 5<k+halfh<h-5: #vertical lines and numbers
            canv.create_line(halfw-3,  halfh+k, halfw+3, halfh+k, fill = 'purple')
            canv.create_text(halfw+20, halfh+k, text=str(round(-i*dh, 10)), fill='purple', font=('Helvectica', '10'))

lastCoordsExist, tmp = False, ceil(w*accuracy/2)
for i in range(-tmp, tmp):
    try:
        x = (i/accuracy)*(dw/zoom)
        new_f = f.replace('x', str(x))
        y = -eval(new_f)*(zoom/dh)+halfh
        x = x*(zoom/dw)+halfw
        if lineMode:
            if lastCoordsExist:
                canv.create_line(lastx, lasty, x, y, width=thickness)
            else:
                canv.create_oval(x-thickness/2, y-thickness/2, x+thickness/2, y+thickness/2)
                lastCoordsExist = True
            lastx, lasty = x, y
        else:
            canv.create_oval(x-thickness/2, y-thickness/2, x+thickness/2, y+thickness/2)
    except:
        lastCoordsExist = False

canv.pack()	
root.mainloop()

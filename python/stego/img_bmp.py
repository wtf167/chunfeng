import PIL.Image as Image

def low():
    img = Image.open("/tmp/in.bmp")
    img1 = img.copy()
    pix = img1.load()
    ww, hh = img1.size
    for w in range(ww):
        for h in range(hh):
            if pix[w,h] & 1 == 0:
                pix[w,h] = 0
            else:
                pix[w,h] = 255
    img1.save("/tmp/out.bmp")

low()

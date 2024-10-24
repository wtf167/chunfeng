from PIL import Image


def foo(fImage, x1, y1, x2, y2, x0, y0):
    w = len(range(x1, x2, x0))
    h = len(range(y1, y2, y0))
    oi = Image.open(fImage)
    ni = Image.new('RGB', (w, h))
    for x in range(w):
        for y in range(h):
            pixel = oi.getpixel((x1 + x * x0, y1 + y * y0))
            print(pixel)
            ni.putpixel((x, y), pixel)
    ni.save("/tmp/1.png")
    ni.show()


if __name__ == '__main__':
    fImage = '/tmp/a.png'
    x1, y1, x2, y2, x0, y0 = 18, 18, 2500, 2500, 25, 25
    foo(fImage, x1, y1, x2, y2, x0, y0)

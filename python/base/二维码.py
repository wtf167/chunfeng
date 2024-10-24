from PIL import Image


txt = '''
0000000001110010000000000
0000000000011110100000000
0000000001110001000000000
0000000010111100000000000
0000000010101010000000000
0000000001100010100000000
0000000010101010100000000
0000000001000001100000000
1100011101110110100011000
0001000010110010010010100
0100111101000011101110011
0011110100101011001001001
1000001001100001001101000
1111000111111011100101000
1011011111001101111110111
1000110110010010101101100
1000111100111111111110111
0000000010110001100010100
0000000010010100101010001
0000000010101010100011001
0000000000100111111110010
0000000000011001011110111
0000000001001100100100001
0000000011000011011011001
0000000011010000101110101
'''
data = txt.split("\n")[1:-1]

# 7*7的定位标志
pos = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

img = Image.new("1", (25, 25))
for i in range(len(data)):
    for j in range(len(data[1])):
        if i < 7 and j < 7:
            img.putpixel((i, j), pos[i][j] ^ 1)
        elif i > 17 and j < 7:
            img.putpixel((i, j), pos[i-18][j] ^ 1)
        elif i < 7 and j > 17:
            img.putpixel((i, j), pos[i][j-18] ^ 1)
        else:
            img.putpixel((i, j), int(data[i][j]) ^ 1)

img.resize((500, 500)).save("/Users/wuduo/Downloads/_tmp/qr.png")

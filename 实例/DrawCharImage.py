from PIL import Image
ascii_char = list('"$%_&WM#oahkbdpqwmZO0QLJUYXzcvuxrjft/\|()!{}[]?-/+@<>i!;:,\^`.')
def get_char(r,b,g,alpha=56):
    if alpha == 0:
        return ' '
    gray = int(0.2126 * r + 0.7152 * g + 0.072 * b)
    unit = 256 /len(ascii_char)
    return ascii_char[int(gray // unit)]
def main():
    im = Image.open('astro.jpg')
    WIDTH,HEIGHT = 100,60
    im = im.resize((WIDTH,HEIGHT))
    txt = ''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    fo = open('pic_char.txt','w')
    fo.write(txt)
    fo.close()
main()
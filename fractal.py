from math import cos, sin
from PIL import Image
from random import randint

minimum = 0
maximum = 255
def clamp(n, minimum, maximum):
    if n < minimum:
        return minimum 
    elif n > maximum:
        return maximum
    else:
        return n 

a_b = (13, 9)
c_d = (0.966, 0.259)
def slozhno(a_b,c_d):
    a, b = a_b
    c, d = c_d
    return (a*c-b*d, a*d+b*c)


z=(0.5,0.7)
C = (0.185, 0.6)
def terpenie_i_trud(z,c):
 for i in range(0,50):
    z = slozhno(z,z)
    z = (z[0]+c[0], c[1]+z[1])
    if z[0]**2+z[1]**2 > 4:
        return i
 return 0 



width_im = 1000
height_im = 1000
im = Image.new("RGB", (width_im,height_im ), "black")
def black(height_im, width_im):
    for x in range(width_im):
        for y in range(height_im):
            a = randint(0,255)
            b = randint(0,255)
            c = randint(0,255)
            a = (x*y)%255
            if terpenie_i_trud((x/width_im*2 - 1, y/height_im*2 - 1), C):
                im.putpixel((x,y),((a,100,300)))
black(height_im, width_im)
import time
im.save(f"img_fractal_{time.time()}_c{C[0]}_{C[1]}.jpg", "JPEG")
im.show()


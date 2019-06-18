
#	Generates a Julia set image


import numpy as np
import random

def generate_julia():
   
    print('=========================================================')

    w = int(input('Enter width of image: '))
    h = int(input('Enter height of image: '))
    f = float(input('Enter a value between 0.55 and 1 (like 0.75): '))
    name_input = input('Enter name of file to get as output: ')

    re_min = -1.5
    re_max = 1.5
    im_min = -1.5
    im_max = 1.5
    name = (str(name_input) + '.pmg')
    c = complex(0.0, f)
    real_range = np.arange(re_max, re_min, (re_min - re_max) / w)		
    image_range = np.arange(im_min, im_max, (im_max - im_min) / h)		
    # real_range = np.random.uniform(re_min, re_max, w)
    # image_range = np.random.uniform(im_min, im_max, h)
    output = open(name, 'w')
    output.write('P2\n# Julia Set image\n' + str(w) + ' ' + str(h) + '\n255\n')
    for im in image_range:
        for re in real_range:
            z = complex(re, im)
            n = 0
            while abs(z) < 10 and n < 255:
                z = z * z + c 
                n += 3
            output.write(str(n) + ' ')
        output.write('\n')
    output.close()

    print('Created photo ' + name)
    print('=========================================================')

generate_julia()


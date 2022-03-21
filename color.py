from colored import fg, bg, attr, style  # this handles the actual coloring
import random
from colormap import rgb2hex

mode = 0

main = fg('blue')
colors = []
questions = fg('green')
errors = fg('red')
print('welcome to terminal colors')
print('copyright Nathan K 2022 released under mit license')
try:
    while True:  # this chooses the input
        print('''choose input mode
	    1 rgb
	    2 hex
	    3 random''')
        while mode == 0:
            mode = str(input('mode:'))
        if mode in ['rgb', '1']:  # this gets rgb values from user then turns them to hex
                def rgb():
                    print('put RGB values here')
                    r = int(input('r'))
                    g = int(input('g'))
                    b = int(input('b'))
                    while r > 255:
                        print('value too high!')
                        r = int(input('r'))
                    while g > 255:
                        print('value too high!')
                        g = int(input('g'))

                    while b > 255:
                        print('value too high!')
                        b = int(input('b'))

                    return rgb2hex(r, g, b)

                print()
                color = rgb()

        elif mode in ['hex', '2']: # this gets hex and turns it to rgb
            h = str(input('put hex value here:'))
            if '#' in h:
                color = h
            else:
                color = '#' + h
            values = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
            print(fg('#E7BF1D') + 'r = ' + str(values[0]))  # these 3 print the rgb values of a hex code
            print('g = ' + str(values[1]))
            print('b = ' + str(values[2]))
        elif mode in ['random', '3']:  # this gets random rgb values and turns them to hex

            r = random.randint(1, 255)
            g = random.randint(1, 255)
            b = random.randint(1, 255)

            # this prints the colors hex code
            color = rgb2hex(r, g, b)

        # this prints the actual color one on its own and one next to white so you can see the difference
        print(fg('#E7BF1D') + color)
        print(fg(color) + bg('white') + '▇▇▇▇▇▇▇▇▇▇' + style.RESET)
        print(fg(color) + '▇▇▇▇▇▇▇▇▇▇' + style.RESET)

        mode = 0
except KeyboardInterrupt:
    exit()


















import math

c1 = float(input('opposite side: '))
c2 = float(input('adjacent cathetus: '))

hipo = math.hypot(c1, c2)

print('Hypotenuse = {:.2f}'.format(hipo))

#By Using Random Module
import random
# User=input('Your Name :- ')
numb = [1,2,3,4,5,6]
D = random.choice(numb)
if D == 1:
    print('[       ]')
    print('[   0   ]')
    print('[       ]')
elif D == 2:
    print('[ 0     ]')
    print('[       ]')
    print('[     0 ]')
elif D == 3:
    print('[ 0     ]')
    print('[   0   ]')
    print('[     0 ]')
elif D == 4:
    print('[ 0   0 ]')
    print('[       ]')
    print('[ 0   0 ]')
elif D == 5:
    print('[ 0   0 ]')
    print('[   0   ]')
    print('[ 0   0 ]')
elif D == 6:
    print('[ 0   0 ]')
    print('[ 0   0 ]')
    print('[ 0   0 ]')

#fuction to solve quadratic equations
def quadratic(a,b,c):
    x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    return x1,x2

#code to make a list of numbers
def make_list(start,stop,step):
    l = []
    while start <= stop:
        l.append(start)
        start += step
    return l

#code to make a list of even numbers
def make_even_list(start,stop):
    l = []
    while start <= stop:
        if start % 2 == 0:
            l.append(start)
        start += 1
    return l

#code to make a list of odd numbers
def make_odd_list(start,stop):
    l = []
    while start <= stop:
        if start % 2 != 0:
            l.append(start)
        start += 1
    return l

#code to make a list of squares
def make_square_list(start,stop):
    l = []
    while start <= stop:
        l.append(start**2)
        start += 1
    return l

#code to make a list of cubes
def make_cube_list(start,stop):
    l = []
    while start <= stop:
        l.append(start**3)
        start += 1
    return l

def main():
    print(quadratic(1,2,3))
    print(quadratic(1,2,1))
    print(quadratic(1,1,1))
    print(quadratic(1,1,2))
    print(quadratic(1,1,3))
    print(quadratic(1,1,4))
    print(quadratic(1,1,5))
    print(quadratic(1,1,6))
    print(quadratic(1,1,7))
    print(quadratic(1,1,8))
    print(quadratic(1,1,9))
    print(quadratic(1,1,10))
    print(quadratic(1,1,11))
    print(quadratic(1,1,12))
    print(quadratic(1,1,13))
    print(quadratic(1,1,14))
    print(quadratic(1,1,15))
    print(quadratic(1,1,16))
    print(quadratic(1,1,17))
    print(quadratic(1,1,18))
    print(quadratic(1,1,19))
    print(quadratic(1,1,20))
    print(quadratic(1,1,21))
    print(quadratic(1,1,22))
    print(quadratic(1,1,23))
    print(quadratic(1,1,24))
    print(quadratic(1,1,25))
    print(quadratic(1,1,26))
    print(quadratic(1,1,27))
    print(quadratic(1,1,28))
    print(quadratic(1,1,29))
    print(quadratic(1,1,30))
    print(quadratic(1,1,31))
    print(quadratic(1,1,32))
    print(quadratic(1,1,33))
    print(quadratic(1,1,34))

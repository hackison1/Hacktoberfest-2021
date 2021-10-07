name = 'vandana'
# index is from 0 to length-1
print(name[0])  # or print(name[-7]) will give same output
# index X = X-length 
# name[3] = "f" -->error will occur # we cannot change the character of string
''' slicing '''
print(name[0:3]) # here index 0, 1, 2 will be included
print(name[:4])  # this means name[0:4] so 0,1,2,3 will be included
print(name[2:])  # is same as name[2:7(i.e.length of string)] so index 2,3,4,6 will be included
''' negative index '''
print(name[-4:-1]) # this is same as name[3:6] so index 3,4,5 will be included

''' slicing with skip value '''
d = name[1:6:1]  # index 1 to 6 with skip value of 1(every 1a=st element will be included) so index 1,2,3,4,5 will be included
print(d)
print(name[1:6:2]) # so here skip value is 2(every 2nd element will be included) so index 1,3,5 will be included
print(name[1::3]) # is same as name[1:7:3] (every 3rd element will be included) so index 1, 4

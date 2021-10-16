# Bubble Sort mplementation 

def bubbleSort(array):
	s = len(array)
	for i in range(s-1):
		for j in range(0, s-i-1):
			
			if array[j] > array[j + 1] :
				array[j], array[j + 1] = array[j + 1], array[j]


array = [46, 39, 5, 2, 28, 101, 99]

bubbleSort(array)

print ("Sorted array is:")
for i in range(len(array)):
	print ("% d" % array[i]),


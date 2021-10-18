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

def bubble_sort(list1):  
    # Outer loop for traverse the entire list  
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1  

list1 = [5, 3, 8, 6, 7, 2]  
print("The unsorted list is: ", list1)  
print("The sorted list is: ", bubble_sort(list1))  

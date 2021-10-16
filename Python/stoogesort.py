#   stooge sort implement 

def stoogesort(array, k, h):
	if k >= h:
		return
	if array[k]>array[h]:
		t = array[k]
		array[k] = array[h]
		array[h] = t


	if h-k+1 > 2:
		t = (int)((h-k+1)/3)

		stoogesort(array, k, (h-t))

		stoogesort(array, k+t, (h))

		stoogesort(array, k, (h-t))


arr = [2,7, 4, 5, 3, 1,9,6,8]
n = len(arr)

stoogesort(arr, 0, n-1)

for i in range(0, n):
	print(arr[i], end = '')



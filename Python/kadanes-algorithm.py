# Kadane's Algorithm to print the maximum subarray sum
# Time Complexity : O(n)

def kadane(arr,n):
	res = 0
	s = 0
	for i in range(n):
		s = max(arr[i],s+arr[i])
		res = max(res,s)
	return res

arr = list(map(int,input().split(" ")))
res = kadane(arr,len(arr))
print("Max SubArray Sum is", res)

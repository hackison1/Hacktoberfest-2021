test_list = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]
  
# printing original list
print("The original list is : " + str(test_list))
  
# initialize K
K = 2
  
# Get Kth Column of Matrix
# using zip()
res = list(zip(*test_list)[K])
  
# printing result
print("The Kth column of matrix is : " + str(res))

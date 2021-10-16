
X = [[1,2,3],
	[6 ,5,6],
	[1 ,8,2]]

Y = [[9,8,7],
	[0,7,4],
	[3,2,1]]


result = [[0,0,0],
		[0,0,0],
		[0,0,0]]

# iterate through rows
for i in range(len(X)):
# iterate through columns
	for j in range(len(X[0])):
		result[i][j] = X[i][j] + Y[i][j]

for r in result:
	print(r)

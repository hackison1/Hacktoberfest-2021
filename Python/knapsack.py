
def knapsack(wt,value,W,n):
#     ########### recursive #############
#     if n == 0 or W == 0:
#         return 0
#     elif(wt[n-1] > W):
#         return knapsack(wt,value,W,n-1)
#     else:
#         return max(value[n-1] + knapsack(wt,value,W - wt[n-1],n-1),
#         knapsack(wt,value,W,n-1))

#     ########### memozied ###############

    # if n == 0 or W == 0:
    #     return 0
    # elif t[n][W] != -1:
    #     return t[n][W]
    # elif(wt[n-1] > W):
    #     t[n][W] = knapsack(wt,value,W,n-1)
    #     return t[n][W]
    # else:
    #     t[n][W] = max(value[n-1] + knapsack(wt,value,W - wt[n-1],n-1),
    #     knapsack(wt,value,W,n-1))
    #     return t[n][W]

#     ########### Tabulation / Bottom up ###############
#     for i in range(n+1):
#         for j in range(W+1):
#             if i == 0 or j == 0:
#                 t[i][j] = 0
#             else:
#                 if wt[i-1] > j:
#                     t[i][j] =  t[i-1][j]
#                 else:
#                     t[i][j] =  max(value[i-1]+t[i-1][j-wt[i-1]],t[i-1][j])
#     return t[n][W]
    
wt = [1,2,3,5]
value = [1,3,4,7]
W = 7
n = 4
## if using memozied uncomment next line ###
# t = [[-1 for i in range(W+1)] for j in range(n+1)]
## if using tabulation uncomment next line ##
# t = [[0 for i in range(W+1)] for j in range(n+1)]
## if using recurison no need of t ###
x = knapsack(wt,value,W,n)
print(x)
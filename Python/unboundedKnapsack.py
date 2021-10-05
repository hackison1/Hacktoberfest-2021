# Unbounded knapsack code is completely same as the 0/1 knapsack with just a small difference. In 0/1 knapsack even if the item is included or not it is marked as processed as we pass i-1/n-1 everytime but in unbounded knapsack if the item is not selected then it is considered as processed but if it is selected then it is not marked as processed but it can be used again and again without any bound.

# The only change we make is on line 13,26,39 where in the first argument to max we change 
# n-1 to n or i-1 to i


def unboundedKnapsack(wt,value,W,n):
#     ########### recursive #############
#     if n == 0 or W == 0:
#         return 0
#     elif(wt[n-1] > W):
#         return knapsack(wt,value,W,n-1)
#     else:
#         return max(value[n-1] + knapsack(wt,value,W - wt[n-1],n),
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
    #     t[n][W] = max(value[n-1] + knapsack(wt,value,W - wt[n-1],n),
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
#                     t[i][j] =  max(value[i-1]+t[i][j-wt[i-1]],t[i-1][j])
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
x = unboundedKnapsack(wt,value,W,n)
print(x)
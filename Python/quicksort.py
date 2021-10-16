def partition (a, s, e):  
    i = (s - 1)  
    pivot = a[e] 
      
    for j in range(s, e):  
     
        if (a[j] <= pivot):  
            i = i + 1  
            a[i], a[j] = a[j], a[i]  
      
    a[i+1], a[e] = a[e], a[i+1]  
  
    return (i + 1)  

def quick(a, s, end): 
    if (s < end):  
        p = partition(a, s, end) 
        quick(a, s, p - 1)  
        quick(a, p + 1, end)  
  
          
def printArr(a): 
    for i in range(len(a)):  
        print (a[i], end = " ")  
  
      
a = [68, 1003, 10, 9, 508, 121,524,138,687]  
print("Before sorting array elements are - ")  
printArr(a)  
quick(a, 0, len(a)-1)  
print("\nAfter sorting array elements are - ")  
printArr(a)  

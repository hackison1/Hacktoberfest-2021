'''
bubble search/sort by clarence yang 1/11/20 (1/3) array sorts

this code breaks down the psudocode:

the bubble sort is a sorting algorith that 'bubbles' the highest number to the end of the array after each iteration, also known as a "pass"
it heavily involves around comparing consecutive/adjacent array values and switches them if one is greater than the other, this always pushes the largest number/value to the end of the array

the numbers at the end of the array, sorted after each iteration are at the correct position, they will still be compared, which makes the algorithm inefficient, but they do not change as they are already sorted.


'''
testArray = [22, 14, 7, 25, 10, 12, 4, 18, 20] #our test array

def bubbleSort(array): #function
    passNum = 0 #our iteration number, starts at zero, a counter
    length = len(array) #length of array
    
    #checks if we have iterated enough times.
    while passNum < length: 
        '''we will iterate as many times as their are values in the array,
        this is because we will essentially have sorted one value after each 
        iteration, adding up to the total number of values in the array'''

        positionNum = 0 #position will increase while scanning the array during each iteration

        '''we check if we have compared to the end of the array, the line 
        below is a check for whether we have compared and swapped/modified the
        array entirely'''
        while positionNum < (length-passNum-1): #positionnum is like an index, arrays start with zero            
            if array[positionNum] > array[positionNum + 1]: 
                #if the given index value is greater than the next consecutive array value
                #swap places
                temp = array[positionNum]
                array[positionNum] = array[positionNum + 1]
                array[positionNum + 1] = temp    
            #increment the index, we move on to the next pair of values to compare        
            positionNum = positionNum + 1             
        #once we have compared all and pushed the highest most number to the end, 
        #we initiate another iteration. 
        passNum = passNum + 1 
        print("once pass: " + str(array)) #debug the process

    print("sorted array: " + str(array)) #sorted array

bubbleSort(testArray) #initiate the process: calls the method with the test array as the parameter. 



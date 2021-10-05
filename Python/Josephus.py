def mesuicide(arr,k):
    global index
    print("The Array",arr) 
    x = len(arr) # as the length of array changes each time

    if x == 1: # When there is only one element left in the array then it means that person is the one who is left last and will suicide

        return arr[0] # As this the last person we written the person

    else:
        y = (index+k)%x # This is a formula so that when we adding k to the index and if it is crossing the end index then it should again return to the front so that will form a circular array

        print("Person Killed at index:",y)

        arr.pop(y) # Killing the person here is simulated here by removing that person from the array

        index = y # Now the index from which we need to kill will move to the person who we killed as it will now be represented by the person after him

        me = mesuicide(arr,k) # We recursively call this condition untill the base condition is met 

    return me # Finally we return that person who is last

n = 5 # this is the given number of people
k = 2 # The number on which we have to kill the person
arr = [i for i in range(1,n+1)] # we create the list filled with number from 1 to n so we have started the range from 1 and went on till n+1

k-=1 # as we have to kill the kth person and we are already starting from a given index we reduce the k value so that it can be easily added to the index and the person can be killed.

index = 0 # the index from where we need to start killing
print(mesuicide(arr,k))

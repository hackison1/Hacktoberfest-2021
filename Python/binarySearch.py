
def binarySearch(array, x, low, high):
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


arr = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(arr, x, 0, len(arr)-1)

if result != -1:
    print("Element in index" + str(result))
else:
    print("No element found")

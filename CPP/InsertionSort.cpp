#include <iostream>

//Insertion sort function
//Arguments: pointer to array(*array) and size of array(n)
//Time Complexity(worst) : O(n^2)
//Returns the pointer to the first element in array
int *insertionSort(int *array, size_t n)
{
    //Print the inital array
    std::cout << "Initial Array: " << std::endl;
    for (int i = 0; i < n; i++)
    {
        std::cout << *(array + i) << " ";
    }
    std::cout << std::endl;

    //Insertion sort Algo
    //For loop from 1 to length of array
    for (int j = 1; j < n; j++)
    {
        int key = *(array + j);
        std::cout << "key " << key << std::endl;
        int i = j - 1;
        //While loop
        //Conditions : i shouldn't be out of bounds of array and array[i] greater than key
        //Keep on shifting elements right until end of array is reached(left end) and element is greater than key
        while (i >= 0 && *(array + i) > key)
        {
            *(array + i + 1) = *(array + i);
            i -= 1;
        }
        *(array + i + 1) = key;

        //Print the array after each pass
        std::cout << "Pass no. " << j - 1 << std::endl;
        for (int i = 0; i < n; i++)
        {
            std::cout << *(array + i) << " ";
        }
        std::cout << std::endl;
    }
    return array;
}

int main()
{
    //initialize array
    int a[] = {1231, 123123, 12, 3, 123, 21, 3, 12, 3, 24, 234, 4542, 5, 43, 55, 3, 542, 52, 53, 24, 32, 4, 123, 41, 24, 3, 52, 5, 2, 4, 24, 35412534, 5, 43, 435, 62, 45437, 787, 568, 4, 8766, 85, 6, 55, 76, 48, 6547, 46, 73, 5426, 5, 2, 53, 45, 4324, 5, 34, 264, 25, 4, 5, 2, 413, 5, 43, 156654326, 45, 76, 473, 567, 5, 8, 678, 467, 8, 247, 6, 254, 4325, 4325, 1, 3245, 134, 6, 436, 2354, 465, 36, 245, 63, 456, 54, 7, 345, 765, 426, 4, 56, 254, 654, 6, 4};

    //Calculate the length of array
    size_t n = sizeof(a) / sizeof(a[0]);

    //call insertion sort function
    int *array = insertionSort(a, n);

    return 0;
}
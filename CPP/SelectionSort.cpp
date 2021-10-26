#include <iostream>

//Function for selection sort
//Arguments: pointer to array(*array) and size of array(n)
//Time Complexity : O(n^2)
//Returns a pointer to the sorted array
int *selectionSort(int *array, size_t n)
{
    //Print the inital array
    std::cout << "Initial Array: " << std::endl;
    for (int a = 0; a < n; a++)
    {
        std::cout << array[a] << " ";
    }
    std::cout << std::endl;

    //Selection Sort Algo
    //For loop from 0 to length of array
    for (int i = 0; i < n; i++)
    {
        int min = i;

        //For loop to find the element smaller than element at ith position
        for (int j = i + 1; j < n; j++)
        {
            if (array[j] < array[min])
            {
                min = j;
            }
        }

        //Swap the elements in the minimum position and i
        int temp = array[i];
        array[i] = array[min];
        array[min] = temp;

        //Print the array after every pass
        std::cout << "Pass no : " << i << std::endl;
        for (int a = 0; a < n; a++)
        {
            std::cout << array[a] << " ";
        }
        std::cout << std::endl;
    }
    return array;
}

int main()
{
    //Initialize the array
    int array[] = {345, 5435, 34, 5, 435, 43, 5, 1, 335, 4, 3263, 1, 6254, 6, 457, 65, 37, 68, 7456, 7, 354, 66, 572, 54, 26, 254, 325, 432};

    //Calculate the length of array
    size_t n = sizeof(array) / sizeof(array[0]);

    //Call the selection sort function
    int *array2 = selectionSort(array, n);

    return 0;
}
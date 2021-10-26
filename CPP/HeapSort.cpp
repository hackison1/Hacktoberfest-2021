#include <iostream>
#include <cmath>

using namespace std;

//Utility functions
int parent(int i)
{
    return floor(i);
}
int left(int i)
{
    return 2 * i;
}
int right(int i)
{
    return (2 * i) + 1;
}

//Sorts the heap in descending order
void maxHeapify(int *array, int i, int size)
{
    int l = left(i);
    int r = right(i);
    int largest;
    for (int i = 0; i < size; i++)
    {
        cout << *(array + i) << " ";
    }
    cout << endl;
    if (l<size && *(array + l) > *(array + i))
    {
        largest = l;
    }
    else
    {
        largest = i;
    }
    if (r<size && *(array + r) > *(array + largest))
    {
        largest = r;
    }
    if (largest != i)
    {
        int temp;
        temp = *(array + i);
        *(array + i) = *(array + largest);
        *(array + largest) = temp;
        maxHeapify(array, largest, size);
    }
}

//Builds heap from array
//Time complexity(worst) : O(n)
int *buildHeapFromArray(int *array, int size)
{
    for (int i = floor(size / 2); i >= 0; i--)
    {
        maxHeapify(array, i, size);
    }
    cout << "Built heap from array" << endl;
    return array;
}

//Heap Sort function
//Arguments: pointer to array(*array) and size of array(n)
//Time Complexity(worst) : O(nlogn)
//Sorts in descending order
//Returns the pointer to the first element in sorted heap
int *heapSort(int *array, size_t n)
{
    int *a = buildHeapFromArray(array, n);
    for (int i = 0; i < n; i++)
    {
        cout << *(a + i) << " ";
    }
    cout << endl
         << "Done" << endl;
    for (int i = n - 1; i > 0; i--)
    {
        int temp;
        temp = *(a + i);
        *(a + i) = *(a + 1);
        *(a + 1) = temp;
        maxHeapify(a, 0, n);
    }
    return array;
}

int main()
{
    int array[] = {4, 1, 3, 2, 16, 9, 10, 14, 8, 7};

    int n = sizeof(array) / sizeof(array[0]);

    int *array1 = heapSort(array, sizeof(array) / sizeof(array[0]));

    for (int i = 0; i < n; i++)
    {
        std::cout << *(array1 + i) << " ";
    }
    std::cout << std::endl;

    return 0;
}
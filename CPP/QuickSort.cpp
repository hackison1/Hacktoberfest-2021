#include <iostream>

namespace sorting
{
    int partition(int arr[], int low, int high)
    {
        int pivot = arr[high];
        int i = (low - 1);

        for (int j = low; j < high; j++)
        {
            if (arr[j] <= pivot)
            {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        return (i + 1);
    }
    void quickSort(int arr[], int low, int high)
    {
        if (low < high)
        {
            int p = partition(arr, low, high);
            quickSort(arr, low, p - 1);
            quickSort(arr, p + 1, high);
        }
    }

}

int main()
{
    int arr[] = {324, 45, 34, 54645675, 8678675, 9, 869, 879, 78, 978, 59, 56, 73, 54, 25, 43, 432151, 64575};
    int size = sizeof(arr) / sizeof(arr[0]);
    sorting::quickSort(arr, 0, size);
    for (int i = 0; i < size; i++)
    {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    return 0;
}
#include <iostream>

void merge(int *array, int left, int middle, int right)
{
    int i, j, k;
    int n1 = middle - left + 1;
    int n2 = right - middle;

    int *L = new int[n1], *R = new int[n2];

    for (i = 0; i < n1; i++)
        L[i] = array[left + i];
    for (j = 0; j < n2; j++)
        R[j] = array[middle + 1 + j];

    i = 0;
    j = 0;
    k = left;
    while (i < n1 || j < n2)
    {
        if (j >= n2 || (i < n1 && L[i] <= R[j]))
        {
            array[k] = L[i];
            i++;
        }
        else
        {
            array[k] = R[j];
            j++;
        }
        k++;
    }
    std::cout << "n1 : " << n1 << " n2 : " << n2 << std::endl;
    std::cout << "Left : ";
    for (int i = 0; i < n1; i++)
    {
        std::cout << L[i] << " ";
    }
    std::cout << std::endl;
    std::cout << "Right : ";
    for (int i = 0; i < n2; i++)
    {
        std::cout << R[i] << " ";
    }
    std::cout << std::endl;
    std::cout << "Array : " << std::endl;
    for (int i = 0; i < 10; i++)
    {
        std::cout << array[i] << " ";
    }
    std::cout << std::endl
              << std::endl;

    delete[] L;
    delete[] R;
}

void mergeSort(int *array, int left, int right)
{
    if (left < right)
    {
        int middle = left + (right - left) / 2;
        mergeSort(array, left, middle);
        mergeSort(array, middle + 1, right);
        merge(array, left, middle, right);
    }
}

int main()
{
    int array[] = {234, 234, 2134, 23, 5, 245, 34, 346, 567, 76};

    size_t n = sizeof(array) / sizeof(array[0]);
    mergeSort(array, 0, n - 1);

    for (int i = 0; i < n; i++)
    {
        std::cout << *(array + i) << " ";
    }
    std::cout << std::endl;

    return 0;
}
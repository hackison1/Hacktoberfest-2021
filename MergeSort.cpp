#include <iostream>
#include <limits>
#include <vector>

void merge(int A[], int p, int q, int r)
{

	int n1 = q - p + 1 ;
	int n2 = r - q  ;

	std::vector<int>L;
	std::vector<int>R;

	for (int i = 0; i <= n1; i++)
	{
		L.push_back(0);
	}
	for (int j = 0; j <= n2; j++)
	{
		R.push_back(0);
	}


	for (int i = 0; i < n1; i++)
	{
	    L[i] = A[p + i];
	}
	for (int j = 0; j < n2; j++)
	{
		R[j] = A[q+j+1];
	}

	int i = 0;
	int j = 0;

	L[n1] = INT_MAX;
	R[n2] = INT_MAX;

	for(int k = p ; k <= r; k++)
	{
		if (L[i] <= R[j])
		{
			A[k] = L[i];
			i = i + 1;
		}
		else
		{
			A[k] = R[j];
			j = j + 1;
		}
	}
}
void MergeSort(int A[], int p, int r)
{
	if (p < r)
	{ 
		int q =(p + r) / 2;
		MergeSort(A, p, q);
		MergeSort(A, q + 1, r);
		merge(A, p, q, r);
    }
}

int main()
{
    int arr[] = {1, 2, 9, 2, 4, 5}; 
	int arrsize = sizeof(arr) / sizeof(arr[0]);
	MergeSort(arr,0,(arrsize-1));
    for (int i = 0; i < arrsize; i++)
	{
		std::cout << arr[i] << " ";
	}
}

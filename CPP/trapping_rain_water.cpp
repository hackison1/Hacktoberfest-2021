// Trapping Rain water problem
#include <bits/stdc++.h>
using namespace std;

int trappedWater(int arr[], int n)
{
	
	int lmax[n], rmax[n], ans= 0;


	lmax[0] = arr[0];

	for (int i = 1; i < n; i++)
		lmax[i] = max(lmax[i - 1], arr[i]);

    rmax[n - 1] = arr[n - 1];

	for (int i = n - 2; i >= 0; i--)
		rmax[i] = max(rmax[i + 1], arr[i]);

	for (int i = 0; i < n; i++)
		ans += min(lmax[i], rmax[i]) - arr[i];

	return ans;
}

int main()
{
	 
	int n;
    cout << "Enter the size of array: ";
    cin >> n;
    int arr[n], i;
     cout << "Enter the array elements : ";
    for(i=0;i<n;i++){
        cin >> arr[i];
    }
	cout << "Trapped rain water: " << trappedWater(arr, n);
	return 0;
}

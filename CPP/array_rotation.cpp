/*
 Problem Statement : Given an array, its lenght and k, right rotate the
                     array by k units and print the resultant array
*/

#include<bits/stdc++.h>
using namespace std;

// Function to rotate the array

void rotate(int arr[], int n, int k) {
    k %= n;
    for (int i = 0; i < n; i++) {
        if (i < k) {
            cout << arr[n + i - k] << " ";
        }
        else {
            cout << (arr[i - k]) << " ";
        }
    }
    cout << "\n";
}

// Main function

int main() {

    int n, k;
    cout << "Enter the size of the array : " << "\n";
    cin >> n;
    int arr[n];
    cout << "Enter the array elements : " << "\n";
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << "Enter the degree of rotation : " << "\n";
    cin >> k;
    cout << "The resultant array after rotation is : ";
    rotate(arr, n, k);

    return 0;
}

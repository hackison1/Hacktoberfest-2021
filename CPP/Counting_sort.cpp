#include<bits/stdc++.h>
using namespace std;
/*
Counting sort is linear time algo used when our input elements are in a small range.

Not a comparision based algo only counts the occurences of elements.

Time complexity : O(n+k) (n-number of elements, k-range of elements)

Auxillary space : O(n+k)

Stable 

Used as a subroutine in radix sort.

Used only when k (range) is small i.e n not n^2 or n^3. Otherwise we generally use radix sort algorithm.
*/
void counting_sort(int arr[],int n)
{
    int mini=*min_element(arr,arr+n);
    int maxi=*max_element(arr,arr+n);
    int k=maxi-mini+1;
    int freq[k];
    for(int i=0;i<k;i++)
    freq[i]=0;

    for(int i=0;i<n;i++)
    {
        freq[arr[i]-mini]++;
    }
    for(int i=1;i<k;i++)
    {
        freq[i]+=freq[i-1];
    }
    //Now freq[i] represent the count of all the elements smaller than or equal to i.
    int temp[n];
    for(int i=n-1;i>=0;i--)
    {
        temp[freq[arr[i]-mini]-1]=arr[i];
        freq[arr[i]-mini]--;
    }
    //We traverse fromm the right so that the sort is stable.
    for(int i=0;i<n;i++)
    {
        arr[i]=temp[i];
    }
}
void print(int arr[], int n)
{
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}
int main(){
    int arr[]={1,4,4,1,0,1};
    int size=sizeof(arr)/sizeof(int);
    print(arr,size);
    counting_sort(arr,size);
    print(arr,size);
    return 0;
}
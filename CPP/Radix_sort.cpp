#include<bits/stdc++.h>
using namespace std;
/*
Generally we use radix sort algorithm instead of using counting sort.

Linear time algo if the data is within a range.

Radix sort works in linear time even if the data is in range of n^2 or n^3.

*/
void counting_sort(int arr[],int n,int exp)
{
    int k=10;
    int freq[k];
    for(int i=0;i<k;i++)
    freq[i]=0;

    for(int i=0;i<n;i++)
    {
        freq[(arr[i]/exp)%10]++;
    }
    for(int i=1;i<k;i++)
    {
        freq[i]+=freq[i-1];
    }
    //Now freq[i] represent the count of all the elements smaller than or equal to i.
    int temp[n];
    for(int i=n-1;i>=0;i--)
    {
        temp[freq[(arr[i]/exp)%10]-1]=arr[i];
        freq[(arr[i]/exp)%10]--;
    }
    //We traverse fromm the right so that the sort is stable.
    for(int i=0;i<n;i++)
    {
        arr[i]=temp[i];
    }
}
void radix_sort(int arr[],int n)
{
    int max=*max_element(arr,arr+n);  //theta(n)
    int max_digit=floor(log10(max)+1);  
    for(int exp=1;exp<=pow(10,max_digit-1);exp*=10)   //theta(d*(n+b)) (d is the number of digits in largest numbers and b is the base we take which is 10 here)
    {
        counting_sort(arr,n,exp);   //o(n)
    }

    //Here we use 10 as base but if we increase the base the time complexity decreases as d decreases but the auxillary space requirred for counting sort increases.
    //Auxillary space : theta(n+b) where b is the base.
    //Also it stable algorithm
}
void print(int arr[], int n)
{
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}
int main(){
    int arr[]={319,212,6,8,100,50};
    int size=sizeof(arr)/sizeof(int);
    print(arr,size);
    radix_sort(arr,size);
    print(arr,size);
    return 0;
}
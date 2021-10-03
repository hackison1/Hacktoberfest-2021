
#include <stdio.h>
int i,j;
int rotLeft(int arr[],int n,int d)
{
    for(j=0;j<d;j++){
    int temp = arr[0];
    for (i = 0; i < n - 1; i++)
        arr[i] = arr[i + 1];
 
    arr[n-1] = temp;
    }
    for(i=0;i<n;i++)
        printf("%d ",arr[i]);
    return 0;
}
int rotRight(int arr[],int n,int d){
    for(j=0;j<d;j++){
        int temp=arr[n-1];
        for(i=n-1;i>0;i--){
            arr[i]=arr[i-1];
        }
        arr[0]=temp;
    }
    for(i=0;i<n;i++)
        printf("%d ",arr[i]);
    return 0;
}
int main()
{
    int n,d;
    char what;
    printf("Enter number of elements in an array: \n")
    scanf("%d",&n);
    int arr[n];
    printf("Input array elements : ");
    for(i=0;i<n;i++)
        scanf("%d",&arr[i]);
    printf("How many roratoins to perform? : ")
    scanf("%d",&d);
    printf("Rotate left or right? 'L' is for left, everything else is for right");
    scanf(" %c",&what);
    if(what=='L') rotLeft(arr,n,d);
    else rotRight(arr,n,d);
	return 0;
}
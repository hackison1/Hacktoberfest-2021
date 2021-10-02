#include<stdio.h>
#include<conio.h>
#define max 20
void main()
{
    int a[max],b[max],c[max],n1,n2,l=0;
    printf("\nenter the length of first array:");
    scanf("%d",&n1);
    printf("\nenter the data in first array:");
    for(int i=0;i<n1;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("\nenter the length of second array:");
    scanf("%d",&n2);
    printf("\nenter the data in second array:");
    for(int i=0;i<n2;i++)
    {
        scanf("%d",&b[i]);
    }
    printf("\n the concatenated array is:");
    for(int i=0;i<n1;i++)
    {
        c[l++]=a[i];
    }
    for(int i=0;i<n2;i++)
    {
        c[l++]=b[i];
    }
    l=n1+n2;
    for(int i=0; i<l;i++)
    {
        printf("%d",c[i]);
        }
}

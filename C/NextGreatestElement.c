#include<stdio.h>
#include<stdlib.h>
int main()
{
	int n;
    printf("Enter the number of elements to be stored in array: ");
    scanf("%d",&n);
    int *a=(int *)malloc(n*sizeof(int));
    printf("Enter elements into the array:\n");
    for(int i=0;i<n;i++)
    {
        scanf("%d",(a+i));
    }
	for(int i=0;i<n;i++)
	{
		int max=*(a+i);
		for(int j=i+1;j<n;j++)
		{
			if(max<*(a+j))
			{
				max=*(a+j);
				break;
			}
		}
		if(max==*(a+i))
		max=-1;
		printf("%d   %d\n",*(a+i),max);
	}
	return 0;
}
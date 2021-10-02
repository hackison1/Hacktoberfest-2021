#include<stdio.h>
int main()
{
	int i=0,a[10],element,n,flag=1;
printf("enter the number of values to be inserted");
scanf("%d",&n);
for(i=0;i<n;i++)
{
	printf("enter the value");
	scanf("%d",&a[i]);
}
printf("enter the element to be searched");
scanf("%d",&element);
for(i=0;i<n;i++)
{
	if(element==a[i])
	{
		flag=0;
		break;
	}
}
(flag)?printf("no") : printf("yes");
}

//sample o/p
//enter the number of values to be inserted8
//enter the value8
//enter the value6
//enter the value9
//enter the value2
//enter the value9
//enter the value4
//enter the value0
//enter the value2
//enter the element to be searched0
//yes

#include <stdio.h>
long addTwoNumbers(long *n1,long *n2){
    return *n1+*n2;
}
int main()
{
    long a,b;
    scanf("%ld %ld",&a,&b);
    printf("%ld",addTwoNumbers(&a,&b));
	return 0;
}
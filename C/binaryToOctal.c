#include <stdio.h>
#include <math.h>
int convertBinarytoOctal(long long binaryNumber);
int main()
{
    int a,y;
    printf("Enter the binary number : ");
    scanf("%d",&a);
    y=convertBinarytoOctal(a);
    printf("The octal equivalent is %o",y);
	return 0;
}
int convertBinarytoOctal(long long binaryNumber){
    int i=0,dec=0;
    while(binaryNumber!=0){
        dec+=(binaryNumber%10)*pow(2,i);
        ++i;
        binaryNumber/=10;
    }
    return dec;
}
#include <stdio.h>
float main(){
	float l,b,A;
	printf("Enter the length of rectangle: ");
	scanf("%f",&l);
	printf("Enter the breadth of rectangle: ");
	scanf("%f",&b);
	A = l*b;
	printf("The area of the rectangle is %f.",A);
	
	return 0;
}

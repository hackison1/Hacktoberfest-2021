#include <stdio.h>
int main() {

    int basenum, exponent;
    long double result = 1.0;

    printf("Enter the base number: ");
    scanf("%d", &basenum);
    printf("Enter the exponentonent: ");
    scanf("%d", &exponent);

    while (exponent != 0) {
        result *= basenum;
        --exponent;
    }
    printf("Power of the Number = %.0Lf", result);
    return 0;
}
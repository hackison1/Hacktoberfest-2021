#include <stdio.h>
int main() {

  char operator;
  double num1, num2;
  printf("Enter operator >>> sum (+) | substract (-) | multiply (*) | divide (/) : ");
  scanf("%c", &operator);
  
  printf("Enter two Numbers: ");
  scanf("%lf %lf", &num1, &num2);

  switch (operator) {
    case '+':
      printf("%.1lf + %.1lf = %.1lf", num1, num2, num1 + num2);
      break;
    case '-':
      printf("%.1lf - %.1lf = %.1lf", num1, num2, num1 - num2);
      break;
    case '*':
      printf("%.1lf * %.1lf = %.1lf", num1, num2, num1 * num2);
      break;
    case '/':
      printf("%.1lf / %.1lf = %.1lf", num1, num2, num1 / num2);
      break;
    default:
      printf("Wrong operator !!! Try Again.");
  }

  return 0;
}
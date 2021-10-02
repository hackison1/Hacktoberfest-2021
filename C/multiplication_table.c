#include <stdio.h>
#include <conio.h>
int main() {
  int n, i, a;
  printf("Enter an integer: ");
  scanf("%d", &n);
  printf("Enter limit: ");
  scanf("%d", &a);
  for (i = 1; i <= a; ++i) {
    printf("%d * %d = %d \n", n, i, n * i);
  }
  return 0;
}
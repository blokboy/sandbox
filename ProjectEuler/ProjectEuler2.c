#include <stdio.h>

int main(void) {
  int a = 0, b = 1, c = 1, sum = 0;

  while (c <= 4000000) {
    if (c % 2 == 0) { sum += c; }
    a = b;
    b = c;
    c = a + b;
  }

  printf("%d\n", sum);

  return sum;
}


#include <stdio.h>

int main(void) {
  int sumOfSquares = 0, sum = 0, squareOfSum = 1, j = 0;

  for (j = 0; j <= 100; ++j) {
    sumOfSquares += j * j;
    sum += j;
  }
  squareOfSum = sum * sum;

  printf("%d\n", squareOfSum - sumOfSquares);

  return (squareOfSum - sumOfSquares);
}

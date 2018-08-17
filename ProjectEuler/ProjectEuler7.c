#include <stdio.h>

#define MAXCOUNT 10001

int isPrime(int num) {
  if (num % 2 == 0)
    return 0;

  for (int i = 3; i < num; i += 2) {
    if (num % i == 0) { return 0; }
  }

  return 1;
}

int main(void) {
  unsigned int i, primeCount = 0;

  for (i = 3;; ++i) {
    if (isPrime(i)) { ++primeCount; }
    if (primeCount == MAXCOUNT - 1) { break; }
  }

  printf("%lu\n", i);

  return 0;
}

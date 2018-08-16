#include <stdio.h>

int main(void) {
  unsigned long long num = 600851475143ULL, i;

  for (i = 2ULL; i < num; i++) {
    while (num % i == 0) { num /= i; }
  }

  printf("%llu\n", num);

  return num;
}

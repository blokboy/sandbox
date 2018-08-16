#include <stdio.h>

int main(void) {
  unsigned long result, i = 0;

  for (result = 2520;; result += 2520) {
    for (i = 10; i < 20; ++i) {
      if (result % i) { break; }
    }
    if (i == 20) { break; }
  }

  printf("%lu\n", result);

  return result;
}

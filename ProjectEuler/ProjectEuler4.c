#include <stdio.h>

int isPalindrome(unsigned long num) {
  unsigned long numReverse = 0, originalNum = num;

  while (num > 0) {
    numReverse = (numReverse * 10) + (num % 10);
    num /= 10;
  }

  return(originalNum == numReverse);
}

int main(void) {
  unsigned long palindrome = 0, product;

  for (int x = 99; x < 999; ++x) {
    for (int y = 99; y < 999; ++y) {
      product = x * y;
      if (isPalindrome(product) && palindrome < product) { palindrome = product; }
    }
  }

  printf("%d\n", palindrome);

  return palindrome;
}

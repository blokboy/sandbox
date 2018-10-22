#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define SUM 1000

void calcPyTrip(float *n, float fSum);
bool chkTripSum(float *n, float fSum);
float prodTrip(float *n);
void printResults(float *n, float prod);

int a = 0, b = 1, c = 2;

int main() {
    float n[3]; // Set of three natural numbers
    float fSum = SUM;
    float product;

    printf("------------------------------\n");
    printf("Pythagorean Triplet Generator\n");
    printf("a^2 + b^2 = c^2\n");
    printf("a + b + c = %.0f\n", fSum);
    printf("------------------------------\n\n");

    calcPyTrip(n, fSum);
    product = prodTrip(n);
    printResults(n, product);

    return 0;
}

void calcPyTrip(float *n, float fSum) { // Calculate Pythagorean Triplets and store
    double tmp; // For use with modf()

    for( n[a] = 1; n[a] < fSum; n[a]++ ) {
        for( n[b] = 1; n[b] < fSum; n[b]++ ) {
            n[c] = sqrt(pow(n[a], 2) + pow(n[b], 2));
            if( modf(n[c], &tmp) == 0 ) { // Continue if c is a natural number
                if( chkTripSum(n, fSum) == 1 ) { // If the current triplet adds up to fSum
                    return;
                }
            }
        }
    }
    return;
}

bool chkTripSum(float *n, float fSum) { // Checks if the triplet adds up to fSum
    if( (n[a] + n[b] + n[c]) == fSum ){
        return true;
    } else {
        return false;
    }
}

float prodTrip(float *n) { // Return the product of the triplet
    float prod;
    prod = n[a] * n[b] * n[c];
    return prod;
}

void printResults(float *n, float prod) {
    char str;

    printf("--------------------\n");
    printf("Results\n");
    printf("--------------------\n");
    printf("a: %.0f\tb: %.0f\tc: %.0f\n", n[a], n[b], n[c]);
    printf("Sum of triplet (a + b + c): %.0f\n", n[a] + n[b] + n[c]);
    printf("Product of triplet (a*b*c): %.0f\n", n[a] * n[b] * n[c]);
    printf("\nReturn to exit program.");
    scanf("%c", &str);

    return;
}


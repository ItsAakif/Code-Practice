#include <stdio.h>

// Function to calculate the factorial of a number
unsigned long long factorial(int n) {
    if (n == 0 || n == 1) {
        return 1; // Factorial of 0 and 1 is 1
    } else {
        return n * factorial(n - 1); // Recursive call for factorial
    }
}

int main() {
    int num;
    
    // Input from the user
    printf("Enter a non-negative integer: ");
    scanf("%d", &num);
    
    if (num < 0) {
        printf("Factorial is not defined for negative numbers.\n");
    } else {
        unsigned long long result = factorial(num);
        
        // Display the result
        printf("Factorial of %d = %llu\n", num, result);
    }
    
    return 0;
}

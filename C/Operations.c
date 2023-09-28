// Menu driven program to perform different arithmetic operations by Aakif Mudel
#include <stdio.h>

int main() {
    int choice;
    float num1, num2, result;

    printf("Menu-Driven Arithmetic Operations\n");
    printf("1. Addition\n");
    printf("2. Subtraction\n");
    printf("3. Multiplication\n");
    printf("4. Division\n");
    printf("Enter your choice (1/2/3/4): ");
    
    // Read the user's choice
    scanf("%d", &choice);

    printf("Enter two numbers: ");
    
    // Read two numbers
    scanf("%f %f", &num1, &num2);

    switch (choice) {
        case 1:
            // Addition
            result = num1 + num2;
            printf("Result: %.2f\n", result);
            break;
        case 2:
            // Subtraction
            result = num1 - num2;
            printf("Result: %.2f\n", result);
            break;
        case 3:
            // Multiplication
            result = num1 * num2;
            printf("Result: %.2f\n", result);
            break;
        case 4:
            // Division with error handling for division by zero
            if (num2 != 0) {
                result = num1 / num2;
                printf("Result: %.2f\n", result);
            } else {
                printf("Error: Division by zero is not allowed.\n");
            }
            break;
        default:
            // Invalid choice
            printf("Invalid choice! Please choose a valid option (1/2/3/4).\n");
            break;
    }

    return 0;
}

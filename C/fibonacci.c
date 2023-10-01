#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>


static uint32_t fibonacci(uint32_t _n);


int main(int _argc, char** _argv) {
    if(_argc == 1) {
        printf("Please provide a number >= 0\n");
        return 1;
    }

    // convert _argv[0] to an integer to match function arg
    uint32_t n = (uint32_t) strtol(_argv[1], NULL, 10);
    printf("fib(%u) = %u\n", n, fibonacci(n));
}

static uint32_t fibonacci(uint32_t _n) {
    // early return for simple values
    if(!_n) return 0;
    if(_n == 1) return 1;

    // stores entries i-1 and i-2 for easy calculations
    uint32_t prev[2] = {1, 0};
    // result for fib(i)
    uint32_t sum = 0;

    // f(n) = f(n-1) + f(n-2)
    for(uint32_t i = 2; i < _n + 1; i++) {
        sum = prev[0] + prev[1];    // stores the sum of the last computed values
        prev[1] = *prev;            // set prev[1] to prev[0]
        prev[0] = sum;              // set prev[0] to the calculated sum
    }

    return sum;
}

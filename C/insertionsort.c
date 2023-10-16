#include <stdio.h>

int main() {
    int n, temp, key;

    printf("Give the number of elements to insert: ");
    scanf("%d", &n);

    int arr[n];
    for (int i = 0; i < n; ++i) {
        scanf("%d", &arr[i]);
    }

    puts("");

    for (int i = 1; i < n; ++i) {
        key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            --j;
        }
        arr[j + 1] = key; // Place the key in its correct position
    }

    for (int i = 0; i < n; ++i) {
        printf("%d ", arr[i]);
    }

    puts("");
}

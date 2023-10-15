def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

# Accept a list from the user
user_input = input("Enter a list of numbers separated by spaces: ")
user_list = [int(x) for x in user_input.split()]

bubble_sort(user_list)
print("Sorted array is:", user_list)

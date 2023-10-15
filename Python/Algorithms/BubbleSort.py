# Function to perform the bubble sort algorithm
def bubble_sort(arr):
    n = len(arr)
    # Loop through the entire list
    for i in range(n):
        swapped = False  # Flag to optimize the algorithm
        # Iterate through the unsorted part of the list
        for j in range(0, n-i-1):
            # If the current element is greater than the next element, swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break

# Accept a list from the user
user_input = input("Enter a list of numbers separated by spaces: ")
user_list = [int(x) for x in user_input.split()]  # Convert the input string to a list of integers
# Call the bubble_sort function to sort the list
bubble_sort(user_list)
# Print the sorted list
print("Sorted array is:", user_list)

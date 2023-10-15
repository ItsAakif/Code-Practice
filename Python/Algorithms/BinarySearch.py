# Binary search function
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Target not found in the array

# Obtain a sorted list from the user
input_str = input("Enter a sorted list of space-separated values: ")
arr = [int(x) for x in input_str.split()]

# Get the target value from the user
target = int(input("Enter the value to search for: "))

# Perform binary search
result = binary_search(arr, target)

# Check and display the result
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")

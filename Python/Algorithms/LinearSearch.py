def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1 

# Input from the user
user_input = input("Enter a list of numbers separated by spaces: ")
arr = [int(num) for num in user_input.split()]  

target = int(input("Enter the number to search for: "))

result = linear_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the list")

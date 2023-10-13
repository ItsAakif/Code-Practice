#write a program for binary search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1 
arr = [1,2,3,4,5,6,7,8,9,10]
target = 8
result = binary_search(arr, target)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
    
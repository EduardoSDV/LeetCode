def binary_search(arr, _target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == _target:
            return middle
        elif _target < arr[middle]:
           right = middle - 1
        else:
            left = middle + 1
    return -1

target = 11
test_list = [-2, 3, 4, 7, 8, 9, 11, 13]
print(binary_search(test_list, target))

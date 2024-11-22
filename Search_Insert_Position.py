# -> This problem is solved by using a binary search (Algorithms/Binary_Search_Iterative.py) , it has a twist however, when the integer isn't in the list,
#the function should return where the integer would be in the ordered list. -> This is done in line 18 and explained below.


def search_insert( nums, target: int):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2
        if target == nums[middle]:
            return middle
        elif target > nums[middle]:
            left = middle + 1
        else:
            right = middle - 1

    return left

example_list1 = [-4, -1, 3, 4, 7, 8]
example_target1 = 8
example_list2 = [-4, -1, 3, 4, 7, 8]
example_target2 = 5
print(search_insert(example_list1,example_target1))
print(search_insert(example_list2,example_target2))

'''
The reason the function returns left rather than right is related to the way binary search works and the meaning of the variables left and right when the search is complete.

Here's a detailed breakdown of why left is used:

Understanding left and right:
Initialization and Updates:

left starts at 0 and right starts at len(nums) - 1.
During the search, left and right are adjusted based on the comparisons between target and nums[middle].
Search Loop:

If target == nums[middle], you return middle because you've found the target.
If target > nums[middle], it means the target must be to the right of middle, so you set left = middle + 1.
If target < nums[middle], it means the target must be to the left of middle, so you set right = middle - 1.
Termination Condition:

The loop continues until left exceeds right.
At this point, left is the smallest index where target could be inserted while still keeping the list sorted.
right will be less than left and will point to an index before where the target should be inserted. Therefore, right does not represent a valid insertion point.
Example to Illustrate:
Suppose nums = [1, 3, 5, 6] and target = 2.

The initial values are left = 0 and right = 3.
After several iterations, left will end up at 1 and right at 0.
This is because target is greater than nums[0] but less than nums[1], so you keep adjusting left and right until left surpasses right.
At the end, left will be 1, which is the correct insertion index for target = 2.
'''

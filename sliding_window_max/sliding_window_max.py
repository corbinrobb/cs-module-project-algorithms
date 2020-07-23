'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

# Psuedocode
# define cur index as 0
# new_arr = []
# while cur + k - 1 is less than len(arr)
    # new_arr.append(max(arr[cur:cur+k]))
    # cur += 1
# return new_arr

# First Pass
# def sliding_window_max(nums, k):
#     cur = 0
#     max_array = []
#     while cur + k - 1 < len(nums):
#         max_array.append(max(nums[cur:cur+k]))
#         cur += 1
#     return max_array

# Second Pass
def sliding_window_max(nums, k):
    max_array = []
    start = 0
    end = k - 1 

    current_max = max(nums[start:k])
    max_array.append(current_max)

    while end < len(nums) - 1:
        if nums[start] == current_max:
            if nums[end + 1] > current_max:
                current_max = nums[end + 1]
            else:
                current_max = max(nums[start+1:end+2])
        elif nums[end + 1] > current_max:
            current_max = nums[end + 1]

        max_array.append(current_max)
        start += 1
        end += 1


    return max_array


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

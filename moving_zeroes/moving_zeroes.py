'''
Input: a List of integers
Returns: a List of integers
'''
# Psuedocode 
# define end index
# define current index as 0
# while cur < end
    # if arr[current] == 0
        # arr.append(arr.pop(current))
        # end -= 1
    # current += 1
# return arr

def moving_zeroes(arr):
    end = len(arr) - 1
    cur = 0
    while cur <= end:
        if arr[cur] == 0:
            arr.append(arr.pop(cur))
            end -= 1
        else:
            cur += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
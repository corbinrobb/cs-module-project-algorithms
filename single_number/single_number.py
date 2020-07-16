'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# Psuedocode 
# define new Array
# for num in arr
# if num is in new array
# remove num from new array
# else
# add num to new array
# return remaining nums in new array

# First Pass
def single_number(arr):
    new_arr = []
    for n in arr:
        if n in new_arr:
            new_arr.pop(new_arr.index(n))
        else:
            new_arr.append(n)
            
    return new_arr[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

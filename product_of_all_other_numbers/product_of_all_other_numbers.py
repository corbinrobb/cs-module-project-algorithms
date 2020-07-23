'''
Input: a List of integers
Returns: a List of integers
'''

# Psuedocode
# define new array
# for i in range(len(array))
    # define product as 1
    # for j in range(len(array))
        # if i != j
            # product *= array[j]
    # new array.append(product)
# return new array

# First pass
# def product_of_all_other_numbers(arr):
#     product_array = []
#     for i in range(len(arr)):
#         product = 1
#         for j in range(len(arr)):
#             if i != j:
#                 product *= arr[j]
#         product_array.append(product)
#     return product_array


# 2nd psuedo

# start at beginning and end:
# loop forward through array
#   store cumulative product for each number before in index in new array
# 
# loop from end to start
#   mulitply cumilutave product for each num after by the number in same index in new array
# 
# return new array

# 2nd
def product_of_all_other_numbers(arr):
    product_array = []

    before_prod = 1
    for n in range(len(arr)):
        product_array.append(before_prod)

        before_prod *= arr[n]

    after_prod = 1
    for n in range(len(arr) - 1, -1, -1):
        product_array[n] *= after_prod

        after_prod *= arr[n]

    return product_array



if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

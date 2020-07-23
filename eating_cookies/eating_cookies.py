'''
Input: an integer
Returns: an integer
'''

# Psuedo Code
# can eat one two or three cookies at a time 
# set up base cases
# if not one two or three
#   return recursive with n-3 n-2 n-1

# first
# def eating_cookies(n):
#     if n <= 1:
#        return 1
#     elif n == 2:
#         return 2
#     elif n == 3:
#         return 4
#     else:
#         return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)


# 2nd psuedo
# create memo cache
# add a check if n in memo exists and store value in memo if not

memo = {}

# second pass using memoization
def eating_cookies (n):
    if n <= 1:
       return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif n in memo:
        return memo[n]
    else:
        x = eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)
        memo[n] = x
        return x


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

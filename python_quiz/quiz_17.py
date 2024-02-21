# Python Quiz (17) 😉
# What is the output of this code and why 🤔?


def get_sum(numbers):

    total = 0 

    for number in numbers:
        if number & 1 == 0: 
            total += number 
    return total 

numbers = [0, 1, 2, 3, 4]

print(get_sum(numbers))

# Output 

# a- 10
# b- 5
# c- 6
# d- 4


# Explanation:

# The get_sum function is defined with one parameter numbers.
# Inside the function, a variable total is initialized to zero. 
# This variable will be used to accumulate the sum of even numbers in the list.
# The function then iterates over each element in the numbers list using a for loop.
# Inside the loop, it checks if the current number is even by using the bitwise AND operation (&) with 1. 
# If the result is 0, it means the number is even because in binary representation, the least significant bit (LSB) of an even number is always 0.
# If the number is even, it adds it to the total.
# After iterating through all the numbers, the function returns the total.
# The output will be 6 because the sum of even numbers (0 + 2 + 4) is 6.
# Finally, the code prints the value 6.
# So, option c- 6 is correct.






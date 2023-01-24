'''
    Highest and Lowest

    In this little assignment you are given a string of space separated numbers 
    And have to return the highest and lowest number.

    Examples: 

        high_and_low("1 2 3 4 5")  # return "5 1"
        high_and_low("1 2 -3 4 5") # return "5 -3"
        high_and_low("1 9 3 4 -5") # return "9 -5"

    Notes:

        All numbers are valid Int32, no need to validate them.
        There will always be at least one number in the input string.
        Output string must be two numbers separated by a single space, 
        And highest number is first.

    Task URI: https://www.codewars.com/kata/554b4ac871d6813a03000035

'''

def high_and_low(numbers):

    high = str(max([int(number) for number in numbers.split()]))
    low = str(min([int(number) for number in numbers.split()]))
    return f"The highest number in the lest: {high} The lowest number in the lest: {low}"
    
print(high_and_low("13 973 743 -390 -997 -757 495 169 -852 -378 827 -80 -634 866 -848"))
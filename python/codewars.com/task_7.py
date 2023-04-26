'''

    Moving Zeros To The End

    Write an algorithm that takes an array and moves all of the zeros to the end
    preserving the order of the other elements.

    Examples:

    move_zeros([1, 0, 1, 2, 0, 1, 3]) => returns [1, 1, 2, 1, 3, 0, 0]

    Task URL: https://www.codewars.com/kata/52597aa56021e91c93000cb0

'''


def move_zeros(array):
    zeros = [zero for zero in array if zero == 0]
    new_array = [number for number in array if number != 0]
    new_array.extend(zeros)
    return new_array

# Another solution


def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i != 0]
    return l+[0] * (len(arr)-len(l))


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))

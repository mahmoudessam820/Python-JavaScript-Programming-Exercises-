"""
  level of challenge 3/10
  
  Min-maxing

  - Define a function named largest_difference 
  - that takes a list of numbers as its only parameter.
  - Your function should compute and return the difference 
  - between the largest and smallest number in the list.

  For example:

  - the call largest_difference([1, 2, 3]) 
  - should return 2 because 3 - 1 is 2.

  You may assume that no numbers are smaller or larger than -100 and 100.

  Hint:

  - Split the problem up into subproblems:
  - First find the smallest number.
  - Then find the largest number.
  - Then compute their difference and return it.
  - To find the smallest number you can use the min() built-in. 
  - Alternatively you can set smallest = 100 and loop over each number in the 
    input list. Whenever you see a smaller one, set smallest to it.

"""

# My solution 

def largest_difference(numbers):
  sm_number = numbers
  la_number = numbers
  smaller = min(sm_number)
  largest = max(la_number)
  return largest - smaller

print(largest_difference([1, 2, 3, 5, 6]))

# Another soultion 

# short solution
def largest_difference(numbers):
    return max(numbers) - min(numbers)

# naive solution
def largest_difference(numbers):
  smallest = 100
  for n in numbers:
    if n < smallest:
      smallest = n

  largest = -100
  for n in numbers:
    if n > largest:
        largest = n

  difference = largest - smallest
  return difference


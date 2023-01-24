"""
  level of challenge 3/10

  Flatten a list

  - Write a function that takes a list of lists and flattens it into a one-dimensional list.
  - Name your function flatten. 
  - It should take a single parameter and return a list.

  - For example, calling:
  - flatten([[1, 2], [3, 4]])

  - Should return the list:
  - [1, 2, 3, 4]

  Hint:

  Start by defining an empty list as the result:

  result = []

  Then use a nested for loop to fill up the result.

"""

# My solution

def flatten(out_list):
    new_list = [] 
    for in_list in out_list:
        for item in in_list:
          new_list.append(item)
    return new_list
print(flatten([[1, 2], [3, 4], [5, 6], [7, 8]]))


# Another Soultion

def flatten(outer_list):
  return [
    item
    for inner_list in outer_list
    for item in inner_list
  ]

# Python Quiz (8)😉

# What is the output of this code and why 🤔?

def func():

    lst, lst2 = [7], [7]
    lst3 = lst * 2

    return lst3 == lst2.extend(lst2)

print(func())

# Output

# a. True
# b. False
# c. Error
# d. [7, 7]

# Explanation 

# lst, lst2 = [7], [7]: This line initializes two lists, lst and lst2, both containing a single element which is the integer 7. 

# This is a simultaneous assignment where lst gets assigned [7] and lst2 gets assigned [7].

# lst3 = lst * 2: This line creates a new list named lst3 by multiplying the list lst by 2. 

# This effectively duplicates the elements of lst in lst3.

# return lst3 == lst2.extend(lst2): This line has two parts:

# lst2.extend(lst2): This extends the list lst2 by appending its own elements to itself. 

# So after this operation, lst2 becomes [7, 7]. 

# It's important to note that extend() method modifies the list in-place and returns None.
# lst3 == lst2.extend(lst2): This checks if the list lst3 is equal to the result of lst2.extend(lst2). 

# Since extend() returns None, this comparison is effectively checking if lst3 is equal to None. 

# Since they are not equal, this expression evaluates to False.

# Therefore, the correct answer is: b- False
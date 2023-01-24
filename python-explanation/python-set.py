# python sets methods explanation and visualizatio

# smileys = {"😀", "🙂", "😉", "🤩", "🤩", "😇", "😍"}


# add()	Adds an element to the set

smileys = {"😀", "🙂", "😉", "🤩"}
smileys.add("😇")

# output
# {'😉', '🙂', '😀', '🤩', '😇'}



# clear() Removes all the elements from the set
smileys = {"😀", "🙂", "😉", "🤩"}
smileys.clear()

# output
# set()


# copy() Returns a copy of the set

smileys = {"😀", "🙂", "😉", "🤩"}
x = smileys.copy()

# output
# {'😀', '😉', '🙂', '🤩'}


# difference() Returns a set containing the difference between two or more sets

smileys = {"😀", "🙂", "😉", "🤩"}
emojis = {"😀", "🙂", "😉", "😍", "🤩", "😇"}
x = emojis.difference(smileys)

# output
{'😍', '😇'}


# difference_update() 
# Removes the items in this set that are also included in another, 
# specified set.
# The difference_update() method is different from the difference() method, 
# because the difference() method returns a new set
# without the unwanted items, and the difference_update() method removes 
# the unwanted items from the original set.

emojis = {"😀", "🙂", "😉", "😍", "🤩", "😇"}
smileys = {"😀", "🙂", "🤩"}
emojis.difference_update(smileys)

# output
# {'😉', '😇', '😍'}


# discard()	Remove the specified item

smileys = {"😀", "🙂", "😉", "🤩"}
smileys.discard("😉")

# output
{'😀', '🙂', '🤩'}


# intersection() Returns a set, that is the intersection of two or more sets

smileys = {"😀", "🙂", "😉", "🤩"}
emojis = {"😉", "😍", "😇"}

x = smileys.intersection(emojis)

# output
# {'😉'}


# intersection_update()	
# method removes the items that is not present in both sets (or in all sets 
# if the comparison is done between more than two sets).
# The intersection_update() method is different from the intersection() method, 
# because the intersection() method returns a new set
# without the unwanted items, and the intersection_update() 
# method removes the unwanted items from the original set.

smileys = {"😀", "🙂", "😉", "🤩", "😇"}
emojis = {"😉", "😍", "😇"}

smileys.difference_update(emojis)

# output
# {'🤩', '🙂', '😀'}


# isdisjoint()	Returns whether two sets have a intersection or not

smileys = {"😀", "🙂", "😇"}
emojis = {"😉", "😍", "🤩"}

x = smileys.isdisjoint(emojis)

# output
# True

# issubset() method returns True if all items in the set exists in the specified set, 
# otherwise it retuns False.

smileys = {"😀", "🙂", "😇"}
emojis = {"😉", "😍", "🤩"}

x = smileys.issubset(emojis)

# output
# False


# pop()	Removes an element from the set
# Note: Because the set() is unordered we cannot ensure what element will be removed.

smileys = {"😀", "🙂", "😉", "🤩", "😇"}
x = smileys.pop()

# output 1
# 🙂
# output 2
# 🤩
# output 3
# 😉


# remove()	Removes the specified element

smileys = {"😀", "🙂", "😉", "🤩", "😇"}
smileys.remove("😉")

# output
# {'😀', '🙂', '😇', '🤩'}



# symmetric_difference() 
# method returns a set that contains all items from both set, 
# but not the items that are present in both sets.
# Meaning: The returned set contains a mix of items that are not present in 
# both sets.

smileys = {"😀", "🙂", "😉", "🤩", "😇"}
emojis = {"😉", "😍", "🤩"}

x = smileys.symmetric_difference(emojis)

# output
# {'😇', '🙂', '😀', '😍'}


# symmetric_difference_update() 
# method updates the original set by removing items that are present in both 
# sets, and inserting the other items.

smileys = {"😀", "🙂", "😉", "🤩", "😇"}
emojis = {"😉", "😍", "🤩", "😇"}

smileys.symmetric_difference_update(emojis)

# output
# {'😍', '🙂', '😀'}


# union() 
# method returns a set that contains all items from the original set, 
# and all items from the specified set(s).
# Note: It will remove the same element from the original set.

smileys = {"😀", "🙂", "😇", "😉"}
emojis = {"😉", "😍", "🤩", "😇"}

x = smileys.union(emojis)

# output
# {'😇', '😉', '😀', '🙂', '😍', '🤩'}


# update()
# method updates the current set, by adding items from another set 
# (or any other iterable).

smileys = {"😀", "🙂"}
emojis = {"😉", "😍", "🤩", "😇"}

smileys.update(emojis)

# output
# {'😍', '🙂', '🤩', '😇', '😉', '😀'}
# python list explanation and visualization 

# symbols = ['🔵', '🟨', '🔺', '🔶']


#append()	Adds an element at the end of the list

symbols = ['🔵', '🟨', '🟨']
symbols.append('🔺')

# output 
# ['🔵', '🟨', '🟨', '🔺']



# extend()	Add the elements of a list (or any iterable), to the end of the current list

symbols = ['🔵', '🟨', '🟨'] 
add_forms = ['🔺', '🔶']
symbols.extend(add_forms)

# output
# ['🔵', '🟨', '🟨', '🔺', '🔶']



# insert()	Adds an element at the specified position

symbols = ['🔵', '🟨', '🟨'] 
symbols.insert(0,  '🔺')

# output
# ['🔺', '🔵', '🟨', '🟨']


# remove()	Removes the first item with the specified value
symbols =  ['🔵', '🟨', '🟨', '🔺', '🔶']
symbols.remove('🟨')

# output
# ['🔵', '🟨', '🔺', '🔶']


# pop()	Removes the element at the specified position

symbols =  ['🔵', '🟨', '🟨', '🔺', '🔶']
symbols.pop(0)

# output
# ['🟨', '🟨', '🔺', '🔶']


# clear()	Removes all the elements from the list
symbols =  ['🔵', '🟨', '🟨', '🔺', '🔶']
symbols.clear()

# output
# []


# sort()	Sorts the list
symbols =  ['🔵', '🟨', '🔺', '🔶']
symbols.sort()

# output
# ['🔵', '🔶', '🔺', '🟨']


# reverse()	Reverses the order of the list
symbols =  ['🔵', '🟨', '🔺', '🔶']
symbols.reverse()

#output 
# ['🔶', '🔺', '🟨', '🔵']


# index()	Returns the index of the first element with the specified value
symbols =  ['🔵', '🟨', '🔺', '🔶']
x = symbols.index('🔶')

# output
# 3


# count()	Returns the number of elements with the specified value
symbols =  ['🔵', '🟨', '🟨', '🔺', '🔶']
x = symbols.count('🟨')

# output
# 2


# copy()	Returns a copy of the list
symbols =  ['🔵', '🟨', '🟨', '🔺', '🔶', '🔶']
x = symbols.copy()

# output
# ['🔵', '🟨', '🟨', '🔺', '🔶', '🔶']
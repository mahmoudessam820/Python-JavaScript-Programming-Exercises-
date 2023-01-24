# python dictionary methods explanation and visualization 

# fruits = {
#     "grape":"🍇",
#     "Watermelon":"🍉",
#     "banana":"🍌",
#     "mango":"🥭",
#     "apple":"🍎",
# }


# get()	Returns the value of the specified key

fruits = {'grape': '🍇', 'Watermelon': '🍉', 'banana': '🍌', 'mango': '🥭', 'apple': '🍎'}

x = fruits.get("mango")

# output
# 🥭


# clear() Removes all the elements from the dictionary

fruits = {'grape': '🍇', 'Watermelon': '🍉', 'banana': '🍌', 'mango': '🥭', 'apple': '🍎'}
fruits.clear()

# output
# {}


# copy() Returns a copy of the dictionary

fruits = {'grape': '🍇', 'Watermelon': '🍉', 'banana': '🍌', 'mango': '🥭', 'apple': '🍎'}

x = fruits.copy()

# output
# {'grape': '🍇', 'Watermelon': '🍉', 'banana': '🍌', 'mango': '🥭', 'apple': '🍎'}


# keys() Returns a list containing the dictionary's keys

fruits = {'grape': '🍇', 'Watermelon': '🍉', 'banana': '🍌', 'mango': '🥭', 'apple': '🍎'}

x = fruits.keys()

# output
# dict_keys(['grape', 'Watermelon', 'banana', 'mango', 'apple'])


# update() Updates the dictionary with the specified key-value pairs

fruits = {'grape': '🍇', 'Watermelon': '🍉', 'banana': '🍌', 'mango': '🥭', 'apple': '🍎'}
fruits.update({"strawberry":"🍓"})


# output
# {'grape': '🍇', 'Watermelon': '🍉', 'banana': '🍌', 'mango': '🥭', 'apple': '🍎', 'strawberry': '🍓' }


# values() Returns a list of all the values in the dictionary

fruits = {'grape': '🍇', 'Watermelon': '🍉', 'banana': '🍌', 'mango': '🥭', 'apple': '🍎'}
x = fruits.values()

# output
# dict_values(['🍇', '🍉', '🍌', '🥭', '🍎'])


# pop()	Removes the element with the specified key

fruits = {'grape': '🍇', 'Watermelon': '🍉', 'banana': '🍌', 'mango': '🥭', 'apple': '🍎'}
fruits.pop('Watermelon')

# output
# {'grape': '🍇', 'banana': '🍌', 'mango': '🥭', 'apple': '🍎'}


# items() Returns a list containing a tuple for each key value pair

fruits = {'grape': '🍇', 'Watermelon': '🍉', 'banana': '🍌', 'mango': '🥭', 'apple': '🍎'}
x = fruits.items()

# output
# dict_items([('grape', '🍇'), ('Watermelon', '🍉'), ('banana', '🍌'), ('mango', '🥭'), ('apple', '🍎' )])


# fromkeys() Returns a dictionary with the specified keys and value

x = ['grape1', 'grape2', 'grape3']
y = '🍇'

fruits = dict.fromkeys(x, y)

# output
# {'grape1': '🍇', 'grape2': '🍇', 'grape3': '🍇'}


# popitem()	Removes the last inserted key-value pair

fruits = {'grape': '🍇', 'Watermelon': '🍉', 'banana': '🍌', 'mango': '🥭', 'apple': '🍎'}
fruits.popitem()

# output
# {'grape': '🍇', 'Watermelon': '🍉', 'banana': '🍌', 'mango': '🥭'}


# setdefault() Returns the value of the specified key. 
# If the key does not exist: insert the key, with the specified value.

fruits = {'grape': '🍇', 'Watermelon': '🍉', 'banana': '🍌', 'mango': '🥭', 'apple': '🍎'}

x = fruits.setdefault("grape", None)

# output
# {'grape': '🍇', 'Watermelon': '🍉', 'banana': '🍌', 'mango': '🥭', 'apple': '🍎'}
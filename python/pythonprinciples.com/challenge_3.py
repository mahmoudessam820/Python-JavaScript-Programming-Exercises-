"""
    level of challenge = 2/10

    Online status
    
    The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

    For example, consider the following dictionary:

    statuses = {
        "Alice": "online",
        "Bob": "offline",
        "Eve": "online",
    }

    In this case, the number of people online is 2.
    Write a function named online_count that takes one parameter. 
    The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
    Your function should return the number of people who are online.

    Hint 

    Use a for loop to iterate over the .items() in the dictionary. 
    Keep track of a count variable that you increase anytime you see a person with a status of "online".

"""

# My solution 

statuses = {
    "Tito": "offline",
    "Amr": "online",
    "s7s": "offline",
    "Hussin": "online",
}

def online_count(people_status):
    count = 0
    for key in people_status:
        if people_status[key] == 'online':
            count += 1
    return count
print(online_count(statuses))



# Another solution

# long version
def online_count(people):
    count = 0
    for person, status in people.items():
        if status == "online":
            count += 1
    return count

# short version
def online_count(people):
    return len([p for p in people if people[p] == "online"])
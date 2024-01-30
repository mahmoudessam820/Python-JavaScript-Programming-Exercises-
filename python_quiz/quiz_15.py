# Python Quiz (15) 😉

# What is the output of this code and why 🤔?


print("python" > "Python" > "PYTHON")


# Output

# a- False
# b- True
# c- Error
# d- python


# Explanation:

# The code print("python" > "Python" > "PYTHON") compares the strings "python", "Python", and "PYTHON" using the greater than operator ">".
# When comparing strings using the greater than operator, Python compares them lexicographically based on their ASCII values.
# In ASCII, uppercase letters come before lowercase letters.
# Therefore, when comparing "python" and "Python", the lowercase "p" has a higher ASCII value than the uppercase "P", resulting in the comparison being True.
# Next, the code compares "Python" and "PYTHON".
# As mentioned before, the comparison is based on ASCII values, and in this case, both strings have the same characters.
# However, the lowercase "p" has a higher ASCII value than the uppercase "Y", so the comparison is True.
# Finally, the code compares the result of the first comparison ("python" > "Python") with the result of the second comparison ("Python" > "PYTHON").
# Both comparisons resulted in True, so the final result is also True.
# Therefore, the correct output of the code is True.
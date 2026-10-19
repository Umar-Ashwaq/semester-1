# Week 4, Session 1

# You are given the function mystery_func. 
# Inspect the code in the function
# Your task is to write a corresponding docstring
# - what the function does 
# - what is the input data and type
# - what is the return value and type


# function implementation

def mystery_func(string):
    upper = 0
    lower = 0
    """The upper and lower case charecter count is set to 0 initially"""
    for ch in string:
        if ch.isupper():
            upper += 1
        if ch.islower():
            lower += 1
    """Created a for loop to fliter out upper case from lower case
        Each time the for loop runs and if it finds a lower or upper case, it does +1 to the corresponding vaiable."""
    return (upper, lower)


# testing

print(mystery_func("abc"))
print(mystery_func("The quick Brown Fox!"))
print(mystery_func("012345"))
print(mystery_func("ABC"))


# Can you predict the output of the following lines of code?
# Uncomment the lines of code one by one and run the program
# to see if you are right?

# print(mystery_func("X"))
# print(mystery_func("[2, 3]"))

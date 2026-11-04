# Week 4, Session 2: Task 1

# Write a function format_date that takes 4 arguments: day, month,
# year, separator. The separator is an optional argument with a default
# value to be "-". The function returns the formatted date as a string
# in the format day-month-year with the default separator.



# complete your code here

def format_date(date, month, year, separator="-"):
    return f"{date}{separator}{month}{separator}{year}"

# Write code to test the function with separators such as "/", ":", "."
print(format_date("20","9","2009"))
print(format_date("20","9","2009","/"))
print(format_date("20","9","2009",":"))
print(format_date("20","9","2009","."))
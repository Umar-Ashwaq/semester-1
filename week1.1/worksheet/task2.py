"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")
print()

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
try:
    amount = int(input(f"Enter the amount you wnat to save every month {name}: "))
    print(f"Cool, £{amount} amount every month...")
except:
    print("Invalid amount")

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
savings = 12*amount
print(f"By the end of the year, you will be saving: {savings}")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).
savings_with_interest = (0.8/100)*savings + savings
print(f"And with interest..... You will be saving {savings_with_interest:.2f}")
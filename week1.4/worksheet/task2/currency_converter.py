
"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name: Umar Mohammad
"""

def currency_converter(amount, from_currency, to_currency):

    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }

    # your code here
    if amount < 0:
        return 0.0
    else:
        if from_currency == 'GBP':
            if to_currency == 'CNY':
                converted_amount = amount*conversion_rate['GBP']['CNY']
                rounded_amount = round(converted_amount, 2)
                print(f"The converted amount is {rounded_amount}")
            elif to_currency == 'PHP':
                converted_amount = amount*conversion_rate['GBP']['PHP']
                rounded_amount = round(converted_amount, 2)
                print(f"The converted amount is {rounded_amount}")
            elif to_currency == 'INR':
                converted_amount = amount*conversion_rate['GBP']['INR']
                rounded_amount = round(converted_amount, 2)
                print(f"The converted amount is {rounded_amount}")
        if from_currency == 'CNY':
            if to_currency == 'GBP':
                converted_amount = amount*conversion_rate['CNY']['GBP']
                rounded_amount = round(converted_amount, 2)
                print(f"The converted amount is {rounded_amount}")
            elif to_currency == 'PHP':
                converted_amount = amount*conversion_rate['CNY']['PHP']
                rounded_amount = round(converted_amount, 2)
                print(f"The converted amount is {rounded_amount}")
            elif to_currency == 'INR':
                converted_amount = amount*conversion_rate['CNY']['INR']
                rounded_amount = round(converted_amount, 2)
                print(f"The converted amount is {rounded_amount}")
        if from_currency == 'PHP':
            if to_currency == 'CNY':
                converted_amount = amount*conversion_rate['PHP']['CNY']
                rounded_amount = round(converted_amount, 2)
                print(f"The converted amount is {rounded_amount}")
            elif to_currency == 'GBP':
                converted_amount = amount*conversion_rate['PHP']['GBP']
                print(f"The converted amount is {converted_amount}")
            elif to_currency == 'INR':
                converted_amount = amount*conversion_rate['PHP']['INR']
                print(f"The converted amount is {converted_amount}")
        if from_currency == 'INR':
            if to_currency == 'CNY':
                converted_amount = amount*conversion_rate['INR']['CNY']
                rounded_amount = round(converted_amount, 2)
                print(f"The converted amount is {rounded_amount}")
            elif to_currency == 'GBP':
                converted_amount = amount*conversion_rate['INR']['GBP']
                rounded_amount = round(converted_amount, 2)
                print(f"The converted amount is {rounded_amount}")
            elif to_currency == 'PHP':
                converted_amount = amount*conversion_rate['INR']['PHP']
                rounded_amount = round(converted_amount, 2)
                print(f"The converted amount is {rounded_amount}")
    
    return None
amount_input = float(input("Enter the amount you want to convert: "))
from_currency = input("Enter the code of currency you want to convert from: ")
to_currency = input("Enter the code of currency you want to convert to: ")
currency_converter(amount_input,from_currency,to_currency)
# Submit only this file currency_converter.py with the completed function.

# Remove any additional code you may have added during development and testing.

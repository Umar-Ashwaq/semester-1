# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

try:
     numbers = read_numbers()
     print(numbers)
     print()
     Maximum = max(numbers)
     Minimum = min(numbers)
     mean = sum(numbers)/len(numbers)
     median = numbers.sort() # I need to find median fully
     print(f"Maximum = {Maximum}")
     print(f"Minimum = {Minimum}")
     print(f"Mean = {mean}")
     print(f"Median = {numbers}")
except:
     sys.exit("Error: no numbers provided")
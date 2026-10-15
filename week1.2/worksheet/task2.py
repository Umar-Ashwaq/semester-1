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
     sort = numbers.sort()
     if len(numbers)% 2 == 1:
          median = numbers[len(numbers) // 2]
     else:
          median = (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
     print(f"Maximum = {Maximum}")
     print(f"Minimum = {Minimum}")
     print(f"Mean = {mean}")
     print(f"Median = {median}")
except:
     sys.exit("Error: no numbers provided")
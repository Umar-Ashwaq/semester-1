"""Advanced Task 2: Budget Breakdown
- Ask for three separate expense amounts (for example: travel, food, accommodation).
- Convert each input so you can add them together to get a total trip cost.
- Calculate the average spend per category and show each value with an f-string.
- Extension: format the totals so they always show two decimal places.
"""

travel_cost_input = float(input("Travel cost in pounds: "))
food_cost_input = float(input("Food cost in pounds: "))
accommodation_cost_input = float(input("Accommodation cost in pounds: "))

total_cost_of_trip = travel_cost_input + food_cost_input + accommodation_cost_input
avg_cost_of_spending = total_cost_of_trip / 3

print(f"The cost of Traveling is {travel_cost_input}, cost of foot is {food_cost_input}, and cost of accommodation {accommodation_cost_input}")
print(f"The total cost of trip is {total_cost_of_trip}")
print(f"The average spending is {avg_cost_of_spending:.2f}")

# TODO: convert each value to a number type that supports decimals
# TODO: calculate the total and the average spend per category
# TODO: print the three costs, the total, and the average
# Extension: format the totals to two decimal places

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#weekday = [x for x in days if x != 'Saturday' or x != 'Sunday'] # Not working
weekday = [x for x in days if x != 'Saturday' and x != 'Sunday'] # Working
print(weekday)
# Week 1.5, Session 1: Task 4
import geometry

# Copy Point class definition here
p = geometry.Point(2.0,4.5)

    
# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle
C = geometry.Circle(3,p)
print(C.area())
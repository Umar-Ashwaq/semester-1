# Week 1.5, Session 1: Task 3
import math
class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here

    def __init__(self,x,y):
        self.x = x
        self.y = y
    # Add distance() method here
    def distance(self):
        return math.hypot(self.x,self.y)
    # Add distance_to() method here
    def distance_to(self,p):
        return math.hypot(self.x-p.x,self.y-p.y)
    # (This will need a parameter representing another point)
p = Point(1.0,2.0)
print(p.x,p.y)
print(p.distance())

q = Point(4,5)
print(p.distance_to(q))
# Finally, add code here to demonstrate use of Point

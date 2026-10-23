"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
state_time = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"
for i in range(maxtime+1):
    
    if state_time < states["red"]:
        state = "red"
    elif state_time < states["red"]+states["red_amber"]:
        state = "red_amber"
    elif state_time < states["red"]+states["red_amber"]+states["green"]:
        state  = "green"
    else:
        state = "amber"
    print(f"Time {systime:03} State {state}")
    state_time += 1
    systime += 1
    if state_time == 15:
        state_time = 0
# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14
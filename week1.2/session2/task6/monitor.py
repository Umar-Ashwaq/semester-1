# Week 1.2, Session 2: Task 6
temperature = int(input("Enter the Temperature of Machine: "))
pressure = int(input("Enter the Pressure of Machine: "))
operational_status = int(input("Enter Machine's Operational Status (1 for operating, 0 for stopped): "))

# Temperature
if temperature > 80:
    print("!! The temperature is too high, Recommending to Shutdown !!")
elif 50 < temperature < 80:
    print("The temperature is within safe limits.")
else:
    print("The machine temperature is low and no action is needed.")

# Pressure
if pressure > 100:
    print("!! High Pressure is detected and recommending maintenance !!")
elif 70 < pressure < 100:
    print("Pressure is Stable.")
else:
    print("The pressure is low and the system is operating normally.")

# Operating Status
if operational_status == 1:
    if temperature > 80 or pressure > 100:
        print("!! The machine is running in unsafe conditions and recommending it shutdown !!")
    else:
        print("The machine is running normally")
else:
    print("The machine is stopped, no immediate action is needed.")
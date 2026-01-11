System = True
Wind = True

def Heater():
    global Wind
    Wind = False
    return Wind

while System:
    user_input = input("Turn on heater? (YES or NO): ")

    if user_input == "YES":
        Wind = Heater()
        print("Heater is ON")
    else:
        Off_Wind = Heater()
        print("Heater is OFF")

#Converting km and hr into kmh

try:
    kmh = int(input("Enter km/h: "))
    mph = 0.6214*kmh
    print("Speed:", kmh, "KM/H=", mph,"MPH")

except:
    print("The given input is incorrect")
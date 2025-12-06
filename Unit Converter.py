# Unit Converter

import time

print("\nWelcome to my Unit Converter Program!")
print("\nPlease select one of the options below:\n")

print("1. Weight")
print("2. Distance")
print("3. Temperature")
print("4. Time")
print("5. Quit (Q)")

option = input("\nWhich unit conversion would you like me to do (1-4), or Quit (5)? ").lower()

if option == "1" or option == "weight":
    print("\nUnits:\n")
    print("1. Kilograms (kg)")
    print("2. Grams (g)")
    print("3. Pounds (lbs)")
    print("4. Ounces (oz)")

    units = {"1": "kg", "2": "g", "3": "lbs", "4": "oz"}

    unit1 = input("\nConvert from (1-4): ")
    unit2 = input("\nConvert to (1-4): ")
    value = float(input(f"\nEnter the weight in {units[unit1]}: "))

    to_unit = {
        "kg": 1,
        "g": 0.001,
        "lbs": 0.453592,
        "oz": 0.0283495
    }

    weight_value = value * to_unit[units[unit1]]

    from_unit = {
    "kg": 1,
    "g": 1000,
    "lbs": 2.20462,
    "oz": 35.274
    }

    result = round(weight_value * from_unit[units[unit2]], 2)

    print(f"\n{value} {units[unit1]} = {result} {units[unit2]}\n")

elif option == "2" or option == "distance":
    print("\nUnits:\n")
    print("1. Kilometres (km)")
    print("2. Metres (m)")
    print("3. Miles (mi")
    print("4. Centimetres (cm)")
    print("5. Inches (in)")
    print("6. Feet (ft)")
    print("7. Yards (yd)")
    print("8. Millimitres (mm)")

    units = {"1": "km", "2": "m", "3": "mi", "4": "cm", "5": "in", "6": "ft", "7": "yd", "8": "mm"}

    unit1 = input("\nConvert from (1-8): ")
    unit2 = input("\nConvert to (1-8): ")
    value = float(input(f"\nEnter the distance in {units[unit1]}: "))

    to_unit = {
        "km": 1000,
        "m": 1,
        "mi": 1609.34,
        "cm": 0.01,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mm": 0.001
    }

    distance_value = value * to_unit[units[unit1]]

    from_unit = {
        "km": 0.001,
        "m": 1,
        "mi": 0.000621371,
        "cm": 100,
        "in": 39.3701,
        "ft": 3.28084,
        "yd": 1.09361,
        "mm": 1000
    }

    result = round(distance_value * from_unit[units[unit2]], 2)

    print(f"\n{value} {units[unit1]} = {result} {units[unit2]}\n")

elif option == "3" or option == "temperature":
    print("\nUnits:\n")
    print("1. Celsius (C)")
    print("2. Fahrenheit (F)")
    print("3. Kelvin (K)")

    units = {"1": "C", "2": "F", "3": "K"}

    unit1 = input("\nConvert from (1-3): ")
    unit2 = input("\nConvert to (1-3): ")
    value = float(input(f"\nEnter the temperature in {units[unit1]}: "))

    if units[unit1] == "C":
        if units[unit2] == "F":
            result = round((value * 9/5) + 32, 2)
        elif units[unit2] == "K":
            result = round(value + 273.15, 2)
        else:
            result = round(value, 2)

    elif units[unit1] == "F":
        if units[unit2] == "C":
            result = round((value - 32) * 5/9, 2)
        elif units[unit2] == "K":
            result = round((value - 32) * 5/9 + 273.15, 2)
        else:  # F → F
            result = round(value, 2)

    elif units[unit1] == "K":
        if units[unit2] == "C":
            result = round(value - 273.15, 2)
        elif units[unit2] == "F":
            result = round((value - 273.15) * 9/5 + 32, 2)
        else:  # K → K
            result = round(value, 2)

    print(f"\n{value} {units[unit1]} = {result} {units[unit2]}\n")

elif option == "4" or option == "time":
    print("\nUnits:\n")
    print("1. Hours (h)")
    print("2. Minutes (min)")
    print("3. Seconds (sec)")
    print("4. Days (d)")
    print("5. Weeks (w)")
    print("6. Months (m)")
    print("7. Years (y)")

    units = {"1": "h", "2": "min", "3": "sec", "4": "d", "5": "w", "6": "m", "7": "y"}

    unit1 = input("\nConvert from (1-4): ")
    unit2 = input("\nConvert to (1-4): ")
    value = float(input(f"\nEnter the time in {units[unit1]}: "))

    to_unit = {
        "s": 1,
        "min": 60,
        "h": 3600,
        "d": 86400,
        "w": 604800,
        "mo": 2592000,
        "y": 31536000 
    }

    time_value = value * to_unit[units[unit1]]

    from_unit = {
        "s": 1,
        "min": 1/60,
        "h": 1/3600,
        "d": 1/86400,
        "w": 1/604800,
        "mo": 1/2592000,
        "y": 1/31536000
    }

    result = round(time_value * from_unit[units[unit2]], 2)

    print(f"\n{value} {units[unit1]} = {result} {units[unit2]}\n")

elif option == "5" or option == "q" or option == "quit":
    print("\nThe program will end in:")
    print("\n3...")
    time.sleep(1)
    print("\n2...")
    time.sleep(1)
    print("\n1...")
    time.sleep(1)    
    print("\nThanks for using my Unit Conversion Program!\n")
    quit()

else:
    print("\nPlease select a valid option next time, this program will end in:")
    print("\n3...")
    time.sleep(1)
    print("\n2...")
    time.sleep(1)
    print("\n1...")
    time.sleep(1)    
    print("\nThanks for using my calculator! Goodbye!\n")
    quit()


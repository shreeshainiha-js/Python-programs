def washing_machine_time(weight, water_level):
    # Check for invalid inputs
    if weight < 0:
        return "INVALID INPUT"
    elif weight > 7000:
        return "OVERLOADED"

    # Determine the time based on weight and water level
    if weight == 0:
        return "Time Estimated: 0 Minutes"
    elif weight <= 2000 and water_level.upper() == 'L':
        return "Time Estimated: 25 Minutes"
    elif 2001 <= weight <= 4000 and water_level.upper() == 'M':
        return "Time Estimated: 35 Minutes"
    elif weight > 4000 and water_level.upper() == 'H':
        return "Time Estimated: 45 Minutes"
    else:
        return "INVALID INPUT"

weight = int(input("Enter the weight of clothes (in grams): "))
water_level = input("Enter the water level (L/M/H): ")
print(washing_machine_time(weight, water_level))

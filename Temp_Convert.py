print("*"*40)
print("Temperature Converter")
print("Enter the temperature value and unit (C for Celsius, F for Fahrenheit):")
print("*"*40)
def Temp(value, unit):
    if unit.upper() == "C":
        fahrenheit = (value * 9/5) + 32  
        kelvin = value + 273.15
        print(f"{value}°C is equal to {fahrenheit}°F and {kelvin}K.")
    elif unit.upper() == "F":
        celsius = (value - 32) * 5/9
        kelvin = celsius + 273.15
        print(f"{value}°F is equal to {celsius}°C and {kelvin}K.")
    else:
        print("Invalid unit. ")
try:
    value = float(input("Enter the temperature value:\n "))
    unit = input("Enter the unit (C/F): \n")
    Temp(value, unit)
except ValueError:
    print("Invalid input.")
    print("*"*40)
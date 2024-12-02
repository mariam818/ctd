x = input("1: to convert from celsius to fahrenheit 2: to convert from fahrenheit to celsius: ")

if x == "1":
    c = float(input("Enter temperature in Celsius: "))
    print("Temperature in Fahrenheit: " +str((c * 1.8) + 32))
elif x == "2":
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Temperature in Celsius: " +str((f - 32) * 0.5556))
else:
    print("Invalid input")



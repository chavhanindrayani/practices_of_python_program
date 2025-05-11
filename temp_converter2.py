from temp_converter import celsius_to_fahrenheit

celsius = float(input(" Enter the temperature in Celsius : "))

fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius} c is equal to {fahrenheit} F")

if celsius <=15:
    print("it is cold")
elif celsius >=30:
    print("it is hot")
else:
    print("the temperature is moderate")
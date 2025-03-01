# Python weight converter

weight= float(input("Enter your weight:  "))
unit = input("Kilograms or Pounds? (K or L) : ")

if unit== "K":
    weight= weight * 2.205
    unit="Lbs"
    print(f"Your weight  is round{weight, 1} {unit}")
elif unit== "Lbs":
    weight= weight / 2.205
    unit="Kilograms"
    print(f"Your weight  is round{weight, 1} {unit}")
else:
    print(f"{unit} was not a valid measurement")



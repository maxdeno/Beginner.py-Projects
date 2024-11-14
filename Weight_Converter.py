# Weight converter program
# converts weight in kilograms to weight in pounds and viceverse.

weight = int(input("weight:"))
unit = input("L(bs) or K(kgs):")

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")

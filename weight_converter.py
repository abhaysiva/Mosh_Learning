weight=int(input("Enter your weight:"))
unit =input("Enter the unit (kg(k) or lbs(l)):")

if unit.upper()=="K":
    converter=weight/0.45
    print("weight in Lbs:",converter)
else:
    converter=weight*0.45
    print("weight in Kg:",converter)
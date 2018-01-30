while True:
    print("This program calculates miles per gallon.")
    milesDriven = float(input("Miles driven: "))
    gallonsUsed = float(input("Gallons used: "))
    mpg = milesDriven/gallonsUsed
    print("Miles per gallon:", mpg, "miles")
    user_input= input("Would you like to perform a new calculation? Y/N: ")
    if user_input== "Y" or user_input== "y":
                      continue
    else:
        break

while True:
    print("This program calculates the area of a rectangle.")
    length = float(input("Length: "))
    width = float(input("Width: "))
    area_of_rectangle = length*width
    print("The Area of the Rectangle is:", area_of_rectangle)
    user_input= input("Would you like to calculate the area of a new rectangle? Y/N: ")
    if user_input== "Y" or user_input== "y":
                      continue
    else:
        break

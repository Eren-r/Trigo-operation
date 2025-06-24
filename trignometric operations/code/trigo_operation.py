# terminal command : pip install numpy

import numpy as np

while True:
    a = input("Which operation do you want to perform:\n"
              " 1. sin(x)\n 2. cos(x)\n 3. tan(x)\n 4. sec(x)\n"
              " 5. cosec(x)\n 6. cot(x)\n 7. log\n 8. Exit\n\nOption: ")

    if a == "1":
        x = float(input("You chose sin(x). Enter value of x (in radians): "))
        print(f"sin({x}) = {np.sin(x)}\n")

    elif a == "2":
        x = float(input("You chose cos(x). Enter value of x (in radians): "))
        print(f"cos({x}) = {np.cos(x)}\n")

    elif a == "3":
        x = float(input("You chose tan(x). Enter value of x (in radians): "))
        try:
            print(f"tan({x}) = {np.tan(x)}\n")
        except Exception as e:
            print(f"Error: {e}\n")

    elif a == "4":
        x = float(input("You chose sec(x). Enter value of x (in radians): "))
        cos_x = np.cos(x)
        if cos_x != 0:
            print(f"sec({x}) = {1/cos_x}\n")
        else:
            print("Error: sec(x) undefined for cos(x) = 0\n")

    elif a == "5":
        x = float(input("You chose cosec(x). Enter value of x (in radians): "))
        sin_x = np.sin(x)
        if sin_x != 0:
            print(f"cosec({x}) = {1/sin_x}\n")
        else:
            print("Error: cosec(x) undefined for sin(x) = 0\n")

    elif a == "6":
        x = float(input("You chose cot(x). Enter value of x (in radians): "))
        tan_x = np.tan(x)
        if tan_x != 0:
            print(f"cot({x}) = {1/tan_x}\n")
        else:
            print("Error: cot(x) undefined for tan(x) = 0\n")

    elif a == "7":
        x = float(input("You chose log(x). Enter a positive value: "))
        if x > 0:
            print(f"log10({x}) = {np.log10(x)}\n")
        else:
            print("Error: log(x) undefined for x <= 0\n")

    elif a == "8":
        print("\n_____( Thank you )_____\n")
        break

    else:
        print("Invalid option. Please choose a valid number from 1 to 8.\n")

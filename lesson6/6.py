num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
option = input("chose the option(+, -, *, /): ")

if option == "+":
    print(f"Calculation {num1} + {num2} = {num1 + num2}")
elif option == "-":
    print(f"Calculation {num1} - {num2} = {num1 - num2}")
elif option == "*":
    print(f"Calculation {num1} * {num2} = {num1 * num2}")
elif option == "/":
    print(f"Calculation {num1} / {num2} = {num1 / num2}")
else:
    print("Invalid option")
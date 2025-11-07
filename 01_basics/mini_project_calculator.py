print("*** My Mini Calculator Program ***")
print()

try:
    num1 = int(input("Type the first number: "))
    num2 = int(input("Type the second number: "))
    operation = input("Select one of the following options: '+','-','*','/': ")

    if operation == "+":
        print(f"The result of {num1} {operation} {num2} is: {num1 + num2}")

    elif operation == "-":
        print(f"The restult of {num1} {operation} {num2} is: {num1 - num2}")

    elif operation == "*":
        print(f"The restult of {num1} {operation} {num2} is: {num1 * num2}")

    elif operation == "/":
        if num2 != 0:
            print(f"The restult of {num1} {operation} {num2} is: {num1 / num2}")
        else:
            print("You cannot divide with 0! Try again!")

    else:
        print("Try Again!")

except ValueError:
    print("Please enter a valid number.")

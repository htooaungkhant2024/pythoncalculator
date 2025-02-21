def calculator(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Choose the correct operator"

print("This is python calculator!\n")

operator = input("Choose your operator '+, -, *, /': ")
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

result = calculator(operator, num1, num2)

print(f"Your result is {result}")
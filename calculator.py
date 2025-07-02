def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b


should_continue = True
num1 = float(input("What's the first number?: " ))

while should_continue:
    operation = input("+\n-\n*\n/\nPick an operation: ")
    num2 = float(input("What's the second number? "))

    if operation == "+":
        answer = add(num1,num2)
    elif operation == "-":
        answer = subtract(num1,num2)
    elif operation == "*":
        answer = multiply(num1,num2)
    elif operation == "/":
        answer = divide(num1,num2)
    else:
        print("Enter the valid input")
    print(f"{num1} {operation} {num2} = {answer}")
    choice = input(f"Type 'y' to continue calculating with {answer} , or type 'n' to start a new calculation: ")
    if choice == "y":
        num1 = answer
    elif choice == "n":
        num1 = float(input("What's the first number?: " ))
    else:
        should_continue = False
        print("Thanks for using")
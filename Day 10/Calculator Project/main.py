def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2

# Define operations once (outside loop)
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

continue_calc = True
current_result = None

while continue_calc:
    if current_result is None:
        n1 = int(input("Enter a number: "))
    else:
        n1 = current_result

    operator = input("Enter operator (+, -, *, /): ")

    if operator not in operations:
        print("Invalid operator")
        continue

    n2 = int(input("Enter another number: "))

    result = operations[operator](n1, n2)
    print(f"Answer of {n1} {operator} {n2} is {result}")

    choice = input("Continue calculation? (y/n): ")
    if choice == "n":
        break

    reuse = input(f"Continue with {result}? (y/n): ")
    if reuse == "y":
        current_result = result
    else:
        current_result = None
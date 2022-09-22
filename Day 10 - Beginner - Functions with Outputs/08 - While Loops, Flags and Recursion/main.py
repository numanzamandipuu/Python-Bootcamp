# Add
def add(n1, n2):
    return n1 + n2

# Substract
def substract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = int(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue == True:
        operations_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))

        calculator_function = operations[operations_symbol]
        answer = calculator_function(num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {answer}")

        next_calculation = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")
        if next_calculation == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()


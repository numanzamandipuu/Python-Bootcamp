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

num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
operations_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))

calculator_function = operations[operations_symbol]
answer = calculator_function(num1, num2)

print(f"{num1} {operations_symbol} {num2} = {answer}")

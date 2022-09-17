# Simple Function
# def greet():
#     print("Hello Dipu")
#     print("How do you do Dipu?")
#     print("Isn't the weather nice today?")
# greet()

# Function that allows for input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")

# greet_with_name("Dipu")

# Functions with more than one input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# greet_with("Dipu", "Dhaka")
# vs.
# greet_with("Dhaka", "Dipu")

# Functions with keyword arguments

greet_with(location="Dhaka", name= "Dipu")
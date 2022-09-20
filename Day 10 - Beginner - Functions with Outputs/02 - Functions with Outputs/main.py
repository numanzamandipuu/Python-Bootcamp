# # Functions with Outputs

# def format_name(f_name, l_name):
#     f_name.title()
#     l_name.title()

def name(num01, num02):
    number = num01 * num02
    return number

number01 = int(input("gimme num01:\n"))
number02 = int(input("gimme num 02:\n"))

print(name(number01, number02))
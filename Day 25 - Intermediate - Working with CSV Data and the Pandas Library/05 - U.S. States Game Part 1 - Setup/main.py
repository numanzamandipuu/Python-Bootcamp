import turtle


screen = turtle.Screen()
screen.title("U.S. States Game")
img_path = "D:/Python-Bootcamp/Day 25 - Intermediate - Working with CSV Data and the Pandas Library/05 - U.S. States Game Part 1 - Setup/blank_states_img.gif"
screen.addshape(img_path)
turtle.shape(img_path)

answer_state = screen.textinput(title= "Guess the State!", prompt= "What's another state's name?")
print(answer_state)
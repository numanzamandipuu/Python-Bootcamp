import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
img_path = "D:/Python-Bootcamp/Day 25 - Intermediate - Working with CSV Data and the Pandas Library/05 - U.S. States Game Part 1 - Setup/blank_states_img.gif"

screen.addshape(img_path)
turtle.shape(img_path)

cap_answer = screen.textinput(title= "Guess the State!", prompt= "What's another state's name?")
answer = cap_answer.title()

data = pandas.read_csv("D:/Python-Bootcamp/Day 25 - Intermediate - Working with CSV Data and the Pandas Library/05 - U.S. States Game Part 1 - Setup/50_states.csv")
state_list = data["state"].tolist()
state_set = set(state_list)

if answer in state_set:
    print("boom")
else:
    print("not boom")


screen.exitonclick()
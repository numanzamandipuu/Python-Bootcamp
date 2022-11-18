import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
img_path = "D:/Python-Bootcamp/Day 25 - Intermediate - Working with CSV Data and the Pandas Library/05 - U.S. States Game Part 1 - Setup/blank_states_img.gif"


turtle.bgpic(img_path)
turtle.hideturtle()
turtle.penup()
n = 0
correct_ans = 0
correct_guess = [""]


data = pandas.read_csv("D:/Python-Bootcamp/Day 25 - Intermediate - Working with CSV Data and the Pandas Library/05 - U.S. States Game Part 1 - Setup/50_states.csv")
state_list = data["state"].tolist()
state_set = set(state_list)


while n < 5:

    cap_answer = screen.textinput(title= f"{correct_ans}/50 States Correct", prompt= "What's another state's name?")
    answer = cap_answer.title()
    correct_set = set(correct_guess)

    if answer in state_set:
        if answer in correct_set:
            pass
        else:
            ans_row = data[data.state == answer]
            turtle.setposition(int(ans_row["x"]), int(ans_row["y"]))
            turtle.write(answer)
            correct_ans += 1
            correct_guess.append(answer)
    else:
        pass

    n += 1


screen.exitonclick()
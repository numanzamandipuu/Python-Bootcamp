import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
img_path = "D:/Python-Bootcamp/Day 25 - Intermediate - Working with CSV Data and the Pandas Library/05 - U.S. States Game Part 1 - Setup/blank_states_img.gif"


turtle.bgpic(img_path)
turtle.hideturtle()
turtle.penup()
correct_ans = 0
correct_guess = []


data = pandas.read_csv("D:/Python-Bootcamp/Day 25 - Intermediate - Working with CSV Data and the Pandas Library/05 - U.S. States Game Part 1 - Setup/50_states.csv")
state_list = data["state"].tolist()

while len(correct_guess) < 50:

    cap_answer = screen.textinput(title= f"{correct_ans}/50 States Correct", prompt= "What's another state's name?")
    answer = cap_answer.title()

    if answer in state_list:
        if answer in correct_guess:
            pass
        else:
            ans_row = data[data.state == answer]
            turtle.setposition(int(ans_row["x"]), int(ans_row["y"]))
            turtle.write(answer)
            correct_ans += 1
            correct_guess.append(answer)

    if answer == "Exit":
        break


missed_state_set = set(state_list) - set(correct_guess)
missed_state = list(missed_state_set)
list_data = pandas.DataFrame(missed_state)
list_data.to_csv("D:/Python-Bootcamp/Day 25 - Intermediate - Working with CSV Data and the Pandas Library/07 - U.S. States Game Part 3 - Saving Data to .csv/states_to_learn.csv")
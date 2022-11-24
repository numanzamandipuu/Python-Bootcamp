import pandas

student_dict = {
    "student" : ["dipu", "angela", "yu"],
    "score" : [56, 76, 98]
}

# looping through dictionary 
for (key, value) in student_dict.items():
    print(key)
    print(value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# looping through a dataframe
for (key, value) in student_data_frame.items():
    print(key)
    print(value)

# looping through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)

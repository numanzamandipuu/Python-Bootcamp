student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    pass

{"A": "Alfa", "B": "Bravo"}

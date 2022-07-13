## Lets see how to create a data frame FROM SCRATCH
import pandas as pd

# Using a dict
data_dict = {
    "students": ["Victor", "Fábio", "Luca"],
    "scores": [20, 18, 15]
}
print(data_dict)

data_df = pd.DataFrame(data_dict)
print(data_df)

data_df.to_csv("./day_25/students_grade.csv")
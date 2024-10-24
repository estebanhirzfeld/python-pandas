import pandas as pd

# READ CSV + PRINT --------------------------------------

df = pd.read_csv("username.csv")

# print(df.to_string())

# DATASET TO DATAFRAME ----------------------------------

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

var = pd.DataFrame(mydataset)

print(var)

# SERIES + INDEX ------------------------------------------------

a = [1,9,15]

var = pd.Series(a)

var = pd.Series(a, index = ["first", "second", "third"])

# print(var)

# OBJECTS TO SERIES ---------------------------------------------

calories = {"day1": 420, "day2": 380, "day3": 390}

var = pd.Series(calories)

var = pd.Series(calories, index = ["day1", "day2"])


print(var)


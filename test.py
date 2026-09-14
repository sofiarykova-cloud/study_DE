import pandas as pd

df = pd.read_csv("employees.csv")

df["country"] = "Russia"

df = df.drop(columns=["country"])


print(df[(df["salary"] > 100000) & (df["department"] == "IT")]) # двойная фильтрация пример


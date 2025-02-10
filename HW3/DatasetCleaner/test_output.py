# Cleaning dataset: "dataset.csv"
import pandas as pd
df = pd.read_csv("dataset.csv")
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df["age"].fillna(30, inplace=True)
df = df[df["age"] >= 18]
df.rename(columns={"old_name": "new_name"}, inplace=True)
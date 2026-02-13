import pandas as pd

df = pd.read_csv("crime_dataset_india.csv")

df.to_json("crime.json", orient="records", indent=4)

print("Converted CSV → crime.json successfully!")

# https://python.pages.doc.ic.ac.uk/lessons/pandas/03-df/04-pokemon.html

import pandas as pd

df = pd.read_csv('Pokemon.csv')

#Find out how many columns the dataset contains.

print(f"Antallet kolonner og rækker: {df.shape}")

# Find out the column names in the dataset. Can you convert this into a Python list?

print(f"Navne på kolonner = {df.columns}")

columns_list = list(df)

# Get the data type for each column (is it a boolean? An integer? A string?) Can you convert this info into a NumPy array?

print(df.info())

nparray = df.dtypes.to_numpy()

# Try printing out the first 20 Pokemons and the last 10 Pokemons!

print(df.head(20))

print(df.tail(10))

#How many Legendary Pokemons are there? Use .value_counts() to discover this!

print(df["Legendary"].value_counts())

#Print all Pokemons that have "Water" as Type 1 and "Dragon" as Type 2.
filtered_type1_water_type2_dragon = df[(df["Type 1"] == "Water") & (df["Type 2"] == "Dragon")]

print(filtered_type1_water_type2_dragon)

#Print all Pokemons that are either Type 2 "Electric" or Type 2 "Ice"

filtered_type2_electric_or_ice = df[df["Type 2"].isin(["Electric","Ice"])]

print(filtered_type2_electric_or_ice)


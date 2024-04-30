import pandas as pd
import matplotlib.pyplot as plt

#indlæs datasættet i en DataFrame
df = pd.read_csv("recipeData.csv", encoding='Latin-1').set_index("BeerID")
print(df.info())

#fjern manglende værdier

df_without_NAvalues_rows = df.dropna()

print(df_without_NAvalues_rows.info())

df_without_NAvalues_cols = df.dropna(axis=1)

print(df_without_NAvalues_cols.info())

#plot numeriske variabler i datasættet

fig = plt.figure()

axis = df["StyleID"].plot.hist(bins=100)
plt.xlabel("StyleID")
plt.show()
'''Indlæs global temperatur data fra Berkeley Earth'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

url = "https://berkeley-earth-temperature.s3.us-west-1.amazonaws.com/Global/Complete_TAVG_complete.txt"

df = pd.read_csv(url, delim_whitespace=True, skiprows=72, header=None, index_col= False)

#Opretter featurenavne

column_names = [
    "Year",
    "Month",
    "Monthly_anomaly",
    "Monthly_uncertainty",
    "Annual_anomaly",
    "Annual_uncertainty",
    "Five_year_anomaly",
    "Five_year_uncertainty",
    "Ten_year_anomaly",
    "Ten_year_uncertainty",
    "Twenty_year_anomaly",
    "Twenty_year_uncertainty",
]

df.columns = column_names

'''Præprocesser data for at fjerne manglende værdier (NaN).'''
# Dropper rækker med NaN værdier. 
df = df.dropna()

'''Bliv fortrolig med dataene ved at beregne statistiske resuméer 
(middelværdi, median, standardafvigelse, min/max, kvartiler) og enkle 
visualiseringer som linjeplots af temperaturen over tid.'''

#Bruger til at beskrive statistiske værdier. 
df.describe()


# Simplet tidsserieplot med ændring over tid.
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df["Ten_year_anomaly"], color='blue', marker='o', linestyle='-')
plt.title('Temperature Anomaly Over Time')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly (°C)')
plt.grid(True)

'''Lav en figur med flere underplots, hver viser et forskelligt aspekt 
såsom globale temperaturtendenser, temperaturanomalier og et histogram
 af temperaturer.'''

# Figur med underplots jf. opgavebeskrivelsen. 
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 12))

axes[0].plot(df['Year'], df['Annual_anomaly'], color='blue', marker='o', linestyle='-', label='Temperature Anomaly')
axes[0].set_title('Temperature Tendencies Over Time')
axes[0].set_xlabel('Year')
axes[0].set_ylabel('Temperature Anomaly (°C)')
axes[0].legend()
axes[0].grid(True)

axes[1].errorbar(df['Year'], df['Annual_anomaly'], yerr=df['Annual_uncertainty'], color='red', marker='o', linestyle='-', label='Temperature Anomaly ± Uncertainty')
axes[1].set_title('Temperature Anomalies Over Time with Uncertainty')
axes[1].set_xlabel('Year')
axes[1].set_ylabel('Temperature Anomaly (°C)')
axes[1].legend()
axes[1].grid(True)

axes[2].hist(df['Annual_anomaly'], bins=20, color='green', alpha=0.7)
axes[2].set_title('Histogram of Temperature Anomalies')
axes[2].set_xlabel('Temperature Anomaly (°C)')
axes[2].set_ylabel('Frequency')
axes[2].grid(True)

plt.tight_layout()


'''Brug varmekort til at repræsentere ændringer i temperaturer over årene.
Overlay et linjeplot på varmekortet for at vise den gennemsnitlige
 temperatur for hvert år (heatmap hvor x-akse viser år,
y-akse måned og z-akse temperatur, linjeplot
 hvor x-akse er år og y-akse er gennemsnitstemperatur).'''
#Laver heatmap data
heatmap_data = df.pivot(index='Month', columns='Year', values='Annual_anomaly')

#Beregner gennemsnitstemperatur 
avg_temp_per_year = df.groupby('Year')['Monthly_anomaly'].mean()

#Opretter figuren
fig, ax = plt.subplots(figsize=(12, 8))

#Opretter heatmap
sns.heatmap(heatmap_data, cmap='coolwarm', ax=ax)


#Indsætter overlay linjeplot, der indeholder gennemsnitstemperaturen.
ax.plot(avg_temp_per_year.index, avg_temp_per_year.values, color='black', marker='o', linestyle='-')
ax.set_title('Temperature Changes Over Time')
ax.set_xlabel('Year')
ax.set_ylabel('Month')


#Det samme med som ovenstående men i 3D. 
heatmap_data = df.pivot(index='Month', columns='Year', values='Monthly_anomaly')


x = np.array(heatmap_data.columns)
y = np.array(heatmap_data.index)
X, Y = np.meshgrid(x, y)
Z = heatmap_data.values

#Opretter 3D figur. 
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

#Plotter headmappet. 
ax.plot_surface(X, Y, Z, cmap='coolwarm')

#Opretter labels til akser og titel til figur
ax.set_xlabel('Year')
ax.set_ylabel('Month')
ax.set_zlabel('Temperature Anomaly (°C)')
ax.set_title('Temperature Changes Over Time')


plt.show()

'''[Optionelt] Introducer interaktive elementer ved hjælp af 
matplotlib.widgets eller ipywidgets for at lade brugerne 
vælge, hvilket lands data der skal vises.'''
'''[Optionelt] Tilpas plots med forskellige farvekort, 
justering af akser, tilføjelse af gitre og brug af annotationer
til at fremhæve specifikke begivenheder eller punkter 
(f.eks. væsentlige klimabegivenheder).'''
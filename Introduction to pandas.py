import pandas as pd

#Opret en serie instans 
series = pd.Series(data=["UK", "France", "Italy"])

#Give serien et navn 
series = pd.Series(data=["UK", "France", "Italy"], name="country")

#Manuel indeksering af rækker
series = pd.Series(data=["UK", "France", "Italy"], index=["a", "b", "c"], name="country")

#Oprette en serie instans ud fra dictionary
series = pd.Series(data={"a": "UK", "b": "France", "c": "Italy"})

#Anvende index til at matche i dictionarys 
series = pd.Series(data={"a": "UK", "b": "France", "c": "Italy"}, index=["b", "c", "d", "a"])

#Tilgå elementer i serie
series = pd.Series(data=["UK", "France", "Italy"])

series[0]
series[:1]

#Tilgå elementer ud fra index labels
series = pd.Series(data={"a": "UK", "b": "France", "c": "Italy"})

series["a"]
series[["c","b"]]

#Omdanne serie til numpy array eller en liste. 
series = pd.Series(data={"a": "UK", "b": "France", "c": "Italy"})

series_array = series.to_numpy()
series_list = list(series)

#Oprette en dataframe ud fra data
data = [["UK", "London"], ["France", "Paris"], ["Italy", "Rome"]]

df= pd.DataFrame(data=data)

#Ændrer indeks til at være prefixes i stedet. 
data = [["UK", "London"], ["France", "Paris"], ["Italy", "Rome"]]
prefixes = ["+44", "+33", "+39"]
col_names = ["country", "capital"]

df = pd.DataFrame(data=data, index=prefixes, columns=col_names)

#Oprette dataframe ud fra dictionary
data = {"country": ["UK", "France", "Italy"], 
            "capital": ["London", "Paris", "Rome"]}
prefixes = ["+44", "+33", "+39"]

df = pd.DataFrame(data=data, index=prefixes)

#Oprette dataframe ud fra en liste i et dictionary
data = [{"country": "UK", "capital": "London"},
            {"country": "France", "capital": "Paris"},
            {"country": "Italy", "capital": "Rome"}]
prefixes = ["+44", "+33", "+39"]

df = pd.DataFrame(data=data, index=prefixes)

#Indlæse csv til en dataframe
df = pd.read_csv("capitals.csv")

#Hvis Code skal være indeks

df= pd.read_csv("capitals.csv", index_col=0)






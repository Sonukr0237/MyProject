import pandas as pd

pokemon = pd.read_csv('Pokemon.csv')
pokemonData = pokemon.head()
print(pokemonData)

# Setting an index
pokemonName = pokemon.set_index('Name')
pokemonNameData = pokemonName.head()
print(pokemonNameData)

# Resetting index to default
pokemonDefault = pokemon.reset_index()
print(pokemonDefault)

# Reset index and drop previous index
dropIndex = pokemonNameData.reset_index(drop=True)
print(dropIndex)

names =  ['Ivysaur', 'Bulbasaur']
subSetNames = [pokemon['Name'].isin(names)]
print(subSetNames)

# Using .loc[]

pokemonNameLoc = pokemonName.loc[names]
print(pokemonNameLoc)

# Setting multi Level indexes

pokemonMulti = pokemon.set_index(['Name', 'Type 1'])
print(pokemonMulti.head())

# Slicing Index Values

pokemonSrt = pokemonMulti.sort_index()
print(pokemonSrt.head())

print(pokemonSrt.loc['Bulbasaur':'Kakuna'])


# Slicing time Series

print(pokemon.iloc[4,1])

# to get first 5 rows

print(pokemon.iloc[:5])

# to get all rows of column "Name", "Type 1", "Type 2":

print(pokemon.iloc[:,1:4])

# To get 10 rows of column 'Name', 'Type 1','Type 2':

print(pokemon.iloc[:10,1:4])


import pandas as pd
titulos = pd.read_csv('data/titles.csv')
print(titulos.head(10))
print("\n"*2)
elenco = pd.read_csv('data/cast.csv')
print(elenco.head(10))
print(titulos[titulos.title.str.contains("war")].sort_values('year'))
print(titulos[titulos.title== "Dracula"].sort_values("year"))
print(titulos[titulos.title.str.contains("Dracula")].sort_values('year'))
print(titulos[titulos.title.str.contains("The Lord of the Rings")].sort_values('year'))
print(len(titulos[titulos.title.str.contains("The Lord of the Rings")].sort_values('year')))
print( elenco[elenco.character == "Superman"] )
print( len(elenco[elenco.character == "Superman"] ))


import pandas as pd
titulos = pd.read_csv('data/titles.csv' )
print(titulos.head(5))
print("\n"*2)
elenco = pd.read_csv('data/cast.csv', encoding='utf-8')
print(elenco.head(5))
print("\n"*2)
print(len(titulos))
print("\n"*2)
print ((len(elenco)))
print("\n"*2)
# Cual fue la primer pelicula hecha titulada "Romeo and Juliet" ?
print(titulos[titulos.title == "Romeo and Juliet"].sort_values('year').head(20))
print(titulos[titulos.title.str.contains("lord")].sort_values('year'))
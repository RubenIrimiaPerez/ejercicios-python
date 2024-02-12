import pandas as pd

nombres = ['Carlos', 'Maria', 'Elias']
edades = [24, 32, 13]
df = pd.DataFrame({'Nombre':nombres, 'Edad':edades })
print(df)

df.index.name = 'ID'

#Generar el documento

df.to_excel('documento.xlsx')
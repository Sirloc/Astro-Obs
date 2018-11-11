import pandas as pd


df = pd.read_table('Objetos_Ciencia_tabla.txt',
					 sep = '|',
					 names = ['Spectral Type', 'Name', 'Catalog Name', 'Ra, Dec j2000', 'Ra, Dec on date', 'mb', 'mg', 'Varviacion en magnitud' ],
					 )
df.to_csv('Table.csv')

df_1 = pd.read_table('Objetos_Ciencia.txt',
					 sep = '|',
					 names = ['ID', 'Spectral Type', 'Name', 'Catalog Name', 'Ra, Dec j2000', 'Ra, Dec on date', 'mb', 'mg', 'magnitude range', 'Type' ],
					 )
df_1.to_csv('Full_Table.csv')

#OBAFGKM
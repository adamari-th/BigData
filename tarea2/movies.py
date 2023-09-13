import pandas as pd
#url = "movie_metadata.csv"

movie = pd.read_csv("movie_metadata.csv", header=0, index_col=0)
print("\t\tDATAFRAME\n", movie) 

print("\n1.- Rellenar con el valor promedio de todos los valores en la columna |gross|\n")
promedio = movie['gross'].mean()
movie['gross'] = movie['gross'].fillna(promedio)
print(movie['gross'].head(6))

print("\n2.- Reemplazar los valor nulos a 0 |facenumber_in_poster|\n")
movie['facenumber_in_poster'] = movie['facenumber_in_poster'].fillna(0)
print(movie['facenumber_in_poster'].head(20))

print("\n3.- Crear columna TittleCode de la columna movie__imdb_lin\n")
#crear = movie['movie__imdb_link']
movie['TittleCode']=movie['movie_imdb_link'].str.split('/').str[4]
print(movie['TittleCode'].head(20))

print("4.- Rellenar las celdas con valor 0 a la columna tittle_year\n")
movie['title_year']=movie['title_year'].fillna(0)
print(movie[['title_year']].head(10))

print("5.- Seleccion de filas -USA- desde columna country, eliminar las filas restantes\n")
movie = movie.query('country == "USA"')
print(movie['country'].head(10))
print("Eliminar restante\n")
movie.drop(movie[(movie['country']!= 'USA')].index,inplace=True)
print(movie['country'].head(20))

#generar un nuevo archivo
movie.to_csv("FilmTV_USAMovies2.csv")
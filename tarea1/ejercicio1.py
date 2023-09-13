import pandas as pd
url = "datos.csv"

##Leer el archivo
datos = pd.read_csv(url, header=0, index_col=0)
print("\t\tDATAFRAME\n", datos) 

print("\n1.- Identificar el semestre y grupo que poseen el mayor número de estudiantes reprobados:\n")
datos1 = pd.read_csv(url, header=0, index_col=0, usecols = ['Semestre','Grupo','Reprobados'])   
reprobados = datos1.sort_values(by= 'Reprobados', ascending=False)          ## .sort_values => Ordene por los valores a lo largo de cualquiera de los ejes.
print(reprobados.head(1),"\n")                                              ## .head => Devuelve las primeras n filas  

print("2.- Identificar el total de estudiantes inscritos entre 1° y 5° semestre de LIDTS:\n")
print("El total es: ", datos["Total"].head(5).sum())

print("\n3.- Identificar los 3 primeros grupos que poseen mayor número de estudiantes beneficiados con Beca:\n")
datos2 = pd.read_csv(url, header=0, index_col=0, usecols = ['Semestre','Grupo','Beca'])
beca = datos2.sort_values(by= "Beca", ascending=False)
print(beca.head(3),"\n")    
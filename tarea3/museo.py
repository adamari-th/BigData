import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image as PILImage
import io
import folium
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

museo = pd.read_csv("new-york-city-art-galleries-1.csv")
print("\t\tDATAFRAME - MUSEOS & GALERIAS\n",museo)

print("\n1.- Eliminar filas o registros duplicados:")
museo = museo.drop_duplicates()
print(museo.head(160))

print("\n2.- Eliminar la columna Address2:")
museo = museo.drop(['ADDRESS2'], axis= 1) #axis: para indicar que deseo eliminar una columna
print(museo.head())

print("\n3.- Seleccionar los museos o galerías de arte del distrito Brooklyn:")
museo = museo.query('CITY == "Brooklyn"')
print(museo['CITY'].head(10))

print("\n4.- Filtrar a los 3 mejor calificados (museo o galería)")
museo = museo.loc[museo['GRADING'] >= 8.2 ]   #loc: nos permite obtener un conjunto de filas >>> 
                                              #se selecciona a la columna y se comprueba el valor dado
museo3 = museo.head(3)
print(museo3)

print("\n5.- Generar imagen de Mapa indicando la ubicación de los 3 mejores")
mapa_museo = folium.Map(location=[40.7037979,-74.0202391], zoom_start=13)

museo3 = museo.head(3)
for indice, row in museo3.iterrows():
    name = row['NAME']
    address = row['ADDRESS1']
    lat, lon = map(float, row['the_geom'].replace('POINT (', '').replace(')', '').split())
    lat, lon = round(lon, 4), round(lat, 4)
    rating = row['GRADING']

    popup_text = f"Name: {name}\nAddress: {address} \nGrade: {rating}"
    folium.Marker(location=[float(lat), float(lon)], popup=popup_text).add_to(mapa_museo)

temp_html_file = 'mapa.html'
mapa_museo.save(temp_html_file)

img_data = mapa_museo._to_png()
img = PILImage.open(io.BytesIO(img_data))
img.save('mapa.png')

doc = SimpleDocTemplate("ReporteFinal.pdf", pagesize=letter)

styles = getSampleStyleSheet()
datos = []

titulo = "The best Galleries and Museums\n"
datos.append(Paragraph(titulo, styles["Title"]))

imagen_mapa = Image("mapa.png", width=400, height=200)
datos.append(imagen_mapa)

for index, row in museo3.iterrows():
    name = row['NAME']
    address = row['ADDRESS1']
    rating = row['GRADING']

    # Crear un párrafo de texto con los datos
    texto_datos = f"\nName: {name} \nAddress: {address} \nGrade: {rating}"
    datos.append(Paragraph(texto_datos, styles["Normal"]))


doc.build(datos)

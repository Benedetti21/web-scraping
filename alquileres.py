from itertools import count
from bs4 import BeautifulSoup 
from matplotlib.pyplot import text
import requests
import pandas as pd

url = 'https://www.incontratoweb.com.ar/propiedades/departamentos_alquiler_monte-grande'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#DptosNombre

dptos = soup.find_all('p', class_= 'card__title')

departamentos = list()

#print(dptos)
count = 0
for i in dptos:
    if count < 100:
        departamentos.append(i.text)
    else: 
        break
    count += 1    
#print(departamentos, len(departamentos))


#Location

loc = soup.find_all('p', class_= 'card__location')

location = list()

count = 0
for i in loc:
    if count < 100:
        location.append(i.text)
    else: 
        break
    count += 1    



#DptosPrecios

precios = soup.find_all('span', class_= 'prices')

preciosDpto = list()

#print(dptos)
count = 0
for i in precios:
    if count < 100:
        preciosDpto.append(i.text)
    else: 
        break
    count += 1    
#print(preciosDpto, len(preciosDpto))

df = pd.DataFrame({'Departamento' : departamentos, 'Locación' : location, 'Precios' : preciosDpto})
print(df)

df.to_csv('Alquileres-MG.csv', encoding='utf-8-sig')





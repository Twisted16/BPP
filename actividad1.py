#APARTADO 1

import pandas as pd

data= pd.read_table("finanzas2020[1].csv")

data['Enero'] = data['Enero'].str.replace("'", " ")
enero = data['Enero'].astype('int')
enero = enero.sum()

febrero = data['Febrero'].sum()
marzo = data['Marzo'].sum()
abril = data['Abril'].sum()
mayo = data['Mayo'].sum()
junio = data['Junio'].sum()

data['Julio'] = data['Julio'].str.replace("'", " ")
julio = data['Julio'].astype('int')
julio = julio.sum()

agosto = data['Agosto'].sum()
data['Septiembre'] = data['Septiembre'].str.replace("bug", "0")

septiembre = data['Septiembre'].astype('int')
septiembre = septiembre.sum()
print(f"septiembre  {septiembre}")

data['Octubre'] = data['Octubre'].str.replace("ups", "0")
octubre = data['Octubre'].astype('int')
octubre = octubre.sum()

data['Noviembre'] = data['Noviembre'].str.replace("'", " ")
noviembre = data['Noviembre'].astype('int')
noviembre = noviembre.sum()

diciembre = data['Diciembre'].sum()

print(f"Enero = {enero}, Febrero = {febrero}, Marzo = {marzo}, Abril = {abril}, Mayo = {mayo}, junio = {junio}, julio = {julio}, agosto ={agosto}, septiembre = {septiembre} octubre = {octubre}, noviembre = {noviembre}, diciembre = {diciembre}")


#¿Qué mes ha ahorrado más?
año = {"enero": enero, "febrero": febrero, "marzo": marzo, "abril":abril, "mayo": mayo, "junio": junio, "julio": julio, "agosto": agosto, 'septiembre': septiembre, "octubre": octubre, "noviembre": noviembre, "diciembre":diciembre}
max_anio = max(año, key=año.get)
print(f"El mes que más se ha ahorrado es {max_anio}")


#Qué mes ha gastado más?
min_anio = min(año, key=año.get)
print(f"El mes que más se ha gastado es {min_anio}")


#Cuál es la media de gasto?
aniolist=(enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre)

def obtener_media(aniolist):
    sumatoria = 0
    for valor in aniolist:
        sumatoria += valor
    longitud = len(aniolist)
        
    return sumatoria / longitud

media = obtener_media(aniolist)
print(f"La media es {media}")


#¿Cuál ha sido el gasto total a lo largo del año?
def obtener_gasto(aniolist):
    gasto = 0
    for valorg in aniolist:
        if valorg <= 0:
            gasto += valorg
       
    return gasto

gastototal=obtener_gasto(aniolist)
print(f"El gasto total ha sido de {gastototal}")


#¿Cuáles han sido los ingresos totales a lo largo del año?
def obtener_ingresos(aniolist):
    ingresos = 0
    for valori in aniolist:
        if valori >= 0:
            ingresos += valori
       
    return ingresos

ingresostotal=obtener_ingresos(aniolist)
print(f"Los ingresos totales han sido de {ingresostotal}")



#APARTADO 2

#Compruebe que el fichero existe y que tiene 12 columnas, una para cada mes del año.
#Para cada mes compruebe que hay contenido.
#Compruebe que todos los datos son correctos. De no haber un dato correcto, el programa debe saber actuar en consecuencia y continuar con su ejecución.


df = pd.DataFrame(data)

try:
    archivo = open('finanzas2020[1].csv')
    total_cols=len(df.axes[1])
    print(f"El archivo existe y tiene {total_cols} columnas")
    print(data)
    archivo.close()
except FileNotFoundError:
    print('El archivo que busca no existe')
    exit()




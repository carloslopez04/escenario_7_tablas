# Importaciónde librerías
import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

# Título de la página
st.title('EMPLEATRONIX CLM')
st.write('Todos los datos de la empresa en un solo lugar')

# Dataframe
empleados = pd.read_csv('dataset/employees.csv')
st.dataframe(empleados)

# Barra separadora
st.write('---')

# Columnas para alinear los eventos. 
col1, col2, col3 = st.columns(3)

with col1:
    color = st.color_picker("Escoge un color", "#00f900")

with col2:
    nombre = st.toggle("Mostrar nombre. ")

with col3:
    sueldo = st.toggle("Mostrar sueldo en la barra")
    
# Tmaño de la gráfica
plt.figure(figsize=(9, 6))
# Crear la figura y los ejes
fig, ax = plt.subplots()
# Crear la gráfica de barras horizontales
ax.barh(empleados['full name'], empleados['salary'], color=color)
# Ampliar x y rotar etiquetas
plt.xlim(0, 4500)
plt.xticks(rotation=90)
# Ocultar los ejes Y
ax.set_yticklabels([]) 
# Agregar etiquetas de nombre en el eje Y
if nombre : 
    ax.set_yticklabels(empleados['full name'])

# Agregar etiquetas de sueldo en las barras
if sueldo:
    for i, v in enumerate(empleados['salary']):
        ax.text(v, i, f"{v}€", color='black', va='center')

# Mostrar la gráfica en Streamlit
st.pyplot(fig)

# Derechos de autor 

st.write("© 2024, Carlos López Muñoz - CPIFP Alan Turing.") 
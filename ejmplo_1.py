import matplotlib.pyplot as plt

# Datos para el gráfico
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [12, 7, 3, 17, 6]

# Crear un gráfico de barras
plt.bar(categorias, valores)

# Agregar etiquetas al gráfico
plt.title('Gráfico de Barras Ejemplo')
plt.xlabel('Categorías')
plt.ylabel('Valores')

# Mostrar el gráfico
plt.show()

import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, StringVar, OptionMenu

# Función para crear el gráfico seleccionado
def crear_grafico():
    grafico_seleccionado = opcion_grafico.get()  # Obtener el tipo de gráfico seleccionado

    categorias = entrada_categorias.get().split(',')
    valores = [int(x) for x in entrada_valores.get().split(',')]
    
    # Crear y mostrar el gráfico según la selección del usuario
    if grafico_seleccionado == "Gráfico de Barras":
        plt.bar(categorias, valores)
        plt.title('Gráfico de Barras')
        plt.xlabel('Categorías')
        plt.ylabel('Valores')
    elif grafico_seleccionado == "Gráfico de Línea":
        plt.plot(categorias, valores)
        plt.title('Gráfico de Línea')
        plt.xlabel('Categorías')
        plt.ylabel('Valores')
    elif grafico_seleccionado == "Gráfico de Pastel":
        plt.pie(valores, labels=categorias, autopct='%1.1f%%')
        plt.title('Gráfico de Pastel')

    plt.show()

# Crear una ventana de tkinter
ventana = Tk()
ventana.title("Ingreso de Datos y Selección de Gráfico")

# Etiquetas y campos de entrada
Label(ventana, text="Categorías (separadas por comas):").grid(row=0, column=0)
Label(ventana, text="Valores (separados por comas):").grid(row=1, column=0)
Label(ventana, text="Selecciona el tipo de gráfico:").grid(row=2, column=0)

entrada_categorias = Entry(ventana)
entrada_valores = Entry(ventana)

entrada_categorias.grid(row=0, column=1)
entrada_valores.grid(row=1, column=1)

# Widget de selección de tipo de gráfico
opciones_grafico = ["Gráfico de Barras", "Gráfico de Línea", "Gráfico de Pastel"]
opcion_grafico = StringVar(value=opciones_grafico[0])
menu_desplegable = OptionMenu(ventana, opcion_grafico, *opciones_grafico)
menu_desplegable.grid(row=2, column=1)

# Botón para crear el gráfico
Button(ventana, text="Crear Gráfico", command=crear_grafico).grid(row=3, column=0, columnspan=2)

ventana.mainloop()


# Interfaz gráfica

import tkinter as tk
from datetime import datetime

def calcular():
    nacimiento = datetime.strptime(entrada.get(), "%d/%m/%Y")
    hoy = datetime.now()

    edad = (hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day)))

    resultado.config(text=f"Su edad es {edad} años")


# crea la ventana
root = tk.Tk()
# tutilo de la ventana
root.title("Aplicacion de Edades")

# tamaño de la ventana
root.geometry("800x600")

saludo = tk.Label(root, text="Calculadora de Edad", font=24, bg="grey")
saludo.pack()

etiqueta = tk.Label(root, text="Ingrese su fecha de nacimiento (DD/MM/YYYY): ", font=24, bg="grey")
etiqueta.pack()
entrada = tk.Entry(root)
entrada.pack()

tk.Button(root, text="calcular", command=calcular).pack()

resultado = tk.Label(root, text="")
resultado.pack()


# ejecuta constantemente la ventana
root.mainloop()
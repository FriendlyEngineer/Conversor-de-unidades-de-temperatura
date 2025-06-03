
import tkinter as tk
from tkinter import ttk

def convertir(): # Se hace la conversión y se imprime una etiqueta con el resultado
    tk.Label(master,text = "                                      ").grid(row=1, column=2)  #  Los espacios son para limpiar de caracteres de salida
    if combo_box2.get() == combo_box.get(): # Si ambas unidades son iguales, el valor de entrada es el de salida
        resultado = valor.get()
    elif combo_box.get() == 'Celsius' and combo_box2.get() =='Fahrenheit':  # El resto se convierte según su respectiva comparación
        resultado = (valor.get() * 9)/5 + 32
    elif combo_box.get() == 'Fahrenheit' and combo_box2.get() =='Celsius':
        resultado = (valor.get() * 5)/9 - 32
    elif combo_box.get() == 'Celsius' and combo_box2.get() =='Kelvin':
        resultado = valor.get() + 273.15
    elif combo_box.get() == 'Kelvin' and combo_box2.get() =='Celsius':
        resultado = valor.get() - 273.15
    elif combo_box.get() == 'Fahrenheit' and combo_box2.get() =='Kelvin':
        resultado = (valor.get() -32)/1.8 +273.15
    elif combo_box.get() == 'Kelvin' and combo_box2.get() =='Fahrenheit':
        resultado = (valor.get() -273.15)*1.8 + 32 

    else:  # De no haber valores, imprime un mensaje de salida indicando la situación
        resultado = "Seleccione dos unidades"
    tk.Label(master,text = resultado, borderwidth=2, bg="lightblue", relief="raised").grid(row=1, column=2) # a la etiqueta de salida se le añade un marco para enfatizar

# Creación de ventana
master = tk.Tk() 
master.title("conversor de unidades") # Se le añade un título a la ventana
master.geometry("300x80") # Se predefine el tamaño de la ventana
master.resizable(False, False) # Se bloqueó el cambio de tamaño de la ventana 

# valores de listas
valores_listas = ["Celsius","Fahrenheit","Kelvin"]

# Creación de combobox de la unidad de temperatura de entrada
combo_box = ttk.Combobox(master, values=valores_listas, width=10)  
combo_box.grid(row=0) # La combobox se coloca en la fila cero
combo_box.current(0) # El valor inicial (normalmente "null") se define como el primero de la lista

# Creación de combobox de la unidad de temperatura de salida
combo_box2 = ttk.Combobox(master, values=valores_listas, width=10)
combo_box2.grid(row=0, column=2)
combo_box2.current(1)

# Texto indicador para la UI
tk.Label(master, text = 'se convierte a:').grid(row = 0, column=1)

# Almacenamiento del valor de temperatura a convertir
valor=tk.IntVar() # Variable asignada al valor a ingresar
entrada1 = tk.Entry(master, textvariable = valor, width=10) 
entrada1.grid(row=1, column=0)

# Creación del botón 
boton_convertir = tk.Button(master, text='Convertir!', height=2, width=15, command = convertir)
boton_convertir.grid(row=1,column=1)


master.mainloop()
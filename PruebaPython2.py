import tkinter as tk

# Función para calcular la cotización
def calcular_cotizacion():
    # Obtener los valores de los campos de entrada
    estilo = estilo_var.get()
    acabado_aluminio = acabado_aluminio_var.get()
   # tipo_vidrio = tipo_vidrio_var.get()
    esmerilado = esmerilado_var.get()
    ancho = float(ancho_var.get())
    alto = float(alto_var.get())
    cantidad = int(cantidad_var.get())

    # Calcular cantidad de aluminio y vidrio requeridos
    ancho_total = ancho + 0.1 # Sumarle 10 cm por los marcos
    alto_total = alto + 0.1 # Sumarle 10 cm por los marcos
    perimetro = 2 * (ancho_total + alto_total)
    cantidad_aluminio = perimetro * 2 # Multiplicar por 2 por las dos barras de aluminio
    area_vidrio = ancho * alto
    cantidad_vidrio = area_vidrio * cantidad

    # Calcular costos de materiales
    precio_aluminio = cantidad_aluminio * 100 # Precio por metro de aluminio
    precio_vidrio = cantidad_vidrio * 50 # Precio por metro cuadrado de vidrio
    precio_esquinas = perimetro * cantidad * 5 # Precio por unidad de esquina
    precio_chapas = cantidad * 10 # Precio por unidad de chapa

    # Calcular costo de fabricación
    costo_fabricacion = precio_aluminio + precio_vidrio + precio_esquinas + precio_chapas

    # Mostrar resultado en pantalla
    resultado.config(text="Cotización para la fabricación de {} ventanas {}: \n- Aluminio ({}) cantidad: {} m - Precio: ${}\n- Vidrio ({}) cantidad: {} m2 - Precio: ${}\n- Esquinas cantidad: {} - Precio: ${}\n- Chapas cantidad: {} - Precio: ${}\n- Costo de fabricación: ${}".format(cantidad, estilo, acabado_aluminio, cantidad_aluminio, precio_aluminio, cantidad_vidrio, precio_vidrio, cantidad * 4, precio_esquinas, cantidad, precio_chapas, costo_fabricacion))

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Cotización de Ventanas")

# Crear etiquetas y campos de entrada
tk.Label(ventana, text="Estilo de ventana: ").grid(row=0, column=0)
estilo_var = tk.StringVar()
estilo = tk.Entry(ventana, textvariable=estilo_var)
estilo.grid(row=0, column=1)

tk.Label(ventana, text="Tipo de acabado de aluminio: ").grid(row=1, column=0)
acabado_aluminio_var = tk.StringVar()
acabado_aluminio = tk.Entry(ventana, textvariable=acabado_aluminio_var)
acabado_aluminio.grid(row=1, column=1)

# Continuación del código anterior

tk.Label(ventana, text="¿Es vidrio esmerilado? ").grid(row=2, column=0)
esmerilado_var = tk.BooleanVar()
esmerilado = tk.Checkbutton(ventana, text="Sí", variable=esmerilado_var)
esmerilado.grid(row=2, column=1)

tk.Label(ventana, text="Ancho (en metros): ").grid(row=3, column=0)
ancho_var = tk.StringVar()
ancho = tk.Entry(ventana, textvariable=ancho_var)
ancho.grid(row=3, column=1)

tk.Label(ventana, text="Alto (en metros): ").grid(row=4, column=0)
alto_var = tk.StringVar()
alto = tk.Entry(ventana, textvariable=alto_var)
alto.grid(row=4, column=1)

tk.Label(ventana, text="Cantidad: ").grid(row=5, column=0)
cantidad_var = tk.StringVar()
cantidad = tk.Entry(ventana, textvariable=cantidad_var)
cantidad.grid(row=5, column=1)

# Crear botón para calcular cotización
tk.Button(ventana, text="Calcular Cotización", command=calcular_cotizacion).grid(row=6, column=0)

# Crear etiqueta para mostrar resultados
resultado = tk.Label(ventana, text="")
resultado.grid(row=7, column=0, columnspan=2)

# Iniciar bucle de eventos de la ventana
ventana.mainloop()

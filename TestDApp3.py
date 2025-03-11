import tkinter as tk  
from tkinter import messagebox  

class Prestamo:  
    def __init__(self, ingreso_mensual, deudas_mensuales, historia_pagos):  
        self.ingreso_mensual = ingreso_mensual  
        self.deudas_mensuales = deudas_mensuales  
        self.historia_pagos = historia_pagos  # "Sí" o "No"  

    def calcular_ratio_deuda_ingreso(self):  
        if self.ingreso_mensual > 0:  
            return self.deudas_mensuales / self.ingreso_mensual  
        return 0  

    def es_aptos_para_prestamo(self):  
        ratio_deuda_ingreso = self.calcular_ratio_deuda_ingreso()  

        # Criterios básicos para aprobación de préstamo  
        if self.historia_pagos.lower() == "no" and ratio_deuda_ingreso < 0.3:  
            return True  
        return False  

def verificar_prestamo():  
    try:  
        ingreso_mensual = float(entry_ingreso.get())  
        deudas_mensuales = float(entry_deudas.get())  
        historia_pagos = entry_historia.get()  

        persona = Prestamo(ingreso_mensual, deudas_mensuales, historia_pagos)  

        if persona.es_aptos_para_prestamo():  
            messagebox.showinfo("Resultado", "¡Felicidades! Usted es apto para recibir un préstamo.")  
        else:  
            messagebox.showwarning("Resultado", "Lo siento, no es apto para recibir un préstamo.")  
    except ValueError:  
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")  

# Crear ventana principal  
root = tk.Tk()  
root.title("Verificación de Préstamo")  

# Crear etiquetas y entradas  
tk.Label(root, text="Ingrese su ingreso mensual:").pack(pady=5)  
entry_ingreso = tk.Entry(root)  
entry_ingreso.pack(pady=5)  

tk.Label(root, text="Ingrese sus deudas mensuales:").pack(pady=5)  
entry_deudas = tk.Entry(root)  
entry_deudas.pack(pady=5)  

tk.Label(root, text="¿Ha tenido problemas para pagar sus deudas en el pasado? (Sí/No):").pack(pady=5)  
entry_historia = tk.Entry(root)  
entry_historia.pack(pady=5)  

# Botón para verificar el préstamo  
btn_verificar = tk.Button(root, text="Verificar Préstamo", command=verificar_prestamo)  
btn_verificar.pack(pady=20)  

# Iniciar el bucle de la interfaz  
root.mainloop()
class Prestamo:  
    def __init__(self, ingreso_mensual, deudas_mensuales, puntuacion_credito):  
        self.ingreso_mensual = ingreso_mensual  
        self.deudas_mensuales = deudas_mensuales  
        self.puntuacion_credito = puntuacion_credito  

    def calcular_ratio_deuda_ingreso(self):  
        if self.ingreso_mensual > 0:  
            return self.deudas_mensuales / self.ingreso_mensual  
        return 0  

    def es_aptos_para_prestamo(self):  
        ratio_deuda_ingreso = self.calcular_ratio_deuda_ingreso()  


# Ejemplo de uso  
def main():  
    print("Verificación de aptitud para préstamo")  

    # Input del usuario  
    ingreso_mensual = float(input("Ingrese su ingreso mensual: "))  
    deudas_mensuales = float(input("Ingrese sus deudas mensuales: "))  
  

    persona = Prestamo(ingreso_mensual, deudas_mensuales
    )  

    if persona.es_aptos_para_prestamo():  
        print("¡Felicidades! Usted es apto para recibir un préstamo.")  
    else:  
        print("Lo sentimos, no es apto para recibir un préstamo.")  

if __name__ == "__main__":  
    main()
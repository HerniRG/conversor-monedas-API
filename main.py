from funciones import *
from monedas import monedas_disponibles

def main():
    while True:
        mostrar_cabecera()
        mostrar_monedas_disponibles()
        
        try:
            moneda_origen_indice = int(input("\nElija la moneda de origen (ingrese el número correspondiente, 0 para salir): "))
            if moneda_origen_indice == 0:
                break
            
            moneda_destino_indice = int(input("Elija la moneda de destino (ingrese el número correspondiente, 0 para salir): "))
            if moneda_destino_indice == 0:
                break
            
            # Validar que los índices ingresados estén dentro del rango de la lista de monedas disponibles
            if moneda_origen_indice < 1 or moneda_origen_indice > len(monedas_disponibles) or \
               moneda_destino_indice < 1 or moneda_destino_indice > len(monedas_disponibles):
                raise ValueError("Índice de moneda no válido.")
            
            # Obtener los códigos de las monedas seleccionadas
            moneda_origen_cod = list(monedas_disponibles.keys())[moneda_origen_indice - 1]
            moneda_destino_cod = list(monedas_disponibles.keys())[moneda_destino_indice - 1]
            
            cantidad = float(input("Ingrese la cantidad a convertir: "))
            
            cantidad_convertido = convertir_monedas(cantidad, moneda_origen_cod, moneda_destino_cod)
            
            if cantidad_convertido is not None:
                print(f"\n{cantidad} {moneda_origen_cod} ({monedas_disponibles[moneda_origen_cod]}) son {cantidad_convertido:.2f} {moneda_destino_cod} ({monedas_disponibles[moneda_destino_cod]})")
            
            continuar = input("\n¿Desea hacer otra conversión? (s/n): ").lower()
            if continuar != 's':
                break
        
        except Exception:
            print("Error: La opción seleccionada no está dentro de la lista de monedas disponibles.")
            input("Presione Enter para continuar...")
            continue

if __name__ == "__main__":
    main()

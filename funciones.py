import requests
import os
from monedas import monedas_disponibles

# URL base de la API (API gratuita sin clave)
BASE_URL = "https://api.exchangerate-api.com/v4/latest/"


def limpiar_pantalla():
    # Función para limpiar la pantalla según el sistema operativo
    if os.name == 'posix':  # Linux y macOS
        _ = os.system('clear')
    else:  # Windows
        _ = os.system('cls')

def mostrar_cabecera():
    limpiar_pantalla()
    print("--- Conversor de Monedas (Online) ---\n")

def obtener_tasa_de_cambio(moneda_origen, moneda_destino):
    url = BASE_URL + moneda_origen
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code != 200:
            print("Error al obtener las tasas de cambio")
            return None
        
        tasa_de_cambio = data['rates'].get(moneda_destino)
        
        if tasa_de_cambio is None:
            print(f"No se encontró la tasa de cambio de {moneda_origen} a {moneda_destino}")
            return None
        
        return tasa_de_cambio
    
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

def convertir_monedas(cantidad, moneda_origen, moneda_destino):
    tasa_de_cambio = obtener_tasa_de_cambio(moneda_origen, moneda_destino)
    
    if tasa_de_cambio is None:
        return None
    
    cantidad_convertido = cantidad * tasa_de_cambio
    return cantidad_convertido

def mostrar_monedas_disponibles():
    print("Monedas disponibles para elegir:")
    for i, (codigo, nombre) in enumerate(monedas_disponibles.items(), start=1):
        print(f"{i}. {nombre} ({codigo})")
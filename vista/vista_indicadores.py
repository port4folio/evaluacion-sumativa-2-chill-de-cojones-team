#En esta clase lo necesario para poder hacer las consultas en en el controlador y poder registrar en él de ser necesario
import json
from controlador.indicadores_controlers import traer_indicadores
def menu_indicadores():
    print("1.- Mostrar los indicadores")
    print("0.- Salir")
    op=int(input("Ingrese una opción: "))
    return op

def mostrar_indicadores():
    indicadores=traer_indicadores()
    print('Unidad de medida: Pesos')
    for moneda, valor in indicadores.items():
        print(f"{moneda}: {valor}")

def main_indicadores():
    while True:
        op=menu_indicadores()
        if op==1:
            mostrar_indicadores()
        elif op==2:
            pass
        elif op==3:
            pass
        elif op==3:
            pass
        elif op==3:
            pass
        elif op==3:
            pass
        elif op==0:
            print("Gracias por preferirnos")
            break

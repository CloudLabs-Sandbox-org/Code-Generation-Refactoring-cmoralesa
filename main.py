"""
Calculadora Avanzada con soporte para números complejos y límites
"""
import cmath
from sympy import symbols, limit, sympify
from sympy.abc import x

def calculadora_compleja():
    """Función principal de la calculadora"""
    while True:
        print("\nCalculadora Avanzada")
        print("1. Operaciones con números complejos")
        print("2. Calcular límites")
        print("3. Salir")
        
        try:
            opcion = int(input("\nSeleccione una opción (1-3): "))
            
            if opcion == 3:
                print("¡Gracias por usar la calculadora!")
                break
                
            if opcion == 1:
                calcular_complejo()
            elif opcion == 2:
                calcular_limite()
            else:
                print("Opción no válida")
                
        except ValueError:
            print("Error: Por favor ingrese un número válido")
        except KeyboardInterrupt:
            print("\nPrograma terminado por el usuario")
            break

def obtener_complejo(mensaje):
    """Obtiene un número complejo del usuario"""
    while True:
        try:
            print(mensaje)
            real = float(input("Parte real: "))
            imag = float(input("Parte imaginaria: "))
            return complex(real, imag)
        except ValueError:
            print("Error: Ingrese números válidos")

def calcular_complejo():
    """Maneja operaciones con números complejos"""
    print("\nOperaciones con números complejos")
    print("Ingrese el primer número complejo:")
    num1 = obtener_complejo("Primer número:")
    
    print("\nIngrese el segundo número complejo:")
    num2 = obtener_complejo("Segundo número:")
    
    print("\nResultados:")
    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Multiplicación: {num1 * num2}")
    try:
        print(f"División: {num1 / num2}")
    except ZeroDivisionError:
        print("Error: División por cero")

def calcular_limite():
    """Calcula límites de funciones"""
    print("\nCálculo de límites")
    print("Ingrese la función en términos de x (ejemplo: 1/x, x**2, sin(x))")
    
    try:
        # Obtener la función
        expr_str = input("Función: ")
        expr = sympify(expr_str)
        
        # Obtener el punto para el límite
        punto = float(input("Valor al que se aproxima x: "))
        
        # Calcular el límite
        resultado = limit(expr, x, punto)
        print(f"\nEl límite de {expr_str} cuando x → {punto} es: {resultado}")
        
    except ValueError:
        print("Error: Ingrese valores numéricos válidos")
    except Exception as e:
        print(f"Error al calcular el límite: {str(e)}")

if __name__ == "__main__":
    calculadora_compleja()
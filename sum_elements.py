"""
Programa para calcular la suma de una lista de números enteros.
Solicita al usuario la cantidad de números y luego los suma.
"""

# Constantes
MAX = 100
MIN = 1

def solicitar_cantidad() -> int:
    """Solicita y valida la cantidad de números a sumar."""
    while True:
        try:
            n = int(input(f"Ingrese la cantidad de números ({MIN}-{MAX}): "))
            if MIN <= n <= MAX:
                return n
            print(f"Error: El número debe estar entre {MIN} y {MAX}")
        except ValueError:
            print("Error: Debe ingresar un número entero válido")

def solicitar_numeros(cantidad: int) -> list:
    """Solicita y valida los números a sumar."""
    numeros = []
    print(f"\nIngrese {cantidad} números enteros:")
    
    for i in range(cantidad):
        while True:
            try:
                num = int(input(f"Número {i + 1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("Error: Ingrese un número entero válido")
    return numeros

def calculate_sum(arr: list) -> int:
    """Calcula la suma de los números en la lista."""
    return sum(arr)

def main():
    """Función principal del programa."""
    try:
        # Solicitar cantidad de números
        n = solicitar_cantidad()
        
        # Solicitar los números
        numeros = solicitar_numeros(n)
        
        # Calcular y mostrar resultado
        total = calculate_sum(numeros)
        print(f"\nLa suma de los números es: {total}")
        
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario")

if __name__ == "__main__":
    main()

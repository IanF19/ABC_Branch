# Función para sumar
def suma(a, b):
    return a + b

# Función para restar
def resta(a, b):
    return a - b

# Función principal
def calculadora():
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")

    operacion = input("Ingresa el número de la operación que deseas realizar (1 o 2): ")

    # Solicitar números al usuario
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if operacion == "1":
        resultado = suma(num1, num2)
        print(f"El resultado de la suma es: {resultado}")
    elif operacion == "2":
        resultado = resta(num1, num2)
        print(f"El resultado de la resta es: {resultado}")
    else:
        print("Opción no válida.")

# Ejecutar la calculadora
calculadora()

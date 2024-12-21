
from menu_function import *


# validacion de la variable option como numero entero, not null y valor entre 1 y 7

def option_validation():
    while True:
        try:
            # Solicitar entrada del usuario y eliminar espacios en blanco
            user_input = input("Seleccione una opción (1 a 7): ").strip()
            
            # Validar si la entrada está vacía
            if not user_input:
                print("No se permite un valor vacío.")  # Mensaje de error
                continue  # Solicitar nuevamente la entrada
            
            # Convertir la entrada a un número entero
            option = int(user_input)
            
            # Validar si el número está en el rango permitido
            if 1 <= option <= 7:
                return option  # Retornar la opción válida
            print("Por favor, ingrese un número entre 1 y 7.")  # Mensaje si está fuera del rango
            
        except ValueError:
            # Manejar entradas no válidas (no convertibles a número)
            print("Tipo de dato no válido. Por favor, ingrese un número.")

# función de validación del nombre del producto
def name_validation():
    while True:
        try:
            name = input("Nombre del producto: ").strip()

            if not name:  # validar que haya un dato
                print("No se admite dato nulo. Ingrese el nombre: ")

            else:
                return name
        except ValueError:
            print("Tipo de dato no valido. Ingrese la cantidad: ")

# función para obtener la descripcion del producto
def description_validation(): 
    description = input("Descripción del producto: ").strip()
    return description


def category_validation():
    while True:
        try:
            category = input("Categoría o tipo de producto: ").strip()
            if not category:
                print("No se admite dato nulo. Ingrese la categoría: ")
            else:
                return category
        except ValueError:
            print("Tipo de dato no valido. Ingrese la cantidad: ")

        
def amount_validation():
    while True:
        try:
            amount = int(input("Cantidad del producto: ").strip())
            if not amount:
                print("No se admite dato nulo. Ingrese la cantidad: ")
            elif amount <= 0:
                print("La cantidad debe ser mayor a 0. Ingrese la cantidad: ")
            else:
                return amount

        except ValueError:
            print("Tipo de dato no valido. Ingrese la cantidad: ")


def price_validation():
    while True:
        try:
            price = float(input("Precio: ").strip())
            if not price:
                print("No se admite dato nulo. Ingrese el precio: ")
            elif price <= 0:
                print("La cantidad debe ser mayor a 0. Ingrese la cantidad: ")
            else:
                return price

        except ValueError:
            print("Tipo de dato no valido. Ingrese el precio: ")

def id_validation():
    while True:
        try:
            id = int(input("ingrese el id del producto a modificar: ").strip())
            if not id:
                print("No se admite dato nulo.")
            elif id <= 0:
                print("El id debe ser mayor a 0.")
            else:
                return id

        except ValueError:
            print("Tipo de dato no valido.")
            


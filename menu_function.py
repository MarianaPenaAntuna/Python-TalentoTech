# importacion de los otros modulos 


from db_function import *
from validation_function import *



# declaracion de las funciones 

# 1. mostrar el menú de opciones y retornar la opcion elegida

def show_option_menu():
    print(
        """
        \n------------------------------------
        \n Menú Principal 
        \n------------------------------------ 
        \n 1. Agregar producto 
        \n 2. Mostrar productos 
        \n 3. Actualizar cantidad de producto 
        \n 4. Eliminar producto 
        \n 5. Buscar producto 
        \n 6. Reporte de bajo stock 
        \n 7. Salir 
        """
        )

    option = option_validation()
    
    return option

# funcion para agregar productos, que invoca a funciones de validación de cada uno de los datos que se ingresan
def add_product():
    print("\nPor favor, ingrese los siguientes datos del producto: ")
    name = name_validation()
    description = description_validation()
    category = category_validation()
    amount = amount_validation()
    price = price_validation()
    
# creo un diccionario temporal que aun los datos de las variables para despues usarlo como parametro en la función de insertar en la base de datos
    product = {
        "name" : name,
        "description" : description,
        "category" : category,
        "amount" : amount,
        "price" : price,
    }
# llamo a la función para insertar los productos en la base de datos
    add_products_in_db(product)
    print("El producto ha sido registrado correctamente")
    
    
# declaro función para mostrar la lista de productos del inventario
def show_products():
    products_list = show_products_in_db()
    if products_list:
        print("\nEstos son los productos que se encuentran en su inventario actualmente: ")
        for product in products_list:
            print(product)
    else:
        print("No se encuentra registrado ningún producto en el inventario")

# declaro la funcion para actualizar la cantidad de producto en stock:  
def update_amount():
    print("Por favor, ingrese los siguientes datos del producto")
    id = id_validation() 
    get_product = get_product_in_db_by_id(id)
    if not get_product:
        print(f"ERROR: no se ha encontrado ningún producto con ese id")
    else:
        print(f"Producto con id {id} Cantidad actual {get_product[4]} ")
        new_amount = amount_validation()
        update_amount_in_db (id, new_amount)
        print(f"Usted ha ingresado la cantidad de {new_amount} para el producto con id {id}.\nRegistro actualizado exitosamente!")
    

def delete_product():
    id = id_validation() 
    get_product = get_product_in_db_by_id(id)
    if not get_product:
        print(f"ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        print("\nATENCION: se eliminará el siguiente registro:")
        print(get_product)
        confirmacion = input(
            "\nIngrese 's' para confirmar o cualquier otro para cancelar: "
        ).lower()
        if confirmacion == "s":
            delete_product_in_db(id)
            print(f"El registro con id {id} ha sido eliminado exitosamente!")
        else:
            print("Operación cancelada.")


def search_product():
    id = int(input("\nIngrese el id del producto que desea consultar: "))
    get_product = get_product_in_db_by_id(id)
    if not get_product:
        print(f"ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        print(get_product)


def stock_report():
    minimum_stock = int(input("\nIngrese el unmbral de mínimo stock:"))
    product_list = get_products_by_condition_in_db(minimum_stock)
    
    if not product_list:
        print(f"No se ha encontrado ningún producto con stock menor a {minimum_stock}")
    else:
        print(f"Estos son los productos con stock menor a {minimum_stock}")
        for product in product_list:
            print(product)
            
            
        
# IMPORTAMOS FUNCIONES
from db_function import *
from menu_function import *
from validation_function import *


# Declaramos la funcion principal main
def main():
    # llamo a la función de creación de base de datos para persistir los datos del inventario
    create_product_table()

    # muestro las opciones del menú en un bucle while
    while True:
        # llamo a la función que retorna la opción que eligió el usuario  y capturo el resultado en la varible option
        option = show_option_menu()
        # muestro al usuario la opción elegida
        print(f"Usted ha seleccionado la opción {option}")
        if option == 1:
            add_product()
        elif option == 2:
            show_products()
        elif option == 3:
            update_amount()
        elif option == 4:
            delete_product()
        elif option == 5:
            search_product()
        elif option == 6:
            stock_report()
        elif option == 7:
            print("\nGracias por usar nuestra App")
            break
        else:
            print("La opcion elegida es inexistente. Vuelva a intentarlo nuevamente")
            
        continuar = input("\nIngrese 's' para salir o cualquier tecla para continuar: ").lower()  # pausa para que el usuario pueda ver
        if continuar == "s":
            print("\nGracias por usar nuestra App")
            break

# ******************************************************************
# INVOCAMOS A LA FUNCION PRINCIPAL
# ******************************************************************
main()  # invocar o llamar a la funcion main()
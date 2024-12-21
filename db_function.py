# importo el modulo de base de datos para crear una base de datos
import sqlite3




# constante de la direccion de la base de datos
db_path = "inventario.db"


# funcion que crea la base de datos en caso que no exista
def create_product_table():
    try: # hacemos un intento de crear la base
        conection = sqlite3.connect(db_path) # nos conectamos a la base de datos
        print("Conexión establecida con la base de datos.")
        cursor = conection.cursor() # dirijimos la conexion a la tabla de productos
      
        # ejecutamos la query de creacion de la tabla con las características de cada campo
        cursor.execute("""CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                category TEXT NOT NULL,
                amount INTEGER NOT NULL,
                price REAL NOT NULL)"""
        )
        conection.commit() # enviamos los datos a la db
        
    except sqlite3.Error as e: # si el intento de crear la base no funciona, capturamos el error
        print(f"Error al crear la tabla: {e}")
        
    finally: # cerramos la conexion con la base de datos
        conection.close()

# creamos una función para agregar un producto a la base de datos        
def add_products_in_db(product):
    try: 
        conection = sqlite3.connect(db_path)
        cursor = conection.cursor()
        query = "INSERT INTO products (name, description, category, amount, price) VALUES (?,?,?,?,?)"
        placeholders = (
        product["name"],
        product["description"],
        product["category"],
        product["amount"],
        product["price"],
        )
        cursor.execute(query, placeholders)
        conection.commit()
        
    except sqlite3.Error as e: # si el intento de agregar un producto en la tabla no funciona, capturamos el error
        print(f"Error al insertar el producto en la tabla: {e}")
        
    finally: # cerramos la conexion con la base de datos
        conection.close()
        
# declaramos una función para traernos los datos de la base de datos
def show_products_in_db():
    try: 
        conection = sqlite3.connect(db_path)
        cursor = conection.cursor()
        query = "SELECT * FROM products"
        cursor.execute(query)
        products_list = cursor.fetchall()
        
    except sqlite3.Error as e: # si el intento de mostrar el inventario no funciona, capturamos el error
        print(f"Error al mostrar el inventario: {e}")
        
    finally: # cerramos la conexion con la base de datos y retornamos el valor de la lista de tuplas
        conection.close()
        return products_list

def get_product_in_db_by_id(id):
    try: 
        conection = sqlite3.connect(db_path)
        cursor = conection.cursor()
        query = "SELECT * FROM products WHERE id=?"
        placeholders =(id, )
        cursor.execute(query, placeholders)
        product = cursor.fetchone()
        
    except sqlite3.Error as e: # si el intento de traer el producto no funciona, capturamos el error
            print(f"Error al buscar el producto en el inventario: {e}")
            
    finally: # cerramos la conexion con la base de datos y retornamos el producto
        conection.close()
        return product   
   
     
def update_amount_in_db (id, new_amount):
    try:
        conection = sqlite3.connect(db_path)
        cursor = conection.cursor()
        query = "UPDATE products SET amount = ? WHERE id = ?"
        placeholders = (new_amount, id)
        cursor.execute(query, placeholders)
        conection.commit()
    except sqlite3.Error as e: # si el intento de actualizar el producto no funciona, capturamos el error
            print(f"Error al buscar el producto en el inventario: {e}")
            
    finally: # cerramos la conexion con la base de datos
        conection.close()

def delete_product_in_db(id):
    try:
        conection = sqlite3.connect(db_path)
        cursor = conection.cursor()
        query = "DELETE FROM products WHERE id= ?"
        placeholders = (id, )
        cursor.execute(query, placeholders)
        conection.commit()
        
    except sqlite3.Error as e: # si el intento de eliminar el producto no funciona, capturamos el error
            print(f"Error al borrar el producto del inventario: {e}")
            
    finally: # cerramos la conexion con la base de datos
        conection.close()   

def get_products_by_condition_in_db(minimum_stock):
    
        conection = sqlite3.connect(db_path)
        cursor = conection.cursor()
        query = "SELECT * FROM products WHERE amount < ? "
        placeholders = (minimum_stock, )
        cursor.execute(query, placeholders)
        product_list = cursor.fetchall()
        
        return product_list
"""
    except sqlite3.Error as e: # si el intento de buscar los productos no funciona, capturamos el error
            print(f"Error al buscar el producto en el inventario: {e}")
            
    finally: # cerramos la conexion con la base de datos 
        conection.close()
"""
    
        




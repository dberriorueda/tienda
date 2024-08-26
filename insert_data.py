import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

# Insertar productos de prueba
cursor.execute("INSERT INTO products (name, description, price, quantity) VALUES ('Producto1', 'Descripción del producto 1', 100.00, 10)")
cursor.execute("INSERT INTO products (name, description, price, quantity) VALUES ('Producto2', 'Descripción del producto 2', 150.00, 20)")

# Insertar clientes de prueba
cursor.execute("INSERT INTO clients (name, email, phone, address) VALUES ('Cliente1', 'cliente1@example.com', '123456789', 'Ubicación1')")
cursor.execute("INSERT INTO clients (name, email, phone, address) VALUES ('Cliente2', 'cliente2@example.com', '987654321', 'Ubicación2')")

# Confirmar cambios y cerrar conexión
conn.commit()
conn.close()

print("Datos de prueba insertados en la base de datos.")



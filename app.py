from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='db_tienda'
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_client', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO clientes (nombre, email, telefono, direccion) VALUES (%s, %s, %s, %s)', 
                           (name, email, phone, address))
            conn.commit()
        except Exception as e:
            print(f'Error al agregar cliente: {e}')
        finally:
            cursor.close()
            conn.close()
        
        return redirect(url_for('index'))
    
    return render_template('add_client.html')

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form.get('product_name')
        description = request.form.get('product_description')
        try:
            price = float(request.form.get('product_price'))
            quantity = int(request.form.get('product_quantity'))
        except (ValueError, TypeError) as e:
            print(f"Error en la conversión de datos: {e}")
            return "Error en los datos del producto", 400
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO productos (nombre, descripcion, precio, cantidad) VALUES (%s, %s, %s, %s)', 
                           (name, description, price, quantity))
            conn.commit()
        except Exception as e:
            print(f'Error al agregar producto: {e}')
            return "Error al agregar el producto", 500
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('list_products'))
    
    return render_template('add_product.html')

@app.route('/list_products')
def list_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos')
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('list_products.html', products=products)

@app.route('/list_clients')
def list_clients():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    clients = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('list_clients.html', clients=clients)


if __name__ == '__main__':
    app.run(debug=True)




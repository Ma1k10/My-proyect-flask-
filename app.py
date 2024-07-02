import requests

from flask import (
    Flask, 
    render_template,
    redirect,
    request,
)

app = Flask(__name__)

lista_productos = []

@app.route('/')
def index():
    return render_template(
        'index.html',
    )

@app.route('/productos')
def productos():
    return render_template(
        'productos.html',
        lista_productos = lista_productos,
    )

@app.route('/add_productos', methods=['POST', 'GET'])
def add_producto():
    if request.method == 'POST':
        codigo = request.form['codigo']
        descripcion = request.form['descripcion']
        stock = request.form['stock']
        precio = request.form['precio']

        producto = dict(
            codigo = codigo,
            descripcion = descripcion,
            stock = stock,
            precio = precio,
        )
        lista_productos.append(producto)
        return redirect('productos')
    return render_template(
        'add_productos.html',
    )
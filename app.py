from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy
import strawberry
from strawberry.flask.views import GraphQLView
from models import db
from schema import Query, Mutation

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping_cart.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

schema = strawberry.Schema(query=Query, mutation=Mutation)

# Actualiza la configuración de la vista
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql_view",
        schema=schema,
        graphiql=True  # Asegúrate de que esto esté en True
    )
)

with app.app_context():
    db.create_all()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>API de Carrito de Compras - GraphQL</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            max-width: 800px; 
            margin: 0 auto; 
            padding: 20px;
        }
        pre { 
            background: #f4f4f4; 
            padding: 15px; 
            border-radius: 5px; 
        }
        h1, h2 { color: #333; }
        .endpoint {
            background: #e9ecef;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <h1>Bienvenido a la API de Carrito de Compras</h1>
    <p>Esta es una API simple para gestionar un carrito de compras utilizando GraphQL.</p>
    
    <div class="endpoint">
        <strong>Endpoint GraphQL:</strong> <a href="/graphql">/graphql</a>
    </div>

    <h2>Consultas</h2>
    <h3>Obtener todos los carritos:</h3>
    <pre>
query {
    carts {
        id
        name
        price
        quantity
        createdAt
        updatedAt
    }
}</pre>

    <h3>Obtener un carrito específico:</h3>
    <pre>
query {
    cart(cartId: 1) {
        id
        name
        price
        quantity
        createdAt
        updatedAt
    }
}</pre>

    <h2>Mutaciones</h2>
    <h3>Crear un nuevo carrito:</h3>
    <pre>
mutation {
    createCart(cartData: {
        name: "Producto 1"
        price: 99.99
        quantity: 2
    }) {
        id
        name
        price
        quantity
        createdAt
        updatedAt
    }
}</pre>

    <h3>Actualizar un carrito existente:</h3>
    <pre>
mutation {
    updateCart(
        cartId: 1
        cartData: {
            name: "Producto Actualizado"
            price: 149.99
            quantity: 3
        }
    ) {
        id
        name
        price
        quantity
        updatedAt
    }
}</pre>

    <h3>Eliminar un carrito:</h3>
    <pre>
mutation {
    deleteCart(cartId: 1)
}</pre>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
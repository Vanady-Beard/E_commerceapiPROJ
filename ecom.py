from flask import Flask, request, jsonify, render_template
from datetime import datetime
from connection import db, app  
from customer import Customer, CustomerAccount, Product, Order, customer_schema, customers_schema, account_schema, accounts_schema, product_schema, products_schema, order_schema, orders_schema

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/create_account", methods=["POST"])
def add_customer():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"message": "No input data provided"}), 400
        new_customer = Customer(
            name=data['name'],
            email=data['email'],
            phone=data['phone']
        )
        db.session.add(new_customer)
        db.session.commit()

        new_account = CustomerAccount(
            customerID=new_customer.customerID,
            username=data['username'],
            password=data['password']
        )
        db.session.add(new_account)
        db.session.commit()

        return account_schema.jsonify(new_account), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400

@app.route("/customers", methods=["GET"])
def get_customers():
    try:
        customers = Customer.query.all()
        return customers_schema.jsonify(customers), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.route("/products", methods=["POST"])
def add_product():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"message": "No input data provided"}), 400
        new_product = Product(
            name=data['name'],
            price=data['price']
        )
        db.session.add(new_product)
        db.session.commit()
        return product_schema.jsonify(new_product), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400

@app.route("/products", methods=["GET"])
def get_products():
    try:
        products = Product.query.all()
        return products_schema.jsonify(products), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.route("/order", methods=["POST"])
def place_order():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"message": "No input data provided"}), 400
        new_order = Order(
            customerID=data['customerID'],
            orderDate=datetime.utcnow(),
            totalAmount=data['totalAmount']
        )
        db.session.add(new_order)
        db.session.commit()
        return order_schema.jsonify(new_order), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400

@app.route("/orders", methods=["GET"])
def get_orders():
    try:
        orders = Order.query.all()
        return orders_schema.jsonify(orders), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)


from connection import db 
from flask_marshmallow import Marshmallow
from marshmallow import fields

ma = Marshmallow()

class Customer(db.Model):
    __tablename__ = "Customer"
    customerID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=True)

class CustomerAccount(db.Model):
    __tablename__ = 'CustomerAccount'
    accountID = db.Column(db.Integer, primary_key=True)
    customerID = db.Column(db.Integer, db.ForeignKey('Customer.customerID'), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    customer = db.relationship('Customer', backref='account')

class Product(db.Model):
    __tablename__ = 'Product'
    productID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Order(db.Model):
    __tablename__ = 'Order'
    orderID = db.Column(db.Integer, primary_key=True)
    customerID = db.Column(db.Integer, db.ForeignKey('Customer.customerID'), nullable=False)
    orderDate = db.Column(db.DateTime, nullable=False)
    totalAmount = db.Column(db.Float, nullable=False)
    customer = db.relationship('Customer', backref='orders')

class CustomerSchema(ma.Schema):
    customerID = fields.Integer()
    name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

class CustomerAccountSchema(ma.Schema):
    accountID = fields.Integer()
    customerID = fields.Integer()
    username = fields.String(required=True)
    password = fields.String(required=True)

account_schema = CustomerAccountSchema()
accounts_schema = CustomerAccountSchema(many=True)

class ProductSchema(ma.Schema):
    productID = fields.Integer()
    name = fields.String(required=True)
    price = fields.Float(required=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

class OrderSchema(ma.Schema):
    orderID = fields.Integer()
    customerID = fields.Integer()
    orderDate = fields.DateTime()
    totalAmount = fields.Float()

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)





























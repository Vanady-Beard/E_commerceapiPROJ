
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import mysql.connector
# from mysql.connector import Error



# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:newyork12@localhost/e_commerce_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# def get_db():
#     return db  


# def connect_database():
#     data_name = "e_commerce_db"
#     user = "root"
#     password = "newyork12"
#     host = "localhost"

#     try:
#         c = mysql.connector.connect(
#             database=data_name,
#             user=user,
#             password=password,
#             host=host
#     )
        
#         if c.is_connected ():
#             print("Connected to MySQL Database successfully")
#             return c
    
    
#     except Error as e:
#        print(f"Error: {e}")
      


# def get_db():
#    return db

#     finally:
#        if c and c.is_connected():
#           c.close()
#           print("Mysql connection is closed.")
# get_db()


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:newyork12@localhost/e_commerce_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


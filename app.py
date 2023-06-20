from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api, Resource
from marshmallow import post_load, fields, ValidationError
from dotenv import load_dotenv
from os import environ

load_dotenv()

# Create App instance
app = Flask(__name__)

# Add DB URI from .env
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')

# Registering App w/ Services
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
CORS(app)
Migrate(app, db)

# Models
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    inventory_quantity = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f"{self.name} {self.description} {self.price} {self.inventory_quantity}"

# Schemas
class ProductSchema(ma.Schema):
    id = fields.Integer(primary_key=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    price = fields.Float(required=True)
    inventory_quantity = fields.Integer(required=True)
    class Meta:
        fields = ("id", "name", "description", "price", "inventory_quantity")

    @post_load
    def create_product(self, data, **kwargs):
        return Products(**data)
    
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Resources



# Routes

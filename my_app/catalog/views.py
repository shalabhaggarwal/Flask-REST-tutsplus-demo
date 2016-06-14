from flask import Blueprint
from my_app import manager
from my_app.catalog.models import Product

catalog = Blueprint('catalog', __name__)

@catalog.route('/')
@catalog.route('/home')
def home():
    return "Welcome to the Catalog Home."


manager.create_api(Product, methods=['GET', 'POST'])

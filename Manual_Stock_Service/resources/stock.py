from datetime import datetime

from flask import jsonify
from daos.bar_sale_dao import Bar_sale_DAO
from daos.user_dao import UserDAO
from daos.product_dao import Product_DAO
from db import Session


class Stock:
    @staticmethod
    def update(d_id, new_stock):
        session = Session()
        Product = session.query(Product_DAO).filter(Product_DAO.id == int(d_id))[0]
        Product.stock.stock = new_stock
        Product.stock.last_update = datetime.datetime.now()
        session.commit()
        return jsonify({'message': 'The stock position was updated'}), 200

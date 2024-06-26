import time
time.sleep(5)
import logging
import os
from flask import Flask, request
from resources.stock import Stock
from db import Base, engine

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
Base.metadata.create_all(engine)

@app.route('/product/<d_id>/stock', methods=['PUT'])
def update_delivery_status(d_id):
    stock = request.get_json()
    return Stock.update(d_id, stock)

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0')
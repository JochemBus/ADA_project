from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from daos.stock_dao import StockDAO
from db import Base


class Product_DAO(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)  # Auto generated primary key
    name = Column(String)
    price = Column(String)
    # reference to status as foreign key relationship. This will be automatically assigned.
    stock_id = Column(Integer, ForeignKey('stock.id'))
    # https: // docs.sqlalchemy.org / en / 14 / orm / basic_relationships.html
    # https: // docs.sqlalchemy.org / en / 14 / orm / backref.html
    stock = relationship(StockDAO.__name__, backref=backref("product", uselist=False))

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

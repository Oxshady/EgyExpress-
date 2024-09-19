from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base import base
from models.tracking import Tracking
from models.Category import Category
from models.Discount import Discount
from models.Comb import VaiationCombination
from models.variationsKey import VaiationKey
from models.variationsValue import VaiationValue
from models.Product import Product
from models.subCategory import Subcategory
from models.order_item import OrderItem
from models.Order import Order
from models.Payment import Payment
from models.CartItem import CartItem
from models.Cart import Cart
from models.Review import Review
from models.users import User

mapp = {
    "Category": Category,
    "Subcategory": Subcategory,
    "Discount": Discount,
    "VaiationCombination": VaiationCombination,
    "VaiationKey": VaiationKey,
    "VaiationValue": VaiationValue,
    "Product": Product,
    "OrderItem": OrderItem,
    "Order": Order,
    "Payment": Payment,
    "CartItem": CartItem,
    "Cart": Cart,
    "Review": Review,
    "User": User,
}

class DBstorage:
    __engine = None
    __session = None

    def __init__(self):
        db = "sh"
        user = "shadi"
        passwd = "1"
        host = "localhost"
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, passwd, host, db),
            pool_pre_ping=True,
            pool_size=10,
            max_overflow=20,
            pool_timeout=30
        )

    def setup(self):
        base.metadata.create_all(self.__engine)
        sfactory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(sfactory)

    def filter_group(self, cls, **kwargs):
        if str(cls) in mapp:
            return self.__session.query(mapp[str(cls)]).filter_by(**kwargs).all()

    def filter_one(self, cls, **kwargs):
        if str(cls) in mapp:
            return self.__session.query(mapp[str(cls)]).filter_by(**kwargs).first()

    def post(self, obj):
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        self.__session.commit()
    
    def roll(self):
        self.__session.rollback()

    def get_all(self, cls):
        if str(cls) in mapp:
            return self.__session.query(mapp[str(cls)]).all()
        else:
            return []

    def delete(self, obj):
        self.__session.delete(obj)
        self.__session.commit()

    def get(self, cls, id):
        if str(cls) in mapp:
            return self.__session.query(mapp[str(cls)]).get(id)
        else:
            return None

    def close(self):
        self.__session.remove()

    def get_session(self):
        return self.__session

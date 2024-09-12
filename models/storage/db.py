from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base import base


class DBstorage:
    __engine = None
    __session = None

    def __init__(self):
        db = "Egy"
        user = "shadi"
        passwd = "1"
        host = "localhost"
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, passwd, host, db),
            pool_pre_ping=True,
        )

    def setup(self):
        from models.tracking import Tracking
        from models.Category import Category
        from models.Discount import Discount
        from models.Comb import VaiationCombination
        from models.variationsKey import VaiationKey
        from models.variationsValue import VaiationValue
        from models.Product import Product
        from models.order_item import OrderItem
        from models.Order import Order
        from models.Payment import Payment
        from models.CartItem import CartItem
        from models.Cart import Cart
        from models.Review import Review
        from models.users import User
        base.metadata.create_all(self.__engine)
        sfactory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(sfactory)
        print("hi")
        self.__session = session()

    def close(self):
        self.__session.remove()

    def get_session(self):
        return self.__session

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base import base


class DBstorage:
    __engine = None
    __session = None

    def __init__(self):
        db = "egye"
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
        from models.subCategory import Subcategory
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
        self.__session = session()

    def post(self, obj):
        self.__session.add(obj)
        self.__session.commit()
    
    def get_all(self, cls):
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
        if str(cls) in mapp:
            return self.__session.query(mapp[str(cls)]).all()
        else:
            return []
    
    def delete(self, obj):
        self.__session.delete(obj)
        self.__session.commit()
    def get(self, cls, id):
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
        if str(cls) in mapp:
            return self.__session.query(mapp[str(cls)]).get(id)
        else:
            return None
        
    def close(self):
        self.__session.remove()

    def get_session(self):
        return self.__session

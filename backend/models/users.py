from models.base import BaseModel, base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref
from typing import List
from bcrypt import hashpw, gensalt,checkpw
class User(BaseModel, base):
    """User class"""

    __tablename__ = "users"
    first_name: Mapped["str"] = mapped_column(String(50), nullable=False)
    last_name: Mapped["str"] = mapped_column(String(50), nullable=False)
    phoneNumber: Mapped["str"] = mapped_column(String(50), nullable=False)
    address: Mapped["str"] = mapped_column(String(100), nullable=False)
    email: Mapped["str"] = mapped_column(String(60), nullable=False)
    password: Mapped["str"] = mapped_column(String(60), nullable=False)
    from models.tracking import Tracking

    tracking: Mapped[List["Tracking"]] = relationship(Tracking, backref="user", cascade='all, delete-orphan')
    from models.Order import Order
    order: Mapped[List["Order"]] = relationship(Order, backref="user", cascade='all, delete-orphan')
    from models.Payment import Payment
    payment: Mapped[List["Payment"]] = relationship(Payment, backref="user", cascade='all, delete-orphan')
    from models.Cart import Cart
    cart: Mapped["Cart"] = relationship(Cart, uselist=False, backref=backref("user", uselist=False), cascade="all, delete-orphan")
    from models.Review import Review
    review: Mapped[List["Review"]] = relationship(Review, backref="user", cascade='all, delete-orphan')
    def __init__(self, *args, **kwargs) -> None:
        """Initialize a new User object"""
        super().__init__(*args, **kwargs)
        for key, value in kwargs.items():
            if key == "password":
                value = self.hash_password(value)
            setattr(self, key, value)

    def hash_password(self, password: str) -> str:
        """Hash password"""
        salt = gensalt()
        passwd = hashpw(password.encode('utf-8'), salt)
        return passwd.decode('utf-8')
    
    def check_password(self, password: str) -> bool:
        """Check password"""
        return checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

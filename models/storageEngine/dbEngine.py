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
        from models.users import User

        base.metadata.create_all(self.__engine)
        sfactory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(sfactory)
        self.__session = session()

    def close(self):
        self.__session.remove()

    def get_session(self):
        return self.__session

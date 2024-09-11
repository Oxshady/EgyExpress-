from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class DBstorage:
    __engine = None
    __session = None

    def __init__(self):
        db = 'hbnb_dev'
        user = 'hbnb_dev'
        passwd = 'hbnb_dev_pwd'
        host = 'localhost'
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user,
                passwd,
                host,
                db),
            pool_pre_ping=True
            )
    def setup(self):
        sfactory = sessionmaker(bind=self.__engine, expire_on_commit = False)
        session = scoped_session(sfactory)
        self.__session = session()
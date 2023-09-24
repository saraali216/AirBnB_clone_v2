#!/usr/bin/python3
"""class for SQLAlchemy"""

from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from os import getenv


class DBStorage:
    """Create tables in the environment"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary __object
        """
        dic = {}
        if cls is None:
            for cl in [State, City, User, Place, Review, Amenity]:
                objs = self.__session.query(cl).all()
                for obj in objs:
                    k = obj.__class__.__name__ + '.' + obj.id
                    dic[k] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                k = obj.__class__.__name__ + '.' + obj.id
                dic[k] = obj
        return dic

    def new(self, obj):
        """Add a new object to the table"""
        self.__session.add(obj)

    def save(self):
        """Saves all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from the table"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloading session"""
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """Close"""
        self.__session.close()

from mongoengine import Document, IntField, StringField, connect
from mongoengine import get_db as get_mongo_db

from natural_loader import (
    MONGO_ATLAS_HOST,
    MONGO_ATLAS_PW,
    MONGO_ATLAS_URI,
    MONGO_ATLAS_USER,
)


class DB:
    def __init__(self):
        self.db_uri = MONGO_ATLAS_URI
        self.db_host = MONGO_ATLAS_HOST
        self.db_user = MONGO_ATLAS_USER
        self.db_pw = MONGO_ATLAS_PW
        self.connect()

    def connect(self):
        connect(host=self.db_uri)
        # connect(db="JaN", host=self.db_host, username=self.db_user, password=self.db_pw)


def get_db():
    return DB()


class Test(Document):
    name = StringField()
    age = IntField()


if __name__ == "__main__":
    db = get_db()
    print(get_mongo_db())
    p = Test(name="John", age=25)
    p.save()

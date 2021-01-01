from typing import List
from tinydb import TinyDB, Query

db = TinyDB('db.json')


def add(m: dict):
    db.insert(m)


def get_all() -> List[dict]:
    return db.all()


def query():
    ...


def update(m, h):
    Item = Query()
    db.update(m, Item.hash == h)


def remove(h):
    Item = Query()
    db.remove(Item.hash == h)

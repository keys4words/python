import sqlite3, random
from datetime import datetime as dt

class UsersDB:
    __instance = None

    @staticmethod
    def get_instance():
        if UsersDB.__instance is None:
            UsersDB()
        return UsersDB.__instance

    def __init__(self):
        if UsersDB.__instance is not None:
            raise Exception("You're doing it wrong, don't do it!")
        else:
            self.con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
            self.init_db()
            UsersDB.__instance = self


#!/usr/bin/python3
import sqlite3
from typing import Tuple


class DBHelper():
    def __init__(self, db_path: str) -> None:
        self.path = db_path
        self.init_db()

    def init_db(self) -> bool:
        """ Create and initialize database
            database_path: a relative path to the database folder, including the filename
            Returns a boolean.
            True: Successfully completed the initialization
            False: Encountered an error. Details will be in the log file
        """
        con = sqlite3.connect(database=f"{self.path}")
        cur = con.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS 'recipes' (
                        'id'	TEXT NOT NULL UNIQUE,
                        'name'	TEXT,
                        'ingredients'	TEXT,
                        'cuisine'	TEXT,
                        'meal'	TEXT,
                        PRIMARY KEY('id')
                    );
                    """)
        cur.close()
        con.close()
        return True

    def execute_db(self, command: str, args: Tuple) -> list:
        """ get and open a database cursor """
        con = sqlite3.connect(database=f"{self.path}")
        cur = con.cursor()
        # TODO: clean up the input
        cur.execute(command, args)
        result = cur.fetchall()
        con.commit()
        cur.close()
        con.close()
        return result

    def close_db(self):
        con = sqlite3.connect(database=f"{self.path}")
        cur = con.cursor()
        cur.execute("DROP TABLE recipes")
        cur.close()
        con.close()




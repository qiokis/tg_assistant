import os
from typing import List
import sqlite3


class Database:

    _path = os.environ['DB_PATH']

    @staticmethod
    def _exec_query(query: str):
        operation = query.split(' ')[0].upper()
        with sqlite3.connect(Database._path) as conn:
            cursor = conn.cursor()
            if operation in ['INSERT', 'DELETE', 'UPDATE']:
                cursor.execute(query)
                print(query)
                conn.commit()
            elif operation in ['SELECT']:
                result = cursor.execute(query)
                return result.fetchall()

    @staticmethod
    def get_films() -> List[dict]:
        result = Database._exec_query('Select * from film;')
        return [{'id': row[0], 'name': row[1], 'viewed': '1' if bool(row[2]) else ''} for row in result]

    @staticmethod
    def change_film(film_id: int, field: str, new_value: str or bool):
        Database._exec_query(f'Update film set {field}={new_value} where id={film_id}')



    @staticmethod
    def get_books():
        result = Database._exec_query('Select * from book;')
        return [{'name': row[1], 'page': row[2], 'read': bool(row[3])} for row in result]

if __name__ == '__main__':
    print(Database.get_books())
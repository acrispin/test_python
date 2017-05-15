"""
https://dev.to/mistermocha/python-unit-testing-with-mock---part-two
http://stackoverflow.com/questions/38657566/detect-whether-to-fetch-from-psycopg2-cursor-or-not

create table in postgresql:
CREATE TABLE IF NOT EXISTS mytable(mystring VARCHAR);

usar con psycopg2=2.7
$ sudo pip install psycopg2==2.7.1

"""

import sys
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '12345678'
DATABASE = 'basedb'
PORT = 5432

class DBWriter(object):
    counter = 0 # like static method

    def __init__(self):
        sql = "CREATE TABLE IF NOT EXISTS mytable(mystring VARCHAR);"
        self.db = DBLibrary()
        self.counter = 0
        self.commit_to_db(sql, True)
        DBWriter.counter += 1

    def commit_to_db(self, sql, flag_create_table=False):
        if not flag_create_table:
            self.counter += 1
        return self.db.commit(sql)

    def save(self, string):
        sql = "INSERT INTO mytable VALUES ('{}')".format(string)
        return self.commit_to_db(sql)

    def drop(self, string):
        sql = "DELETE FROM mytable WHERE mystring = '{}'".format(string)
        return self.commit_to_db(sql)

    def read(self, string=None):
        sql = "SELECT * FROM mytable"
        if string:
            sql = "SELECT * FROM mytable WHERE mystring = '{}'".format(string)
        return self.commit_to_db(sql)


class DBLibrary(object):

    def __init__(self):
        pass

    def commit(self, _sql):
        print("DBLibrary commit")
        tpl = None
        with DBHelper() as conn:
            with conn:
                with conn.cursor() as cur:
                    rowcount, data, query = 0, None, ''
                    cur.execute(_sql)
                    if cur.description: # came from a select
                        data = cur.fetchall()
                    rowcount, query = cur.rowcount, cur.query
                    tpl = (rowcount, data, query)
        if not tpl:
            tpl = (0, None, '')
        return tpl


class DBHelper(object):

    def __init__(self):
        print("DBHelper open")
        self.conn = self.open()

    def open(self):
        try:
            conn = psycopg2.connect( host=HOSTNAME,
                                     user=USERNAME,
                                     password=PASSWORD,
                                     dbname=DATABASE,
                                     port=PORT )
        except Exception as e:
            print('Error to connet: ', e)
            print('Saliendo del programa')
            sys.exit(0)
        return conn

    def close(self):
        if self.conn:
            self.conn.close()

    def __enter__(self):
        print("DBHelper return conn")
        # return connection
        return self.conn

    def __exit__(self, type, value, traceback):
        print("DBHelper close")
        self.close()


if __name__ == '__main__':
    db = DBWriter()
    db2 = DBWriter()

    print(db.save("texto1"))
    # print(db.save("texto2"))
    # print(db.save("texto3"))
    print(db.read())
    print(db2.read("texto1"))
    print(db.drop("texto1"))
    # print(db.drop("texto2"))
    # print(db.drop("texto3"))

    print("Objetos creados de DBWriter", DBWriter.counter)
    print("Llamadas de db", db.counter)
    print("Llamadas de db2", db2.counter)

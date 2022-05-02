import sqlite3
from datetime import datetime


class DatabaseHandler:
    connection = sqlite3.connect('./CinemaBookingSystem.db')
    cursor = connection.cursor()

    def __init__(self):
        self.create_tables()
        self.insert_data_to_tables_for_start()

    def create_tables(self):
        # make database and users (if not exists already) table at programe start up

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at DATE ,
        user_name TEXT NOT NULL ,
        password TEXT NOT NULL
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at DATE ,
        first_name TEXT NOT NULL ,
        last_name TEXT NOT NULL,
        mobile TEXT ,
        email TEXT
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS salons (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at DATE ,
        salon_name TEXT NOT NULL ,
        capicity TEXT NOT NULL,
        price integer 
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at DATE ,
        movie_name TEXT NOT NULL ,
        genre TEXT NOT NULL,
        age_limit TEXT NOT NULL ,
        price INTEGER NOT NULL 
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS shop (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at DATE ,
        product_name TEXT NOT NULL ,
        price TEXT NOT NULL
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at DATE ,
        user_id INTEGER NOT NULL ,
        salon_id INTEGER NOT NULL,
        movie_id INTEGER NOT NULL,
        premiere_day DATE ,
        premiere_time TIMESTAMP ,
        chair_id Text, 
        shop_id TEXT,
        price TEXT NOT NULL
        )
        ''')

        self.connection.commit()

    def insert_data_to_tables_for_start(self):
        result = self.check_data_exist('movies')
        if not result:
            movies_insert = 'INSERT INTO movies(created_at, movie_name, genre, age_limit, price) VALUES(?,?,?,?,?)'
            movie_list = [(datetime.now(), 'Matrix', 'Action', '+18', 100),
                          (datetime.now(), 'TENET', 'Action', '+13', 110),
                          (datetime.now(), 'Ice Age', 'Animation', '+7', 120),
                          (datetime.now(), 'Mask', 'Comedy', '+13', 150)]
            self.cursor.executemany(movies_insert, movie_list)
        result = self.check_data_exist('salons')
        if not result:
            salon_insert = 'INSERT INTO salons(created_at, salon_name, capicity, price) VALUES(?,?,?,?)'
            salon_list = [(datetime.now(), 'Winter', 35, 100),
                          (datetime.now(), 'Summer', 45, 110),
                          (datetime.now(), 'Spring', 55, 120)]
            self.cursor.executemany(salon_insert, salon_list)
        self.connection.commit()

    def check_data_exist(self, table_name):
        query = (f'SELECT * FROM {table_name}')
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result:
            return True
        else:
            return False

    def check_user_exist(self, username, password):
        find_user = ('SELECT * FROM user WHERE user_name = ? and password = ?')
        self.cursor.execute(find_user, [username, password])
        result = self.cursor.fetchall()
        if result:
            return True
        else:
            return False

    def check_user_exist_by_username(self, username):
        find_user = ('SELECT * FROM user WHERE user_name = ?')
        self.cursor.execute(find_user, [username])
        result = self.cursor.fetchall()
        if result:
            return True
        else:
            return False

    def insert_new_user(self, username, password):
        insert = 'INSERT INTO user(created_at, user_name,password) VALUES(?,?,?)'
        self.cursor.execute(insert, [datetime.now(), username, password])
        self.connection.commit()

    def get_all_salons(self):
        all_salons_query = ('SELECT * FROM salons ')
        self.cursor.execute(all_salons_query)
        result = self.cursor.fetchall()
        if result:
            return result
        else:
            return False

    def get_all_movies(self):
        all_movies = ('SELECT * FROM movies ')
        self.cursor.execute(all_movies)
        result = self.cursor.fetchall()
        if result:
            return result
        else:
            return False

    def get_movie_price(self, movie):
        price = ('SELECT price FROM movies  WHERE movie_name = ? ')
        self.cursor.execute(price, [movie])
        result = self.cursor.fetchall()
        if result:
            return result[0][0]
        else:
            return False

import os
import sqlite3

con = sqlite3.connect(r'uploaded_files' + os.sep + 'assortment.db')

"""
Создание новых таблиц
"""


def close_connection():
    if con:
        con.close()
        print("Соединение с SQLite закрыто")


def create_table_warehouse_addresses():
    """
    Создание таблицы с адресами и контактами складов
    :return:
    """
    try:
        with con:
            con.execute("""
            CREATE TABLE WAREHOUSE_ADDRESSES (
                identifier TEXT,
                name TEXT,
                city TEXT,
                phone TEXT,
                site TEXT,
                email TEXT,
                address TEXT
            );
        """)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def create_table_tire_assortment():
    """
    Создание таблицы с ассортиментом шин
    :return:
    """
    try:
        with con:
            con.execute("""
            CREATE TABLE TIRE_ASSORTMENT (
                code TEXT,
                p_full_name TEXT,
                p_brand TEXT,
                p_model TEXT,
                p_width TEXT,
                p_height TEXT,
                p_diameter TEXT,
                p_load_index TEXT,
                p_speed_index TEXT,
                p_season TEXT,
                p_category TEXT,
                p_xl TEXT,
                p_protection TEXT,
                p_omologation TEXT,
                p_side TEXT,
                p_mud_terrain TEXT,
                p_all_terrain TEXT,
                p_cargo TEXT,
                p_thorn TEXT,
                p_runflat TEXT,
                p_axis TEXT,
                p_layering TEXT,
                p_appointment TEXT,
                p_photo_last_modified TEXT,
                p_info_last_modified TEXT,
                p_photo TEXT,
                p_shipping_weight TEXT,
                p_shipping_volume TEXT,
                p_shipping_length TEXT,
                p_shipping_width TEXT,
                p_shipping_height TEXT,
                p_completeness TEXT,
                p_design TEXT,
                p_can_thorn TEXT
            );
        """)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def create_table_wheels_assortment():
    """
    Создание таблицы с ассортиментом дисков
    :return:
    """
    try:
        with con:
            con.execute("""
            CREATE TABLE WHEELS_ASSORTMENT (
                code TEXT,
                p_full_name TEXT,
                p_brand TEXT,
                p_model TEXT,
                p_color TEXT,
                p_width TEXT,
                p_diameter TEXT,
                p_bolts_count TEXT,
                p_bolts_space TEXT,
                p_pcd TEXT,
                p_et TEXT,
                p_dia TEXT,
                p_type TEXT,
                p_photo_last_modified TEXT,
                p_info_last_modified TEXT,
                p_photo TEXT,
                p_shipping_weight TEXT,
                p_shipping_volume TEXT,
                p_shipping_length TEXT,
                p_shipping_width TEXT,
                p_shipping_height TEXT
            );
        """)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def create_table_tire_remnants():
    """
    Создание таблицы с данными по остаткам шин
    :return:
    """
    try:
        with con:
            con.execute("""
            CREATE TABLE TIRE_REMNANTS (
                code TEXT,
                stock_name TEXT,
                stock_name_ru TEXT,
                wholesale_price TEXT,
                quantity TEXT,
                recommended_retail_price TEXT,
                minimal_internet_price TEXT,
                minimal_internet_price_msk TEXT,
                provider_key TEXT,
                cae TEXT,
                year TEXT,
                sale TEXT,
                price TEXT,
                delivery_time TEXT
            );
        """)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def create_table_wheels_remnants():
    """
    Создание таблицы с данными по остаткам дисков
    :return:
    """
    try:
        with con:
            con.execute("""
            CREATE TABLE WHEELS_REMNANTS (
                code TEXT,
                stock_name TEXT,
                stock_name_ru TEXT,
                wholesale_price TEXT,
                quantity TEXT,
                recommended_retail_price TEXT,
                minimal_internet_price TEXT,
                minimal_internet_price_msk TEXT,
                provider_key TEXT,
                cae TEXT,
                year TEXT,
                sale TEXT,
                price TEXT,
                delivery_time TEXT
            );
        """)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


"""
Добавление данных в таблицы
"""


def insert_database_warehouse_addresses(data):
    """
    Метод для записи данных адресов складов
    :param data: данные для записи в таблицу
    :return:
    """
    try:
        sql = 'INSERT INTO WAREHOUSE_ADDRESSES (name, city, phone, site, email, address, identifier) values(?, ?, ?, ?, ?, ?, ?)'
        with con:
            con.executemany(sql, data)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def insert_database_wheels_assortment(data):
    """
    Добавление данных таблицу БД по ассортименту дисков
    :param data:
    :return:
    """
    try:
        sql = 'INSERT INTO WHEELS_ASSORTMENT (code, p_full_name, p_brand, p_model, p_color, p_width, p_diameter, p_bolts_count, p_bolts_space, p_pcd, p_et, p_dia, p_type, p_photo_last_modified, p_info_last_modified, p_photo, p_shipping_weight, p_shipping_volume, p_shipping_length, p_shipping_width, p_shipping_height) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        with con:
            con.executemany(sql, data)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def insert_database_tire_assortment(data):
    """
    Добавление данных таблицу БД по ассортименту шин
    :param data:
    :return:
    """
    try:
        sql = 'INSERT INTO TIRE_ASSORTMENT (code, p_full_name, p_brand, p_model, p_width, p_height, p_diameter, p_load_index, p_speed_index, p_season, p_category, p_xl, p_protection, p_omologation, p_side, p_mud_terrain, p_all_terrain, p_cargo, p_thorn, p_runflat, p_axis, p_layering, p_appointment, p_photo_last_modified, p_info_last_modified, p_photo, p_shipping_weight, p_shipping_volume, p_shipping_length, p_shipping_width, p_shipping_height, p_completeness, p_design, p_can_thorn) values( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        with con:
            con.executemany(sql, data)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def insert_database_tire_remnants(data):
    """
    Добавление данных в таблицу БД по остаткам шин
    :param data:
    :return:
    """
    try:
        sql = 'INSERT INTO TIRE_REMNANTS (code, stock_name, stock_name_ru, wholesale_price, quantity, recommended_retail_price, minimal_internet_price, minimal_internet_price_msk, provider_key, cae, year, sale, price, delivery_time) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        with con:
            con.executemany(sql, data)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def insert_database_wheels_remnants(data):
    """
    Добавление данных в таблицу БД по остаткам дисков
    :param data:
    :return:
    """
    try:
        sql = 'INSERT INTO WHEELS_REMNANTS (code, stock_name, stock_name_ru, wholesale_price, quantity, recommended_retail_price, minimal_internet_price, minimal_internet_price_msk, provider_key, cae, year, sale, price, delivery_time) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        with con:
            con.executemany(sql, data)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


"""
Очистка данных в таблицах
"""


def clear_database(table_name):
    """
    Очистка содержимого таблицы
    :param table_name: название таблицы в БД
    :return:
    """
    try:
        with con:
            con.execute('DELETE FROM ' + table_name)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


"""
Считывание данных из БД
"""


def select_database_test():
    try:
        with con:
            data = con.execute("SELECT * FROM USER WHERE age <= 25")
            for row in data:
                print(row)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

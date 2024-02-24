import configparser
import os

import app
import db_sqlite
from app import download_file
from csv_assortment import read_csv

if __name__ == '__main__':
    print('Начало работы программы')
    config = configparser.ConfigParser()
    print('Инициализация файла конфигураций')
    config.read('config.ini')
    print('Очистка от файлов предыдущей выгрузки')
    app.clear_folder('uploaded_files')
    # todo Сделать тайм слип

    print('\nЗагрузка файлов выгрузки')
    print('Скачивание выгрузки адресов складов')
    download_file(config['WAREHOUSES']['warehouse_addresses'], "warehouse_addresses.csv")
    print('Скачивание выгрузки ассортимента шин')
    download_file(config['TIRES']['tire_assortment'], "tire_assortment.csv")
    print('Скачивание выгрузки ассортимента дисков')
    download_file(config['WHEELS']['wheels_assortment'], "wheels_assortment.csv")
    print('Скачивание выгрузки остатков шин')
    download_file(config['TIRES']['tire_remnants'], "tire_remnants.csv")
    print('Скачивание выгрузки остатков дисков')
    download_file(config['WHEELS']['wheels_remnants'], "wheels_remnants.csv")

    print('\nСоздание таблиц в БД')
    print('Создание таблицы адресов складов')
    db_sqlite.create_table_warehouse_addresses()
    print('Создание таблицы ассортимента шин')
    db_sqlite.create_table_tire_assortment()
    print('Создание таблицы ассортимента дисков')
    db_sqlite.create_table_wheels_assortment()
    print('Создание таблицы остатков шин')
    db_sqlite.create_table_tire_remnants()
    print('Создание таблицы остатков дисков')
    db_sqlite.create_table_wheels_remnants()

    print('\nЗагрузка данных в БД из скаченных файлов')
    print('Загрузка адресов складов в БД из локального файла')
    db_sqlite.insert_database_warehouse_addresses(read_csv('uploaded_files' + os.sep + 'warehouse_addresses.csv'))
    print('Загрузка ассортимента шин в БД')
    db_sqlite.insert_database_tire_assortment(read_csv('uploaded_files' + os.sep + 'tire_assortment.csv'))
    print('Загрузка ассортимента дисков в БД')
    db_sqlite.insert_database_wheels_assortment(read_csv('uploaded_files' + os.sep + 'wheels_assortment.csv'))
    print('Загрузка остатков шин в БД')
    db_sqlite.insert_database_tire_remnants(read_csv('uploaded_files' + os.sep + 'tire_remnants.csv'))
    print('Загрузка остатков дисков в БД')
    db_sqlite.insert_database_wheels_remnants(read_csv('uploaded_files' + os.sep + 'wheels_remnants.csv'))
    db_sqlite.close_connection()

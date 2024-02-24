import os
from unittest import TestCase
import os
from pathlib import Path

import db_sqlite
import main
from csv_assortment import read_csv


class Test(TestCase):

    def test_exists_database(self):
        """
        Проверка наличия файла базы данных
        :return:
        """
        if os.path.isfile('assortment.db'):
            print("Файл базы данных найден")
        else:
            print("Файл базы данных не найден")

    """
    Создание новых таблиц
    """

    def test_create_table_warehouse_addresses(self):
        db_sqlite.create_table_warehouse_addresses()

    def test_create_table_tire_assortment(self):
        db_sqlite.create_table_tire_assortment()

    def test_create_table_wheels_assortment(self):
        db_sqlite.create_table_wheels_assortment()

    def test_create_table_tire_remnants(self):
        db_sqlite.create_table_tire_remnants()

    def test_create_table_wheels_remnants(self):
        db_sqlite.create_table_wheels_remnants()

    """
    Добавление данных в таблицы
    """

    def test_insert_database_warehouse_addresses(self):
        db_sqlite.insert_database_warehouse_addresses(read_csv('uploaded_files' + os.sep + 'warehouse_addresses.csv'))

    def test_insert_database_tire_assortment(self):
        db_sqlite.insert_database_tire_assortment(read_csv('uploaded_files' + os.sep + 'tire_assortment.csv'))

    def test_insert_database_wheels_assortment(self):
        db_sqlite.insert_database_wheels_assortment(read_csv('uploaded_files' + os.sep + 'wheels_assortment.csv'))

    def test_insert_database_tire_remnants(self):
        db_sqlite.insert_database_tire_remnants(read_csv('uploaded_files' + os.sep + 'tire_remnants.csv'))

    def test_insert_database_wheels_remnants(self):
        db_sqlite.insert_database_wheels_remnants(read_csv('uploaded_files' + os.sep + 'wheels_remnants.csv'))

    """
    Очистка данных в таблицах
    """

    def test_clear_database(self):
        db_sqlite.clear_database('WAREHOUSE_ADDRESSES')
        db_sqlite.clear_database('TIRE_ASSORTMENT')
        db_sqlite.clear_database('WHEELS_ASSORTMENT')
        db_sqlite.clear_database('TIRE_REMNANTS')
        db_sqlite.clear_database('WHEELS_REMNANTS')

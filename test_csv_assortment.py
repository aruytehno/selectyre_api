import os
from unittest import TestCase

import configparser

from app import download_file
from csv_assortment import read_csv, write_csv


class Test(TestCase):

    def test_write_csv_data_test(self):
        # Define data
        data = [
            (1, "A towel,", 1.0),
            (42, " it says, ", 2.0),
            (1337, "is about the most ", -1),
            (0, "massively useful thing ", 123),
            (-2, "an interstellar hitchhiker can have.", 3),
        ]
        write_csv('test.csv', data)

    def test_read_csv_data_test(self):
        print(read_csv('test.csv'))

    def test_read_csv(self):
        print(read_csv('uploaded_files' + os.sep + 'warehouse_addresses.csv'))
        print(read_csv('uploaded_files' + os.sep + 'tire_assortment.csv'))
        print(read_csv('uploaded_files' + os.sep + 'tire_remnants.csv'))
        print(read_csv('uploaded_files' + os.sep + 'wheels_assortment.csv'))
        print(read_csv('uploaded_files' + os.sep + 'wheels_remnants.csv'))

    def test_download(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        download_file(config['WHEELS']['wheels_remnants'], "wheels_remnants.csv")

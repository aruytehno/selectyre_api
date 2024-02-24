from unittest import TestCase

import app


class Test(TestCase):
    def test_download_file(self):
        self.fail()

    def test_clear_folder(self):
        app.clear_folder('uploaded_files')

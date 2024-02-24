import os
import shutil
import urllib.request


def download_file(url, name):
    path = 'uploaded_files'
    print('Download: ' + name + ' ' + str(url))
    if not os.path.isdir(path):
        os.makedirs(path)
    urllib.request.urlretrieve(url, 'uploaded_files' + os.sep + name)


def clear_folder(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

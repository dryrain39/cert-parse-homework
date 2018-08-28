from zipfile import ZipFile
from copy import copy


class Unzip:
    extract_path = './unzip/'

    def unzip_and_read(self, filename):
        with ZipFile(filename) as certZip:
            with certZip.open('signCert.cert') as certFile:
                return certFile.read()

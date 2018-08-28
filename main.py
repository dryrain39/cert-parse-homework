import WebIndexParser
import FileDownloader
import Unzip
import CsvWriter
import json
import re
import datetime
import time

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def content_parse(text, date, ip):
    result = re.findall(r"cn=(.+)\(\)([0-9]+),ou=([a-zA-Z]+),", text)

    data = {
        'name': result[0][0],
        'time': int(time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d %H:%M").timetuple())),
        'bank_name': result[0][2],
        'account_no': result[0][1],
        'ip_address': ip,
        'country': ''
    }

    return data


if __name__ == "__main__":
    print("hello world!")

    downloader = FileDownloader.FileDownloader()
    unzip = Unzip.Unzip()
    parser = WebIndexParser.WebIndexParser()
    writer = CsvWriter.CsvWriter()

    downloader.use_cache_if_exists = True

    writer.header = ['name', 'time', 'bank_name', 'account_no', 'ip_address', 'country']
    writer.path = './data.csv'

    parser.base_url = 'http://fl0ckfl0ck.info/cert/'

    f = open('data.json', 'r')
    data = f.read()
    data = json.loads(data)

    for d in data:
        file_name = d['name'] + '.' + d['extension']

        if downloader.download(parser.base_url + d['link'], file_name) is True:
            logging.debug("File {} downloaded.".format(file_name))
            writer.write(content_parse(text=unzip.unzip_and_read(
                downloader.path + file_name).decode('euc-kr'), date=d['date'], ip=d['name']))
        else:
            logging.debug("File {} download Failed.".format(file_name))

    print(downloader.download_failed)

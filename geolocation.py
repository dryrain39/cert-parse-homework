import time
import json
from datetime import datetime
import CsvWriter
import FileDownloader

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    writer = CsvWriter.CsvWriter()
    downloader = FileDownloader.FileDownloader()

    writer.header = ['name', 'time', 'bank_name', 'account_no', 'ip_address', 'country']
    writer.path = './data.csv'

    data = writer.read()

    for i in range(0, len(data)):
        res = downloader.read(
            "https://api.ipgeolocation.io/ipgeo?apiKey=&ip={}".format(data[i][4]))
        
        result = json.loads(res)
        logging.debug("Updated {}".format(data[i][4]))
        data[i][5] = result['country_name']

    logging.debug("Writing...")
    writer.write(data, mode='w')

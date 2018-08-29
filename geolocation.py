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

    writer.header = ['name', 'time', 'bank_name',
                     'account_no', 'ip_address', 'country']
    writer.path = './data.csv'

    data = writer.read()

    writer.path = './data.geolocation.csv'

    failed = []

    for i in range(0, len(data)):
        try:

            if data[i][5] == '':
                res = downloader.read(
                "https://api.ipgeolocation.io/ipgeo?apiKey=&ip={}".format(data[i][4]))

                result = json.loads(res)
                
                logging.debug("Updated {}".format(data[i][4]))
                data[i][5] = result['country_name']
                    
            else:
                logging.debug("Pass {} {}".format(data[i][4], data[i][5]))

            writer.write({
                    'name': data[i][0],
                    'time': data[i][1],
                    'bank_name': data[i][2],
                    'account_no': data[i][3],
                    'ip_address': data[i][4],
                    'country': data[i][5]
                })

        except Exception:
            failed.append({
                    'name': data[i][0],
                    'time': data[i][1],
                    'bank_name': data[i][2],
                    'account_no': data[i][3],
                    'ip_address': data[i][4],
                    'country': data[i][5]
                })

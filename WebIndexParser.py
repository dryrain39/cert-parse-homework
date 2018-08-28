from bs4 import BeautifulSoup
import urllib.request
from pathlib import Path
import logging


class WebIndexParser:
    base_url = ''
    webcache_path = './.webcache'
    extensions = ['zip']
    load_cache_if_available = False
    save_cache = True

    web_data = None
    data = []

    def get(self):
        logging.info("Please wait...")

        if self.load_cache_if_available is True and self._cache_exists() is True:
            self.web_data = self._cache_io('rb')
            logging.debug("Webcache Loaded!")
        else:
            logging.debug("Download HTML from server...")
            self.web_data = urllib.request.urlopen(self.base_url).read()
            if self.save_cache is True:
                self._cache_io('wb')

        return self.web_data

    def parse_data(self):
        logging.info("Start parsing...")
        soup = BeautifulSoup(self.web_data, 'html.parser')

        links = soup.findAll('a')

        for link in links:
            extension = link['href'].split('.')[-1]

            if extension in self.extensions:
                logging.debug("Matched extension. OKAY")
                data = {
                    'link': link['href'],
                    'name': '.'.join(link.get_text().split('.')[:-1]),
                    'extension': extension,
                    'date': link.findNext('td').get_text().strip()
                }
                self.data.append(data)

            else:
                logging.debug("No matched extension. PASS.")
                pass

        logging.info("Parse Done!")

        # print(link['href'])
        # table = soup.find("table")
        # table_row = table.findAll("tr")
        # for row in table_row:
        #     cols = row.findAll('td')
        #     if len(cols) > 2:
        #         print('filename: ', cols[1].get_text())
        #         print('date: ', cols[2].get_text())
        #         print('filesize: ', cols[3].get_text())

    def _cache_io(self, act):
        f = open(self.webcache_path, act)
        if 'w' in act:
            f.write(self.web_data)
            return True
        elif 'r' in act:
            return f.read()
        f.close()

    def _cache_exists(self):
        cache_file = Path(self.webcache_path)

        result = True if cache_file.is_file() else False
        return result

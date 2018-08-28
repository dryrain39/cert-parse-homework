import urllib.request
from pathlib import Path


class FileDownloader:
    path = './downloads/'
    download_failed = []
    use_cache_if_exists = False

    def download(self, url, file_name):
        try:
            if self.use_cache_if_exists is False or self._check_files(self.path + file_name) is False:
                with urllib.request.urlopen(url) as response, open(self.path + file_name, 'wb') as out_file:
                    data = response.read()
                    out_file.write(data)
            return True
        except Exception:
            failed = self.download_failed.append({
                "url": url,
                "file_name": file_name
            })
            return failed

    def read(self, url):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            result_string = urllib.request.urlopen(req).read()
            return result_string
        except Exception as e:
            return e

    def _check_files(self, file_path):
        cache_file = Path(file_path)

        result = True if cache_file.is_file() else False
        return result

import urllib.request


class FileDownloader:
    path = './downloads/'
    download_failed = []

    def download(self, url, file_name):
        try:
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

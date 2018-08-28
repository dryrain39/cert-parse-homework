import csv


class CsvWriter:
    path = ''
    header = ['name', 'time', 'bank_name', 'account_no', 'ip_address', 'country']

    def write(self, data):
        # csv를 작성(추가)한다. fieldnames에 맞는 dictionary가 들어오면 필드에 맞게 csv를 쓴다.
        with open(self.path, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.header)

            writer.writerow(data)
        pass

    def make_new(self):
        # 초기 field(첫 번째 라인)을 구성하는 함수이다.
        with open(self.path, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.header)
            writer.writeheader()
        pass

    def read(self):
        # csv파일을 읽는 함수
        with open(self.path, 'r') as csvfile:
            r = list(csv.reader(csvfile))
            return r
        pass

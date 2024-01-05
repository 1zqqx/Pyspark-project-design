import datetime

year = ['2020', '2021', '2022', '2023', '2024']
month = ['01', '02']  # , '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']


def gen_date():
    with open('qdFiction/qdFiction/spiders/urls.txt', "w") as fs:
        for y in year:
            for m in month:
                if int(y) == datetime.datetime.now().year and datetime.datetime.now().month < int(m):
                    break
                str_url = "https://www.qidian.com/rank/yuepiao/year" + y + "-month" + m + "-page5/"
                fs.write(str_url + '\n')
                pass


if __name__ == '__main__':
    gen_date()

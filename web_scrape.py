import requests
import bs4
import re
import csv
import sys

UrlBasic = "https://volby.cz/pls/ps2017nss/"
header_data = ["kód obce",
               "název obce",
               "voliči v seznamu",
               "vydané obálky",
               "platné hlasy"
               ]

content = list()
countyR = str()
file = str()
data = list()
error = False


def to_csv():
    global file
    f = open(file, "w")
    f_write = csv.writer(f)
    f_write.writerow(header_data)
    f_write.writerows(content)
    f.close()


def find(countyS, args):
    global data
    for i in countyS.findAll("td", attrs=args):
        data.append(i.get_text())


def title(cityS):
    global data
    name = cityS.find("h3", string=re.compile('Obec'), class_=None).get_text()
    data.append(name[7:].strip("\n"))


def header(cityS):
    global header_data
    for strana in cityS.findAll("td", class_="overflow_name"):
        header_data.append(strana.get_text())


def county(countyS):
    global error
    global content
    global data
    first = True
    for link in countyS.findAll("td", class_="cislo"):
        data = list()
        data.append(link.string)
        city_r = requests.get(UrlBasic + link.a["href"])
        if city_r.status_code != 200:
            error = True
        city_s = bs4.BeautifulSoup(city_r.text, "html.parser")
        if first:
            header(city_s)
        first = False
        title(city_s)
        find(city_s, {"data-rel": "L1", "headers": ["sa2", "sa3", "sa6"]})
        find(city_s, {"class": "cislo", "headers": ["t1sa2 t1sb3", "t2sa2 t2sb3"]})
        content.append(data)


def check() -> bool:
    """Checks if user entered valid url and filename"""
    global countyR
    global file
    countyR = requests.get(sys.argv[1])
    if countyR.status_code != 200:
        print("Wrong URL/error code:", countyR.status_code)
        print(sys.argv[1])
        return False
    else:
        if sys.argv[2].endswith(".csv"):
            print("Url and filename OK")
            file = sys.argv[2]
            return True
        elif sys.argv[2].find(".") == int(-1):
            print("Url and filename OK (added suffix)")
            file = sys.argv[2] + ".csv"
            return True
        else:
            print("Wrong filename/suffix")
            return False


if __name__ == "__main__":
    global error
    if not check():
        exit()
    print("Start with scraping...")
    county(bs4.BeautifulSoup(countyR.text, "html.parser"))
    if error:
        print("Could not connect to some cities")
    print("Convert to csv", file)
    to_csv()
    print("Done")

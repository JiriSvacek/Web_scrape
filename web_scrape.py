import requests
import bs4
import re
import csv
import sys

UrlZaklad = "https://volby.cz/pls/ps2017nss/"
zahlavi = ["kód obce",
            "název obce",
            "voliči v seznamu",
            "vydané obálky",
            "platné hlasy"
            ]

obsah = list()
okresR = str()
soubor = str()
data = list()
chyba = False

def tocsv():
    global soubor
    f = open(soubor, "w")
    f_write = csv.writer(f)
    f_write.writerow(zahlavi)
    f_write.writerows(obsah)
    f.close()

def find(obecS, args):
    global data
    for i in obecS.findAll("td", attrs=args):
        data.append(i.get_text())

def nazev(obecS):
    global data
    nazev = obecS.find("h3", string=re.compile("Obec"), class_=None).get_text()
    data.append(nazev[7:].strip("\n"))

def nadpis(obecS):
    global zahlavi
    for strana in obecS.findAll("td", class_="overflow_name"):
        zahlavi.append(strana.get_text())

def obce(okresS):
    global chyba
    global obsah
    global data
    prvni = True
    for link in okresS.findAll("td", class_="cislo"):
        data = list()
        data.append(link.string)
        obecR = requests.get(UrlZaklad + link.a["href"])
        if obecR.status_code != 200:
            chyba = True
        obecS = bs4.BeautifulSoup(obecR.text, "html.parser")
        if prvni:
            nadpis(obecS)
        prvni = False
        nazev(obecS)
        find(obecS, {"data-rel": "L1", "headers": ["sa2", "sa3", "sa6"]})
        find(obecS, {"class": "cislo", "headers": ["t1sa2 t1sb3", "t2sa2 t2sb3"]})
        obsah.append(data)

def overeni():
    global okresR
    global soubor
    okresR = requests.get(sys.argv[1])
    if okresR.status_code != 200:
        print("Špatné URL/chybový kod:", okresR.status_code)
        print(sys.argv[1])
        return False
    else:
        if sys.argv[2].endswith(".csv"):
            print("Url i název souboru v pořádku")
            soubor = sys.argv[2]
            return True
        elif sys.argv[2].find(".") == int(-1):
            print("Url i název souboru v pořádku (přidána přípona)")
            soubor = sys.argv[2] + ".csv"
            return True
        else:
            print("Špatnný název souboru/přípony")
            return False

def main():
    if not overeni():
        exit()
    okresS = bs4.BeautifulSoup(okresR.text, "html.parser")
    print("Začínám se scrapingem...")
    obce(okresS)
    if chyba:
        print("K některým obcím se nepodařilo připojit")
    print("Převádím do csv", soubor)
    tocsv()
    print("Hotovo")

if __name__ == "__main__":
    main()
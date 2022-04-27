## web_scrape.py 
Tento script slouží k získání volebních dat (kód obce, název obce, voliči v seznamu, vydané obálky, platné hlasy a kandidující strany) 
ze stránky https://volby.cz/pls/ps2017/ps3?xjazyk=CZ, kde si vybereme příslušný volební okrsek
(např. Liberec - https://volby.cz/pls/ps2017/ps32?xjazyk=CZ&xkraj=7&xnumnuts=5103) a získané data zkopíruje do csv souboru. 

![obrazek](https://user-images.githubusercontent.com/99678439/165470067-25e6d0a4-e9a1-4907-9863-1c535e831ce1.png)

Odkaz zadáme jako první argument do terminálu za názvem scriptu, druhým argumentem zadáme název csv souboru, 
do kterého chceme data zkopírovat. Nezaleží jestli csv soubor bude mít příponu, popřípadě si ji script automaticky přidá. Důležite je je vložit oba argumenty s uvozovkami.
Viz příklad dole
```
web_scrape.py "https://volby.cz/pls/ps2017/ps32?xjazyk=CZ&xkraj=7&xnumnuts=5103" "liberec.csv"  
```

K funkci budeme potřebovat několik knihoven jejich instalace se provádí příkazem v terminálu: 
```
pip install -r requirements.txt 
``` 

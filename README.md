## Voting web scraper
This script is scraping voting data (code of city, name of city, number of votes,issued envelopes, valid votes and candidate parties) from page https://volby.cz/pls/ps2017/ps3?xjazyk=CZ, where we choose respective district (for example [Liberec](https://volby.cz/pls/ps2017/ps32?xjazyk=CZ&xkraj=7&xnumnuts=5103)) and scraped data are pushed to csv file

![obrazek](https://user-images.githubusercontent.com/99678439/165470067-25e6d0a4-e9a1-4907-9863-1c535e831ce1.png)

We enter the link as the first argument in the terminal after the name of the script, as the second argument we enter the name of the csv file,
to which we want to copy the data. It does not matter if the csv will have an extension, the script will automatically add suffix. It is important to enclose both arguments with quotation marks.
See example below
```
web_scrape.py "https://volby.cz/pls/ps2017/ps32?xjazyk=CZ&xkraj=7&xnumnuts=5103" "liberec.csv"  
```

We will need several libraries for the function, their installation is done by a command in the terminal: 
```
pip install -r requirements.txt 
``` 

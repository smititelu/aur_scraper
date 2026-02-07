# aur_scraper

1. Install scrapy playwright in new venv:
```
python3 -m venv ~/.playwright
source ~/.playwright/bin/activate
pip install scrapy-playwright
```

2. Run gold crawler
```
scrapy crawl aur -o aur.csv
```

2. Check price per gram data
```
libreoffice aur.csv
```

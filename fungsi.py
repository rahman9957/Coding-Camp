from ast import main
from bs4 import BeautifulSoup
import requests 

result = requests.get("https://www.detik.com/")

print(result)

print(result.encoding)
print(result.status_code)
print(result.elapsed)
print(result.url)
print(result.history)
print(result.headers['Content-Type'])

def main_scraper(url,directory):
    #fungsi.create.directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    print(source_text)

main_scraper("https://www.detik.com/","Hasil")

#simpan html

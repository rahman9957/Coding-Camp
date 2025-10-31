from bs4 import BeautifulSo
soup BeautifulSoup('<html><body><div class="class1">'
'</div><div class="class2"></div><div class="class3"></div></body></html>')
soup.findAll(True, {"class": ["class1", "class2"]})

from bs4 import BeautifulSoup
import os
import fungsi
import requests
def main_scraper (url, directory):
fungsi.create_directory(directory) #Membuat Directory
source_code
requests.get(url)
source_text source_code.text
soup
BeautifulSoup (source_text, "html.parser")
articles soup.find_all("h3", {'class': 'article__title article__title--medium'})
ticles2 = soup.find_all(True, 'class': ['article__box', 'article__title']}) #Penulisan Multiple class
for article in articles:
print("URL:"article.a.get("href"))
print("Judul:"article.text)
print()
for article2 in articles2:
print("URL2:"article2.a.get("href"))
print("Judul2:"article2.text)
print()
main_scraper("https://tekno.kompas.com/gadget", "Hasil")

for article in articles:
print("URL:"article.a.get("href"))
print("Judul:"article.text)
print()
article_format = "URL: " + article.a.get("href") + "\n" + "title" article.a.text
if fungsi.does_file_exist(directory + "/artikel.txt") is False: fungsi.create_new_file(directory + "/artikel.txt")

def does_file_exist(path): return os.path.isfile(path)
fungsi.write_to_file(directory + "/artikel.txt", article_format) print(article_format)

from bs4 import BeautifulSoup

import fungsi
import requests
def main_scraper (url, directory):
fungsi.create_directory(directory) #Membuat Directory
source_code requests.get(url)
source_text = source_code.text
soup BeautifulSoup (source_text, "html.parser")
articles soup.find_all("h2", {'class':'entry-title'})
for article in articles:
print("URL:"article.a.get("href"))
print("Judul:"article.text)
print()
article_format = "URL:"article.a.get("href") + "\n" + "title" article.a.text + "\n"
if fungsi.does_file_exist(directory + "/artikel.txt") is False:
fungsi.create_new_file(directory + "/artikel.txt")
fungsi.write_to_file(directory+"/artikel.txt", article_format)
print(article_format)
main_scraper("https://dongengceritarakyat.com/category/cerita-anak/", "Hasil")

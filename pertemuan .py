from bs4 import BeautifulSoup
import os
import fungsi
import requests

def main_scraper (url, directory):
    fungsi.create_directory(directory) #Membuat Directory
    source_code = requests.get(url)
    source_text source_code.text
    soup = BeautifulSoup (source_text, "html.parser")
    articles soup.find_all("h3", {'class': 'article__title article__title--medium'})
    
    for article in articles:
        print("URL:"article.a.get("href"))
        print("Judul:"article.text)
        print()
        article_format = "URL : " + article.a.get("href") + "\n" + "title : " + article.a.text + "\n"

        if fungsi.does_file_exist(directory + "/artikel.txt") is False:
           fungsi.create_new_file(directory + "/artikel.txt")

       fungsi.write_to_file(directory + "/artikel.txt", article_format)
       print(article_format)
main_scraper("https://tekno.kompas.com/gadget", "Hasil")

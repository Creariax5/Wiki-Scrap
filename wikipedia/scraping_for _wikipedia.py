import time

import requests
from bs4 import BeautifulSoup
import markdownify
from other.fonc import *

inp = input("Donnez un nom d'article wikipedia: ")

url = 'https://fr.wikipedia.org'
links = ['/wiki/' + inp]
file_url = "brain/"

i = 0

while i <= len(links):
    case = []
    print("begin request: " + links[i])
    result = requests.get(url + links[i])
    if result.ok:
        html = result.text
        soup = BeautifulSoup(html, 'lxml')
        title = soup.find("title").text
        title = transform_title(title)

        try:
            content = soup.findAll(class_="mw-parser-output")
            content = content[len(content)-1]
            scraped_links = content.findAll("a")
            for a in scraped_links:
                try:
                    link = a['href']
                    link_first_five = ""
                    for j in range(5):
                        link_first_five += link[j]
                    if link_first_five == '/wiki':
                        if not contain_point(link):
                            case.append(link)
                            links.append(link)
                except:
                    pass
            content = str(content)
            md = markdownify.markdownify(content, heading_style="ATX")

            tmp_case = []
            for c in case:
                c = remove_wiki(c)
                tmp_case.append(c)

            csv = create_csv(title, tmp_case)

            file_name = title
            with open(file_url + 'html/' + file_name + ".html", "w", encoding="utf-8") as f:
                f.write(content)
            with open(file_url + 'md/' + "wiki/" + file_name + ".md", "w", encoding="utf-8") as f:
                f.write(md)
            f = open(file_url + 'csv/' + "data" + ".csv", "a", encoding="utf-8")
            f.write(csv + "\n")
            f.close()
            print(title + " saved")
        except Exception as e:
            print(e)
        i += 1
    time.sleep(0)

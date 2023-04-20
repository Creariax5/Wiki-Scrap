import time

import requests
from bs4 import BeautifulSoup
import markdownify
from other.fonc import *

url = 'https://www.youtube.com'
links = ['/watch?v=PUMMCLrVn8A']
file_url_md = "brain/md/"
file_url_html = "data/html/"

i = 0
print(links)
while i <= len(links):
    print("begin request: " + links[i])
    session = requests.Session()
    result = session.get(url=url + links[i])
    if result.ok:
        html = result.text
        print(html)
        file_name = "yt"
        with open(file_url_html + file_name + ".html", "w", encoding="utf-8") as f:
            f.write(html)

        '''try:
            content = soup.findAll(class_="mw-parser-output")
            content = content[len(content)-1]
            scraped_links = content.findAll("a")
            for a in scraped_links:
                try:
                    link = a['href']
                    for j in range(5):
                        link_first_five = link[j]
                    if link[0] == '/':
                        links.append(link)
                except:
                    pass
            content = str(content)

            md = markdownify.markdownify(content, heading_style="ATX")
            file_name = title
            with open(file_url_html + file_name + ".html", "w", encoding="utf-8") as f:
                f.write(content)
            with open(file_url_md + "wiki/" + file_name + ".md", "w", encoding="utf-8") as f:
                f.write(md)
            print(title + " saved")
        except:
            print("bad link ERROR")'''
        i += 1
    time.sleep(0)

import time
from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org"
start = "/wiki/Special:Random"



def remove_brackets(text):
    hloubka = 0
    tag = False
    vysledek = ""
    for letter in text:
        if tag:
            vysledek += letter
            if letter == ">":
                tag = False
        else:
            if letter == "(":
                hloubka += 1
            elif letter == ")":
                hloubka -= 1
            elif hloubka == 0:
                vysledek += letter
                if letter == "<":
                    tag = True

        return vysledek


def get_title(soup):
    return soup.find(id='firstHeading').text


def get_link(soup):
    main_text = soup.find(class_="mw-parser-output")
    for odstavec in main_text.find_all('p'):
        html = remove_brackets(str(odstavec))
        odstavec = BeautifulSoup(html, "html.parser")
        for odkaz in odstavec.find_all('a'):
            href = odkaz.get("href")
            if href.startswith("/wiki/"):
                return href


def scrape(webpage):
    visited = set()
    while True:
        if webpage in visited:
            break
        visited.add(webpage)

        response = requests.get(f"{url}{webpage}")
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        print(get_title(soup))

        if not webpage:
            break

        time.sleep(1)


if __name__ == "__main__":
    scrape(start)
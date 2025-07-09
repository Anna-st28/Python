from bs4 import BeautifulSoup
import requests
import re
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def refined(s):
    return re.sub(r"\D+", "", s)


def write_csv(data):
    with open('dz_plugins.csv', "a") as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\r")
        writer.writerow([data["name"], data['url'], data['rating'], data['snippet']])


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    p1 = soup.find_all("section", class_="plugin-category")[2]
    plugins = p1.find_all("h2", class_="plugin-card")
    for plugin in plugins:
        try:
            name = plugin.find("h3", class_="plugin-link").text
        except AttributeError:
            name = ""
        url = plugin.find("h3", class_="plugin-link").find("a").get("href")
        rating = plugin.find("span", class_="plugin-status active").text
        replace_rating = refined(rating)
        snippet = plugin.find("div", class_="plugin-card__description").text.strip()

        data = {"name": name, "url": url, "rating": replace_rating, "snippet": snippet}
        write_csv(data)


def main():
    url = "https://lampa.nnslvp.io/plugins.html"
    get_data(get_html(url))


if __name__ == '__main__':
    main()

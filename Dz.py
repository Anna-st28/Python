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
    p1 = soup.find_all("section", class_="plugin-section")[2]
    plugins = p1.find_all("li")
    for plugin in plugins:
        try:
            name = plugin.find("h3", class_="entry-title").text
        except AttributeError:
            name = ""
        url = plugin.find("h3", class_="entry-title").find("a").get("href")
        rating = plugin.find("span", class_="rating-count").text
        replace_rating = refined(rating)
        snippet = plugin.find("div", class_="entry-excerpt").text.strip()

        data = {"name": name, "url": url, "rating": replace_rating, "snippet": snippet}
        write_csv(data)


def main():
    url = "https://ru.wordpress.org/plugins/"
    get_data(get_html(url))


if __name__ == '__main__':
    main()

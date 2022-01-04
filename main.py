#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import pdfkit
import sys

def get_links_on_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    return [
        (link.get('href'), link.get_text())
        for link in soup.find_all('a')
    ]


def download_single_pdf(link_tuple):
    url, title = link_tuple
    pdfkit.from_url(url, f"./pdfs/{title}.pdf")


def download_links_from_single_website(url):
    link_tuples = get_links_on_page(url)
    for link_tuple in link_tuples:
        download_single_pdf(link_tuple)


if __name__ == "__main__":
    with open("websites.txt") as f:
        for website in f:
            print(f"Downloading links from {website}...")
            download_links_from_single_website(website.strip())
# Bulk PDF downloader

Small utility for downloading all linked pages as PDFs.

## Installation
Prerequisites:
* Python 2.7+/3.X
* pip
* [wkhtmltopdf](https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf)

Install dependencies using `pip install -r requirements.txt`

## Usage

In repo root dir place `websites.txt` file with URLs of websites you want to save links from (1 URL per line).

Run `./main.py`

In `pdfs` dir you should find saved PDFs.
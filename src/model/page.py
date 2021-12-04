import requests as r
from bs4 import BeautifulSoup as bs
from os import link, remove, write
import typing

WRITE = "./src/data/index.html"

class Page:
    def page(preview_url: str) -> str:

        if not preview_url.startswith("https://t.me/s/"):
            raise ValueError("Url doesn't start with t.me/s/")

        s = preview_url
        return s

        # page = open(WRITE, "wb")
        # page.write(s)
        # page.close()
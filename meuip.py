#!/usr/bin/python3

from bs4 import BeautifulSoup
import urllib.error
import urllib.request

import urllib


url = "http://meuip.com"

try:

    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    a = resp.read()

    soup = BeautifulSoup(a, "html.parser")

    print("O seu IP: ", soup.font.string)

except Exception as e:

    print(e)

except urllib.error.HTTPError as e:

    print(e.code)
    print(e.read())

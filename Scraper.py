from urllib import *
import urllib

url = "https://searchenginesmarketer.com/company/resources/university-college-list"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)

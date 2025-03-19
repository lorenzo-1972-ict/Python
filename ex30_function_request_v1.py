# 

import requests
adresse_du_site = "https://books.toscrape.com/"

def recuperer_page(url_de_la_page):
    print(adresse_du_site + url_de_la_page)
    response = requests.get(adresse_du_site + url_de_la_page)
    return response.text

response = recuperer_page( "catalogue/page-1.html")
response = recuperer_page( "catalogue/page-2.html")
response = recuperer_page( "catalogue/page-3.html")
response = recuperer_page( "catalogue/page-4.html")
print(response)
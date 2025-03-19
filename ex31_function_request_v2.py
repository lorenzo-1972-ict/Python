# 

import requests
adresse_du_site = "https://books.toscrape.com/"

def recuperer_page(nb_de_la_page=1):
    url_de_la_page = f"catalogue/page-{nb_de_la_page}.html"
    print(adresse_du_site + url_de_la_page)
    response = requests.get(adresse_du_site + url_de_la_page)
    return response.text

response = recuperer_page()
print(response)

# def fonction2(arg1, arg2=0, arg3=3):
#   print("fonction2", arg1, arg2, arg3)

# fonction2("valeur1", arg3="valeur3")
# fonction2(arg2="valeur1", arg1="valeur2", arg3="valeur3")
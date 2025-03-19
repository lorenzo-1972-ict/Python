# script to illustrate a fonction with requests library

import requests

SiteURL = "https://www.python.org/"

SiteMenu = {
	"1": "about",
	"2": "downloads",
	"3": "doc",
	"4": "community",
	"5": "success Stories",
	"6": "news",
	"7": "events"
	}

def PageRetrieve(PageURL):
	print("\nMenu:", SiteMenu)
	MenuOption = input ("\nWhat page do you wish to retrieve? ")
	while MenuOption not in SiteMenu.keys():
		print("\nInvalid selection. Please provide a value displayed in the menu.")
		MenuOption = input ("\nWhat page do you wish to retrieve? ")
	response = requests.get(SiteURL + SiteMenu[MenuOption])
	return response
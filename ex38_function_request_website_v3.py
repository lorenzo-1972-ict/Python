# script to illustrate a fonction with requests library

from ex39_function_request_website_fetcher_v3 import PageRetrieve

PageURL = "MenuOption"
response = PageRetrieve(PageURL)
print(response.text)
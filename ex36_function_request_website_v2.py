# script to illustrate a fonction with requests library

from ex37_function_request_website_fetcher import PageRetrieve

PageURL = "MenuOption"
response = PageRetrieve(PageURL)
print(response.text)
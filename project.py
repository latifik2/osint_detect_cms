import requests, re
from bs4 import BeautifulSoup

url = input("Input clean url, without directories.\n").strip()

def checkRobots(url):
    url += "/robots.txt"
    drupal = "/user/login"
    wp = "/wp-admin"
    joomla = "/administrator"

    request = requests.get(url)
    if(re.search(drupal, request.text) != None):
        print(f"There is {drupal} directory in robots.txt file\nSuggesting CMS - Drupal")
    if(re.search(wp, request.text) != None):
        print(f"There is {wp} directory in robots.txt file\nSuggesting CMS - WordPress")
    if(re.search(joomla, request.text) != None):
        print(f"There is {joomla} directory in robots.txt file\nSuggesting CMS - Joomla")


checkRobots(url)


import requests
import lxml as lxml
import smtplib
from bs4 import BeautifulSoup

TARGET_PRICE = 25
MY_EMAIL = "ENTER EMAIL ADDRESS"
MY_PASSWORD = "ENTER PASSWORD"
RECIPIENT = "uENTER RECIPIENT'S EMAIL ADDRESS"
URL = "ENTER THE PRODUCT URL"


'''ADDITION INFORMATION MUST BE PASSED ALONG AS THE REQUESTS HEADERS IN ORDER FOR BEAUTIFULSOUP TO WORK THE
CURRENT BROWSER'''
response = requests.get(URL, headers={"Accept-Language": "en-US,en;q=0.9",
                                      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"})
webpage = response.text
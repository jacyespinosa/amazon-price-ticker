import requests
import lxml as lxml
import smtplib
from bs4 import BeautifulSoup

TARGET_PRICE = "ENTER THE TARGET PRICE"
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
#SINCE THE HTML.PARSER DOESN'T WORK WITH AMAZON, LXML MUST BE USED INSTEAD.
soup = BeautifulSoup(webpage, "lxml")
find_price = soup.find_all(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString")

price = [str(price.getText().split("$")[1]) for price in find_price]

#CHANGE INTO FLOATING POINT
current_price = 0
for item in price:
    current_price = float(item)


#PRODUCT NAME NEEDS TO BE MODIFIED (REMOVED UNNECESSARY NEWLINES) SO IT COULD BE USED IN THE CONTENT OF THE NOTIFICATION
name_of_product = soup.find_all(name="span", class_="a-size-large product-title-word-break")

product = ""
for text in name_of_product:
    product = text.getText()

product_name = product.strip("\n")
from bs4 import BeautifulSoup
import requests

def webscrap(url):

    source = requests.get(url)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')

    phones = soup.find('div', class_ = "_1YokD2 _3Mn1Gg").find_all('div', class_="_13oc-S")

    for phone in phones:

        phone_name = phone.find('div', class_="_4rR01T").get_text(strip= True)
        phone_price = phone.find('div', class_= "_30jeq3 _1_WHN1").get_text(strip= True)

        print(phone_name,  phone_price)


webscrap("https://www.flipkart.com/search?q=realme+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=realme+mobile%7CMobiles&requestId=ab32feee-58d1-4547-bc4e-14f8868d78c5&as-backfill=on")

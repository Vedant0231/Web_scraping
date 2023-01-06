from bs4 import BeautifulSoup
import requests
import openpyxl

excel = openpyxl.Workbook()
sheet = excel.active

sheet.title = "samsung phones"
sheet.append(['phone_name','phone_price'])


source = requests.get("https://www.flipkart.com/search?q=samsung+s22+ultra&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&as-pos=1&as-type=RECENT&suggestionId=samsung+s22+ultra%7CMobiles&requestId=e35ff1c0-5516-4fe6-afc5-3a55c39a5932&as-backfill=on")
source.raise_for_status()

soup = BeautifulSoup(source.text, 'html.parser')

phones = soup.find('div', class_ = "_1YokD2 _3Mn1Gg").find_all('div', class_="_13oc-S")

for phone in phones:

    phone_name = phone.find('div', class_="_4rR01T").get_text(strip= True)
    phone_price = phone.find('div', class_= "_30jeq3 _1_WHN1").get_text(strip= True)

    sheet.append([phone_name,phone_price])

excel.save("sasmsung_phones_details.xlsx")       
    



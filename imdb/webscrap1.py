from bs4 import BeautifulSoup
import requests
import openpyxl



try:
    
    excel = openpyxl.Workbook()
    sheet = excel.active
    sheet.title = "top 250 movies of all time"
    sheet.append(["Rank", "Movie_Name", "Year", "Rating"])

    source = requests.get("https://www.imdb.com/chart/top/")                 #we take url of  the web page we want to scrap.
    
    source.raise_for_status()                                                #this raise_for_status will give error if url is not present.
    
    soup = BeautifulSoup(source.text, 'html.parser')                         #this will help to get html content and present into better manner.

    movies = soup.find('tbody', class_ = 'lister-list').find_all('tr')       #first we need to filter our needed data from raw html content      

    # print(len(movies))    #                                                #250 because there are 250 list in it.

    for movie in movies:

        rank = movie.find('td', class_="titleColumn").get_text(strip = True).split('.')[0]      #strip will remove all unwanted space and other type of noicey data.
        name = movie.find('td', class_="titleColumn").a.text                                    #movie name is present in 'a' tag so a.text will give you a movie name  
        year = movie.find('td', class_="titleColumn").span.text.strip('()')                     #year is in span class which is in td, we you strip to remove () from (1999)
        rating = movie.find('td', class_="ratingColumn imdbRating").strong.text                 #rating is in strong tag which is in td tag

        sheet.append([rank, name , year , rating])
        
    excel.save("IMDB Top 250 Movies of all Times.xlsx")   

except Exception as e:

    print(e)

 
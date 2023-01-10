from bs4 import BeautifulSoup
import requests
import openpyxl

exl = openpyxl.Workbook()
sheet = exl.active
sheet.title = "rottentomato"
sheet.append(['movie_name','glimpse','tomatometer','audiencescore'])

source = requests.get("https://www.rottentomatoes.com/browse/movies_at_home/sort:popular?page=1")

soup =  BeautifulSoup(source.text, 'html.parser')

for movie in soup.find("div", class_= "discovery-grids-container").find_all('a', class_= "js-tile-link"):

    name = movie.find("span",class_="p--small").get_text(strip = True)

    movie_glimpse = movie.find('button')

    if movie_glimpse is None:

        url = (f"url for {name} is not found")
   
    else:
        
        url = movie_glimpse['data-video-player-overlay-url']
    
    rating = movie.find("score-pairs")

    Tomatometer = rating['criticsscore']

    audiencescore = rating['audiencescore']
    
    sheet.append([name, url, Tomatometer, audiencescore])
    exl.save('rottentomato.xlsx')







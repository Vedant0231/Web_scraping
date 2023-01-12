from bs4 import BeautifulSoup
import requests

source = requests.get("https://github.com/Vedant0231?tab=repositories")

soup = BeautifulSoup(source.text, 'html.parser')

gitdatas = soup.find('div',id="user-repositories-list").find_all('li', class_="col-12 d-flex flex-justify-between width-full py-4 border-bottom color-border-muted public source")

for repo in gitdatas:

    repo_name = repo.find('a', itemprop= "name codeRepository").get_text(strip = True)

    print(repo_name)
  

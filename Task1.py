

from pprint import pprint
from bs4 import BeautifulSoup
import requests
import json
import pprint

url="https://www.imdb.com/india/top-rated-indian-movies/"
page=requests.get(url)
soup=BeautifulSoup(page.text,"html.parser")

def scrap_top_list():
    main_div=soup.find("div",class_="lister")
    tbody=main_div.find("tbody",class_="lister-list")
    trs=tbody.find_all("tr")
    # print(tbody)


    movie_r=[]
    movie_n=[]
    year_release=[]
    m_urls=[]
    m_ratings=[]

    for tr in trs:
        position=tr.find("td",class_="titleColumn").get_text().strip()
        rank=""
        for i in position:
            if "." not in i:
                rank=rank+i
            else:
                break
        movie_r.append(rank)
    # print(movie_r)

        name=tr.find("td",class_="titleColumn").a.get_text()
        movie_n.append(name)
    # print(movie_n)

        year=tr.find("td",class_="titleColumn").span.get_text()
        year_release.append(year)
    # print(year_release)

        url=tr.find("td",class_="titleColumn").a["href"]
        link="https://www.imdb.com"+url
        m_urls.append(link)
    # print(m_urls)

        rating=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
        m_ratings.append(rating)
    # print(m_ratings)

    Top_Movies=[]
    details={"position":"","name":"","year":"","rating":"","url":""}
    for i in range(0,len(movie_r)):
        details["position"]=int(movie_r[i])
        details["name"]=str(movie_n[i])
        details["year"]=(year_release[i][1:5])
        details["rating"]=float(m_ratings[i])
        details["url"]=m_urls[i]
        Top_Movies.append(details.copy())
        

    # return (Top_Movies)
    with open("Task1.json","w")as f:
        json.dump(Top_Movies,f,indent=4)

pprint.pprint(scrap_top_list())
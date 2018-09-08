from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)

raw_data = conn.read()
html_page = raw_data.decode("utf-8")

soup = BeautifulSoup(html_page,"html.parser")
section = soup.find("section", "section chart-grid")
div = section.find("div")
ul = div.find("ul")
li_list = ul.find_all("li")
news_list = []
for li in li_list:
    h3 = li.h3
    h4 = li.h4
    name = h3.string
    artists = h4.string
    news = {
        "Artists": artists,
        "Name": name,
    }
    news_list.append(news)
    print(name)
    print(artists)
import pyexcel
pyexcel.save_as(records=news_list, dest_file_name="itunes.xlsx")

from youtube_dl import YoutubeDL

option = {
      'default_search' : 'ytsearch',
      'max_downloads': 5,
}
dl = YoutubeDL(option)
list_songs = []
for items in li_list :
    dl.download(items['song name']+ " - "+items['artist'])

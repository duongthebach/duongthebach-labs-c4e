# 1.1 Open connection to page
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://dantri.com.vn"
conn = urlopen(url) 

# 1.2 Read data
raw_data = conn.read()
# 1.3 Decode data
html_page = raw_data.decode("utf-8")
# 1.4 Save data to file
# 1.4.1 Open connection to file 
# 1.4.2 Write data
# 1.4.3 Close connection
    # f_conn = open('dantri.html', 'wb')
    # f_conn.write(raw_data)
    # f_conn.close()

soup = BeautifulSoup(html_page, "html.parser")
ul = soup.find("ul", "ul1 ulnew") # id="tbl_grade"

li_list = ul.find_all("li")

news_list = []

for li in li_list:
    a = li.h4.a
    title = a.string
    link = url + a["href"]
    news = {
        "Title": title,
        "Link": link,
    }
    news_list.append(news)
    print(link)
    print(title)
    print("* " *10)
print(news_list)
import pyexcel
pyexcel.save_as(records=news_list, dest_file_name="dantri.xlsx")
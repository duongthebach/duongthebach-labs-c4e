from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)

raw_data = conn.read()
html_page = raw_data.decode("utf-8")
soup = BeautifulSoup(html_page,"html.parser")
h_t = soup.find_all('td', 'h_t')
h_t_list = []
table = soup.find("table", id="tableContent")
tr = table.find_all('tr')
tr_list = []
for item in h_t_list:
    h_t_list.append(item)
for item in tr:
    tr_new_list = item.find_all('td', 'b_r_c')
    tr_data_list = []
    for i in tr_new_list:
        i = i.string
        if i != None:
            tr_data_list.append(i)
    if len(h_t_list):
        tr_list.append(tr_data_list)
final = []
for item in tr_list:
    value_list = []
    value = {
            "Danh Muc" : item[0]
        }  
    for i in range(len(h_t_list)):
        value[h_t_list[i]] =  item[1+i]   
              
    final.append(value)
# import pyexcel
# pyexcel.save_as(records=final, dest_file_name="ROI.xlsx")
print(final)
  
            




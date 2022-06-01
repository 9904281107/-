#requests 불러오기 pip install requests)
import requests
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}

url = "https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop"
#requests.get()으로 Url정보 요청하기 
r= requests.get(url, headers=headers)
r.status_code

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
print(soup)
#선수들의 정보가 담긴 태그와 클래스 찾기
player_info=soup.find_all('tr', class_=['odd','even'])

#첫번째 요소 확인하기 
print(player_info[0])

#전체 개수 확인하기
print(len(player_info))


# 7개의 정보를 담을 리스트 만들기 (등번호, 이름, 포지션, 나이, 국적, 팀 ,가치)

number=[]
name=[]
position=[]
age=[]
nation=[]
team=[]
value=[]


for info in player_info:
    player = info.find_all("td")
    #print(player)
    #print(player[0])
#   해당 정보를 찾아서 각리스트에 .append로 추가하기
    number.append(player[0].text)
    name.append(player[3].text)
    position.append(player[4].text)
    age.append(player[5].text)
    nation.append(player[6].img['alt'])
    team.append(player[7].img['alt'])
    value.append(player[8].text.strip())

    print(value)

    
    #데이터 프레임 만들기
    import pandas as pd

    
from bs4 import BeautifulSoup as bs
import requests

#requests야 네이버 실시간 검색 정보 그걸 글로 바꿔줘

url='https://www.naver.com'
response=requests.get(url).text
# print(type(response))

#bs 객체에서 response라고 하는 변수안에 담긴 객체를 파싱하고 그 결과를 bs 객체로 반환한다/
soup=bs(response, 'html.parser')
# print(type(soup))

keywords=soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div span[class*=ah_k]')
print(keywords)
print(type(keywords))

for index, keyword in enumerate(keywords):
    print(index, keyword.text)
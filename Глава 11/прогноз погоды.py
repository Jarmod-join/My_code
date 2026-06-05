import bs4, requests

headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get('https://world-weather.ru/pogoda/russia/khabarovsk/', headers=headers)
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
result = noStarchSoup.select('#weather-now-number')
print(result[0].text)
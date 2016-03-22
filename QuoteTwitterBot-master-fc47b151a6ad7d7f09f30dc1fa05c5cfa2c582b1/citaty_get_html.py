from requests import request
import time
while True:

    url = 'http://www.aphorisme.ru/random/?q=2329'#Адрес сайта для парсинга

    t = request('GET', url).text
    with open('test1.html', 'w', encoding='utf-8') as f: #Сохраняю страницу на диск
        f.write(t)
        time.sleep(5)#Залипаю на 5 сек чтобы не качать постоянно






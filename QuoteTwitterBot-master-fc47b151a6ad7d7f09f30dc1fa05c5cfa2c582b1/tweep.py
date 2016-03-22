from TwitterFollowBot import TwitterBot
from bs4 import BeautifulSoup
import time, random
while True:

    my_bot = TwitterBot()#Инициализирую бота
    def getQoute():
        soup = BeautifulSoup(open('test1.html'), 'lxml')
        for rendom_aph in soup.find_all('div',{'class':'rendom_aph'}):
            print((str(rendom_aph.text)))


        if len(rendom_aph.text) >=132: #Проверка длины отправки сообщения Если больше 133 то повторно выполнить парсинг
            time.sleep(10)
            getQoute()
        else:
            return rendom_aph.text

    a = getQoute()
    #dict = ['Qoute', 'DatQt', 'FunDy', 'Mind'] #Словарь хештегов



    my_bot.send_tweet(a + '#Follow' )#Бот шлет сообщение
    time.sleep(3600)







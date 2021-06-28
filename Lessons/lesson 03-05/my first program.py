from urllib.request import urlopen
from bs4 import BeautifulSoup
import telebot

bot = telebot.TeleBot('1641431246:AAHOQ6SAeVwXbYMWCPKjLb-WmfJccqn9bFA')

@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello there')

@bot.message_handler(commands = ['update'])
def update_message(message):
    html = urlopen('https://kurs.onliner.by/')
    soup = BeautifulSoup(html)

#test = soup.findAll('tr', {'class':'tr-main'})[0].contents[3].contents[1].text

    tag_list = soup.findAll('p', {'class':'value rise'})

    buy = tag_list[0].text
    sell = tag_list[1].text
    nb = tag_list[2].text

    bot.send_message(message.chat.id, buy + "; " + sell + "; " + nb)

bot.polling()
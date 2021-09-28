import os
import telebot
from newsapi import NewsApiClient
from datetime import date
from telebot import util



API_KEY = os.getenv('API_KEY')
NEWS_API = os.getenv('NEWS_API_KEY')
bot = telebot.TeleBot(API_KEY)
api = NewsApiClient(api_key= NEWS_API)
print(NEWS_API)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to DailyNFTNews 📰 by yazyyyyy,\n🔹Use the command /nftnews to get the top NFT headlines for today.")

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, "Hello")


@bot.message_handler(commands=['nftnews'])
def nftnews(message):
  today = date.today()
  d1 = today.strftime("%Y-%m-%d")
  print(d1)
  
  data =api.get_everything(q='NFT', language='en', from_param=d1, page_size=20)

  print(data.keys())
  print(data['status'])
  print(data['totalResults'])
  # print(data['articles'][0])
  articles = data['articles']
  result = "Latest NFT Headlines for " + d1 + " :\n"
  for x,y in enumerate(articles):
    result = result + (f'{x+1}. *{y["title"]}* - {y["url"]}') + "\n"

  splitted_text = util.split_string(result, 4000)

  for text in splitted_text:
    bot.send_message(message.chat.id, text, parse_mode='Markdown')

  # bot.send_message(message.chat.id, result, parse_mode='Markdown')



bot.polling()

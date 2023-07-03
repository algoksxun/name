from telebot.async_telebot import AsyncTeleBot
from random  import*

bot = AsyncTeleBot("6303803551:AAHSolp6PGR07ZlGdPadSdDCwVVvP0jmbwY")
@bot.message_handler(commands=['help','start'])
async def send_welcom(message):
    await bot.reply_to(message, 'приветствую тебя пользователь ')
@bot.message_handler(commands=['Давайте поговорим?'])
async def send_welcom(message):
    await bot.reply_to(message, 'давайте , можете задать мне вопрос')
@bot.message_handler(func=lambda message:True)
async def  echo_message(messega):
    text_message = messega.text
    text_message = messega.text
    if 'дела' in text_message or 'настроение' in text_message:
        await  bot.reply_to((messega , 'все круто , а у тебя?'))
    #if 'шутка' in text_message or ''

import asyncio
asyncio.run(bot.polling())

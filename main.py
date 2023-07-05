import os

from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv , find_dotenv

load_dotenv(find_dotenv())

TOKEN= os.getenv('nazvanie_peremenou')
bot = AsyncTeleBot(TOKEN, parse_mode='HTML')



@bot.message_handler(commands=['timer'])
async  def send_timer(message):
    chat_id = message.from_user.id
    bot_message = await bot.send_message(chat_id , 'таймер на 100000 секунд')
    for i in range(1,100000):
        await asyncio.sleep(1)
        await bot.edit_message_text(f'{100000 -i} прошло',chat_id, bot_message.id)
        await bot.delete_message(chat_id , bot_message.id)
#@bot.message_handler(content_types=["text1"])
#async def draznilka(message):
 #   chat_id = message.from_user.id
  #  await bot.delete_message(chat_id , message.id)
@bot.message_handler(content_types=['comanda22'])
async def send_com(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, '<i>text</i>')

@bot.message_handler(commands=['help'])
async def send_mesage(message):
    chat_id = message.from_user.id
    await  bot.send_message(chat_id,'m',disable_notification=True, protect_content=True)
@bot.message_handler(commands='kazino')
async  def kasik_mesage(mesage):
    chat_id = mesage.from_user.id
    bot_message = await bot.send_dice(chat_id ,'🎰')
    print(bot_message.dice.value)
@bot.message_handler(commands=['start'])
async def send_welcom(message):
    await bot.reply_to(message, 'приветствую тебя, пользователь ')
@bot.message_handler(commands=['kosti'])
async  def send_kost(message):
    chat_id = message.from_user.id
    await bot.send_sticker(chat_id,'CAACAgIAAxkBAAIiRmSkDDLFeyEtYh37qiXwKbyzNsPGAAJ6FwAChkRZSvL6Vnp_vOjhLwQ')
@bot.message_handler(commands=['textdoc'])
async  def send_text(message):
    chat_id = message.from_user.id
    await bot.send_document(chat_id , open('text.txt.txt','rb'))
@bot.message_handler(commands=['kordi'])
async  def bot_kordinat(message):
    chat_id = message.from_user.id
    await  bot.send_location(chat_id ,48.21994809389074, 53.22507023359397)
@bot.message_handler(commands=['foto_bobra'])
async  def bot_foto(message):
    chat_id = message.from_user.id
    await  bot.send_photo(chat_id , 'https://www.belta.by/images/storage/news/with_archive/2021/000022_1634479196_464896_big.jpg', caption='вот ваш бобр' )
@bot.message_handler(commands=['Давайте поговорим?'])
async def send_welcom(message):
    await bot.reply_to(message, 'давайте , можете задать мне вопрос')
@bot.message_handler(commands=['ПРЫФВРФЫВОР0'])
#async def send_jurn(message):
 #   await  bot.send_message(<b>текст</b>)
#@bot.message_handler(commands=['Давайте поговорим?'])
#async def send_welcom(message):
    #await bot.reply_to(message, 'давайте , можете задать мне вопрос')
@bot.message_handler(func=lambda message:True)
async def  echo_message(messega):
    text_message = messega.text
    text_message = messega.text
    if 'дел' in text_message or 'настроение' in text_message:
        await  bot.reply_to((messega , 'все круто , а у тебя?'))
    if 'шутка' in text_message or 'сме' in text_message:
        await  bot.reply_to((messega, 'В Африке, если человек на 80% состоит из воды, то считается, что он из благополучной семьи.'))
markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup.add('первая кнопка')
markup.add('вторая кнопка')

@bot.message_handler(commands=['knopki'])
async def send_klava(message):
    chat_id = message.from_user.id
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    one_knopka = 'кнопка 1'
    two_knopka = 'кнопка 2 '
    three_knopka ='кнопка 3 '
    markup.add(one_knopka , two_knopka , three_knopka,row_width=2)
    await bot.send_message(chat_id , '2 вариант кнопок', reply_markup=markup)

@bot.message_handler(commands=['hep'])
async def sendWelcom(message):
    chat_id = message.from_user.id
    list_buttons = ['1','2','3']
    await bot.send_message(chat_id, 'ТтттттттттттттТ', reply_markup=generate_btns(list_buttons, 2))

def generate_btns(list_butonns, rows):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(*list_butonns, row_width=rows)
    return (markup)


@bot.message_handler(commands=['awerty'])
async def qwerty_send(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id,'<b>text</b>')
    await bot.send_message(chat_id,'<i>text</i>')
    await bot.send_message(chat_id, '<u>text</u>')
    await bot.send_message(chat_id, '<s>text</s>')
    await bot.send_message(chat_id, '<code>text</code>')
    await bot.send_message(chat_id, '<pre>text</pre>')
    await bot.send_message(chat_id, '<tg-spoiler>text</tg-spoiler>')
    await bot.send_message(chat_id, '<a href="https://learn.algoritmika.org/login">text</a>')
    await bot.send_message(chat_id, '<a href="tg://user?id=(message.id)")">bold</>')


@bot.message_handler(commands=['lp'])
async def sendWelcom(message):
    chat_id = message.from_user.id
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('1',callback_data='first')
    btn2 = InlineKeyboardButton('2',callback_data='second')
    btn3 = InlineKeyboardButton('3',callback_data='third')
    markup.add(btn1, btn2, btn3)
    await bot.send_message(chat_id, 'первый вариант', reply_markup=markup)


import asyncio
asyncio.run(bot.polling())

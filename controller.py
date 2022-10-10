import telebot
from telebot import types
import random

TOKEN = "*********************************"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Рандомное число 🔢')
    item2 = types.KeyboardButton('Курсы валют 💰')
    item3 = types.KeyboardButton('Информация ℹ️')
    item4 = types.KeyboardButton('Пожелание на сегодня 🌸')
    item5 = types.KeyboardButton('Другое')

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Рандомное число 🔢':
            bot.send_message(message.chat.id, 'Ваше число:' + str(random.randint(0, 1000)))
        elif message.text == 'Курсы валют 💰':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Курс доллара 💵')
            item2 = types.KeyboardButton('Курс евро 💶')
            back = types.KeyboardButton('Назад 🔙')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Этот курс вас не порадует ;(', reply_markup=markup)

        elif message.text == 'Курс доллара 💵':
            bot.send_message(message.chat.id, ' ≈37.4, к сожалению пока так :(')

        elif message.text == 'Курс евро 💶':
            bot.send_message(message.chat.id, ' ≈37.4, к сожалению пока так :(')

        elif message.text == 'Пожелание на сегодня 🌸':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Я счастлив(а)  😀')
            item2 = types.KeyboardButton('Мне грустно 😢')
            item3 = types.KeyboardButton('Я тебе не доверяю,бот 🤖')
            back = types.KeyboardButton('Назад 🔙')
            markup.add(item1, item2, item3, back)

            bot.send_message(message.chat.id, 'Пожелание на сегодня 🌸', reply_markup=markup)

        elif message.text == 'Информация ℹ️':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('О боте 🤖')
            item2 = types.KeyboardButton('Что в коробке? 📦')
            back = types.KeyboardButton('Назад 🔙')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Что вас интересует ⬇️', reply_markup=markup)

        elif message.text == 'О боте 🤖':
            bot.send_message(message.chat.id, 'Created by Danylo Kyrychenko 👨🏻')

        elif message.text == 'Что в коробке? 📦':
            bot.send_message(message.chat.id, '➡️📦🫵❤️')

        elif message.text == 'Другое':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Настройки')
            item2 = types.KeyboardButton('Подписка')
            item3 = types.KeyboardButton('Стикер')
            back = types.KeyboardButton('Назад 🔙')
            markup.add(item1, item2, item3, back)

            bot.send_message(message.chat.id, 'Тут пока ничего нет нажмите на клавиатуре: Назад 🔙', reply_markup=markup)

        elif message.text == 'Назад 🔙':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Рандомное число 🔢')
            item2 = types.KeyboardButton('Курсы валют 💰')
            item3 = types.KeyboardButton('Информация ℹ️')
            item4 = types.KeyboardButton('Пожелание на сегодня 🌸')
            item5 = types.KeyboardButton('Другое')

            markup.add(item1, item2, item3, item4, item5)

            bot.send_message(message.chat.id, 'Назад 🔙', reply_markup=markup)

        elif message.text == 'Я счастлив(а)  😀':
            bot.send_message(message.chat.id, 'Считают, что успех приходит к тем, кто рано встает. Нет: успех приходит к тем, кто встает в хорошем настроении. Марсель Ашар 🤔')

        elif message.text == 'Мне грустно 😢':
            bot.send_message(message.chat.id, 'Улыбка имеет эффект зеркало – улыбнись и ты увидишь улыбку. 😁')

        elif message.text == 'Я тебе не доверяю,бот 🤖':
            bot.send_message(message.chat.id, 'Я бы на твоем месте доверял, у меня твои данные, {0.first_name} 😈'.format(message.from_user))


bot.polling(none_stop=True)

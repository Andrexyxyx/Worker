import telebot

from Config import TOKEN, keys, help_text
from Extensions import APIException, MoneyConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = help_text
    bot.reply_to(message, f'''Здравствуйте, {message.chat.username}
{text}''')

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Список доступных валют:"
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def get_price(message: telebot.types.Message):
    try:
        val = message.text.split(" ")
        if len(val) != 3:
            raise APIException("Количество введенных параметров не равно трем. Введите 3 параметра")
        quote, base, amount = val
        total_base = MoneyConverter.convert(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        result = round(float(amount)*float(total_base), 2)
        text = f'Стоимость {amount} {quote} - {result} {base}'

        bot.send_message(message.chat.id, text)

bot.polling()


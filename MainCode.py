import telebot;
from telebot import types

bot = telebot.TeleBot('My Token');

#Главное меню с приветствием и выбором возраста
@bot.message_handler(commands=['start'])
def main_menu(message):
    hello_text = "Приветствую вас в моем небольшом справочнике"
    markup = types.InlineKeyboardMarkup(row_width=2)
    zero_six = types.InlineKeyboardButton('0-6', callback_data= "06month")
    six_twelve = types.InlineKeyboardButton('6-12', callback_data= "612month")
    one_two = types.InlineKeyboardButton('1-2', callback_data= "12year")
    two_three = types.InlineKeyboardButton('2-3', callback_data= "23year")
    three_six = types.InlineKeyboardButton('3-6', callback_data= "36year")
    six_above = types.InlineKeyboardButton('Более 6', callback_data= "6year")
    markup.add(zero_six,six_twelve,one_two,two_three,three_six,six_above)
    bot.send_message(message.chat.id, hello_text, reply_markup=markup)

#здесь меню для 0-6 
@bot.callback_query_handler(func=lambda call:True)
def answer (call): 
    if call.message:
        if call.data == '06month':
            hello_text = "Поздравляю вас, вы выбрали меню 0-6"
            markup1 = types.InlineKeyboardMarkup(row_width=2)
            lavanda = types.InlineKeyboardButton('Лаванда', callback_data= "lavanda1")
            rimska_romashka = types.InlineKeyboardButton('Римская ромашка',callback_data= "rimska_romashka1")
            dosirovka_masla = types.InlineKeyboardButton('Дозировка',callback_data= "dosirovka")
            dlya_vanni = types.InlineKeyboardButton('Ванна',callback_data= "Vanna")
            prostudi_virusi = types.InlineKeyboardButton('Болезни',callback_data= "prostudi_virusi1")
            masash = types.InlineKeyboardButton('Массаж',callback_data= "masash1")
            nasad_v_menu = types.InlineKeyboardButton('Вернуться в главное меню',callback_data= "nasad_v_menu1")
            markup1.add(lavanda, rimska_romashka, dosirovka_masla, dlya_vanni,prostudi_virusi, masash, nasad_v_menu)
            bot.send_message(call.message.chat.id, hello_text, reply_markup=markup1)
            
        elif call.data == "612month":
            markup2 = types.InlineKeyboardMarkup(row_width=1)
            nasad_v_menu = types.InlineKeyboardButton('Вернуться в главное меню', callback_data="nasad_v_menu1")
            markup2.add(nasad_v_menu)
            bot.send_message(call.message.chat.id, "Спасибо, что пользуетесь нашим приложением", reply_markup=markup2)

        elif call.data == "12year":
            markup3 = types.InlineKeyboardMarkup(row_width=1)
            nasad_v_menu = types.InlineKeyboardButton('Вернуться в главное меню', callback_data="nasad_v_menu1")
            markup3.add(nasad_v_menu)
            bot.send_message(call.message.chat.id, "Спасибо, что пользуетесь нашим приложением", reply_markup=markup3)

        elif call.data == "23year":
            markup4 = types.InlineKeyboardMarkup(row_width=1)
            nasad_v_menu = types.InlineKeyboardButton('Вернуться в главное меню', callback_data="nasad_v_menu1")
            markup4.add(nasad_v_menu)
            bot.send_message(call.message.chat.id, "Спасибо, что пользуетесь нашим приложением", reply_markup=markup4)

        elif call.data == "36year":
            markup5 = types.InlineKeyboardMarkup(row_width=1)
            nasad_v_menu = types.InlineKeyboardButton('Вернуться в главное меню', callback_data="nasad_v_menu1")
            markup5.add(nasad_v_menu)
            bot.send_message(call.message.chat.id, "Спасибо, что пользуетесь нашим приложением", reply_markup=markup5)

        elif call.data == "6year":
            markup6 = types.InlineKeyboardMarkup(row_width=1)
            nasad_v_menu = types.InlineKeyboardButton('Вернуться в главное меню', callback_data="nasad_v_menu1")
            markup6.add(nasad_v_menu)
            bot.send_message(call.message.chat.id, "Спасибо, что пользуетесь нашим приложением", reply_markup=markup6)
        
        
        elif call.data == "nasad_v_menu1":
            hello_text = "Приветствую вас в моем небольшом справочнике"
            markup = types.InlineKeyboardMarkup(row_width=2)
            zero_six = types.InlineKeyboardButton('0-6', callback_data="06month")
            six_twelve = types.InlineKeyboardButton('6-12', callback_data="612month")
            one_two = types.InlineKeyboardButton('1-2', callback_data="12year")
            two_three = types.InlineKeyboardButton('2-3', callback_data="23year")
            three_six = types.InlineKeyboardButton('3-6', callback_data="36year")
            six_above = types.InlineKeyboardButton('Более 6', callback_data="6year")
            markup.add(zero_six, six_twelve, one_two, two_three, three_six, six_above)
            bot.send_message(call.message.chat.id, hello_text, reply_markup=markup)
            
        #далее идет код меню 0-6 месяцев
        elif call.data == 'lavanda1':
            hello_text = "Вы выбрали лаванду!"
            markup7 = types.InlineKeyboardMarkup(row_width=1)
            nasad_v_menu = types.InlineKeyboardButton('Вернуться в главное меню', callback_data="nasad_v_menu1")
            dosirovka_masla = types.InlineKeyboardButton('Дозировка для возраста 0-6', callback_data="dosirovka")
            markup7.add(nasad_v_menu, dosirovka_masla)
            bot.send_message(call.message.chat.id, hello_text, reply_markup=markup7)

        elif call.data == 'rimska_romashka1':
            hello_text = "Вы выбрали ромашку!"
            markup8 = types.InlineKeyboardMarkup(row_width=1)
            nasad_v_menu = types.InlineKeyboardButton('Вернуться в главное меню', callback_data="nasad_v_menu1")
            dosirovka_masla = types.InlineKeyboardButton('Дозировка для возраста 0-6', callback_data="dosirovka")
            markup8.add(nasad_v_menu, dosirovka_masla)
            bot.send_message(call.message.chat.id, hello_text, reply_markup=markup8)

        elif call.data == 'dosirovka':
            hello_text = "Вы выбрали дозировку!"
            markup9 = types.InlineKeyboardMarkup(row_width=1)
            nasad_v_menu = types.InlineKeyboardButton('Вернуться в главное меню', callback_data="nasad_v_menu1")
            markup9.add(nasad_v_menu)
            bot.send_message(call.message.chat.id, hello_text, reply_markup=markup9)

        elif call.data == 'dlya_vanni1':
            markup10 = types.InlineKeyboardMarkup(row_width=1)
            nasad_v_menu = types.InlineKeyboardButton('Вернуться в главное меню', callback_data="nasad_v_menu1")
            markup10.add(nasad_v_menu)
            bot.send_message(call.message.chat.id, "Привет", reply_markup=markup10)

        elif call.data == 'prostudi_virusi1':
            hello_text = "Вы выбрали раздел 'болезни'"
            markup11 = types.InlineKeyboardMarkup(row_width=1)
            nasad_v_menu = types.InlineKeyboardButton('Вернуться в главное меню', callback_data="nasad_v_menu1")
            dosirovka_masla = types.InlineKeyboardButton('Дозировка для возраста 0-6', callback_data="dosirovka")
            markup11.add(nasad_v_menu, dosirovka_masla)
            bot.send_message(call.message.chat.id, hello_text, reply_markup=markup11)

        elif call.data == 'masash1':
            hello_text = "Вы выбрали массаж!"
            markup12 = types.InlineKeyboardMarkup(row_width=1)
            nasad_v_menu = types.InlineKeyboardButton('Вернуться в главное меню', callback_data="nasad_v_menu1")
            dosirovka_masla = types.InlineKeyboardButton('Дозировка для возраста 0-6', callback_data="dosirovka")
            markup12.add(nasad_v_menu, dosirovka_masla)
            bot.send_message(call.message.chat.id, hello_text, reply_markup=markup12)
            
bot.polling(none_stop=True, interval=0)

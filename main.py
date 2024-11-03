import telebot
import utils
TOKEN = "7345251836:AAGwfa24qSKwPrsFXW9rrUhnTdD8q7gcHQw"
bot = telebot.TeleBot(TOKEN)
keyboard_0 = telebot.types.InlineKeyboardMarkup()
keyboard_1 = telebot.types.InlineKeyboardMarkup()
keyboard_3 = telebot.types.InlineKeyboardMarkup()
sp_1 =["Python ","Scratch", "Roblox ","WEB разработка","Game ART"]
for i in sp_1:
    btn_get_photo = telebot.types.InlineKeyboardButton(str(i), callback_data=str(sp_1.index(i)+2))
    keyboard_0.add(btn_get_photo)
i = "Поставить оценку"
btn_get_photo = telebot.types.InlineKeyboardButton(i, callback_data=i)
keyboard_3.add(btn_get_photo)
i = "Рейтинг преподавателей"
btn_get_photo = telebot.types.InlineKeyboardButton(i, callback_data=i)
keyboard_3.add(btn_get_photo)
i = "Поставить лайк"
btn_get_photo = telebot.types.InlineKeyboardButton(i, callback_data="1")
keyboard_1.add(btn_get_photo)
i = "Поставить дизлайк"
btn_get_photo = telebot.types.InlineKeyboardButton(i, callback_data="-1")
keyboard_1.add(btn_get_photo)
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Действия: ', reply_markup=keyboard_3)
g =''
h = False
sas = 0
@bot.callback_query_handler(func=lambda callback: True)
def handle_callback(callback):
    global g
    global sas
    if callback.data == "exit":
        sas-=2
    if sas == 3:
        gh = []
        with open('text.txt', 'r', encoding='utf-8') as f:
            gh = list(f)
        p=[]
        sp_1 =["  ","Илья","Кирилл", "Маша ","Настя","Данил"]
        g = sp_1[g]
        with open("text.txt", "w",encoding='utf-8') as file:
            for i in list(gh):
                p = i.split()
                if g == p[0]:
                    file.write(f"{p[0]} {int(p[1])+int(callback.data)}\n")
                else:
                    file.write(f"{p[0]} {p[1]}\n")
        with open("te.txt", "a") as file:
            file.write(f"\n{callback.message.chat.id}")
        sas = 0
    elif sas == 0:
        bot.send_message(callback.message.chat.id, 'Выбери курс: ', reply_markup=keyboard_0)
        sas+=1
    elif callback.data == "Рейтинг преподавателей":
        sp = utils.top_prepod()
        print(sp)
        for i in range(len(sp)):
            st = f"{i+1}. {sp[i]}"
            bot.send_message(callback.message.chat.id, st)
    elif sas==2:
        with open('te.txt', 'r', encoding='utf-8') as f:
            gh = list(f)
        for i in range(len(gh)):
            gh[i] = gh[i][:-1]
        if str(callback.message.chat.id) in gh:
            bot.send_message(callback.message.chat.id, 'Ты уже отправлял оценку')
            sas=0
        else:
            bot.send_message(callback.message.chat.id, 'Выбери оценку', reply_markup=keyboard_1)
            g = int(callback.data)-2
            sas+=1
    elif sas ==1:
        a = int(callback.data)-2
        sp_2 = ["Назад","Илья","Кирилл", "Маша ","Настя","Данил"]
        keyboard_3 = telebot.types.InlineKeyboardMarkup()
        b = telebot.types.InlineKeyboardButton(sp_2[0], callback_data="exit")
        keyboard_3.add(b)
        if a!=4:
            s = 0
            for i in range(1+a,len(sp_2)):
                s+=1
                b = telebot.types.InlineKeyboardButton(sp_2[i], callback_data=str(i+2))
                keyboard_3.add(b)
                if s == 2:
                    break
        bot.edit_message_text(text = "Выбери преподователя:",chat_id= callback.message.chat.id,message_id=callback.message.id)
        bot.edit_message_reply_markup(reply_markup=keyboard_3 ,chat_id= callback.message.chat.id,message_id=callback.message.id)
        sas+=1

bot.polling(non_stop=True, interval=1)
import telebot
from telebot import types
import psycopg2
from week import weeker

conn = psycopg2.connect(database="telebot",
                        user="postgres",
                        password="12345",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()

c = int(weeker())

token = "2133792240:AAE7hDb_PFpsDU5DaHdE8WUmeeTUarcTLRc"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    if c == 0:
        bot.send_message(message.chat.id, 'Добрый день, сейчас  ⬆️верхняя⬆️  неделя. '
                                          '\n\nПожалуйста, выберите интересующий вас день',
        reply_markup=keyboard())
    elif c == 1:
        bot.send_message(message.chat.id, 'Добрый день, сейчас  ⬇️нижняя⬇️  неделя. '
                                          '\n\nПожалуйста, выберите интересующий вас день',
        reply_markup=keyboard())


def keyboard():
    but1 = types.KeyboardButton('Понедельник')
    but2 = types.KeyboardButton('Вторник')
    but3 = types.KeyboardButton('Среда')
    but4 = types.KeyboardButton('Четверг')
    but5 = types.KeyboardButton('Пятница')
    button1 = types.KeyboardButton('Расписание на текущую неделю')
    button2 = types.KeyboardButton('Расписание на следующую неделю')
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(but1).add(but2).add(but3).add(
        but4).add(but5).add(button1).add(button2)
    return markup


@bot.message_handler(content_types=['text'])
def manipulator(message):
    if message.text == 'Понедельник' and c==1 :
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Понедельник'")
        x = cursor.fetchall()
        x1 = str('Понедельник, нижняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
    elif message.text == 'Вторник' and c==1 :
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Вторник2'")
        x = cursor.fetchall()
        x1 = str('Вторник, нижняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
    elif message.text == 'Среда' and c==1 :
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Среда2'")
        x = cursor.fetchall()
        x1 = str('Среда, нижняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
    elif message.text == 'Четверг' and c==1 :
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Четверг'")
        x = cursor.fetchall()
        x1 = str('Четверг, нижняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
    elif message.text == 'Пятница' and c==1 :
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Пятница2' ")
        x = cursor.fetchall()
        x1 = str('Пятница, нижняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
    elif message.text == 'Понедельник' and c==0 :
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Понедельник'")
        x = cursor.fetchall()
        x1 = str('Понедельник, верхняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
    elif message.text == 'Вторник' and c==0 :
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Вторник1'")
        x = cursor.fetchall()
        x1 = str('Вторник, верхняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
    elif message.text == 'Среда' and c==0 :
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Среда1'")
        x = cursor.fetchall()
        x1 = str('Среда, верхняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
    elif message.text == 'Четверг' and c==0 :
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Четверг'")
        x = cursor.fetchall()
        x1 = str('Четверг, верхняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
    elif message.text == 'Пятница' and c==0 :
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Пятница1'")
        x = cursor.fetchall()
        x1 = str('Пятница, верхняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())

    elif message.text == 'Расписание на текущую неделю' and c == 0:
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Понедельник'")
        x = cursor.fetchall()
        x1 = str('Понедельник, верхняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Вторник1'")
        x = cursor.fetchall()
        x1 = str('Вторник, верхняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Среда1'")
        x = cursor.fetchall()
        x1 = str('Среда, верхняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Четверг'")
        x = cursor.fetchall()
        x1 = str('Четверг, верхняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Пятница1'")
        x = cursor.fetchall()
        x1 = str('Пятница, верхняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())

    elif message.text == 'Расписание на текущую неделю' and c == 1:
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Понедельник'")
        x = cursor.fetchall()
        x1 = str('Понедельник, нижняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Вторник2'")
        x = cursor.fetchall()
        x1 = str('Вторник, нижняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Среда2'")
        x = cursor.fetchall()
        x1 = str('Среда, нижняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Четверг'")
        x = cursor.fetchall()
        x1 = str('Четверг, нижняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Пятница2'")
        x = cursor.fetchall()
        x1 = str('Пятница, нижняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())

    elif message.text == 'Расписание на следующую неделю' and c == 0:
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Понедельник'")
        x = cursor.fetchall()
        x1 = str('Понедельник, нижняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Вторник2'")
        x = cursor.fetchall()
        x1 = str('Вторник, нижняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Среда2'")
        x = cursor.fetchall()
        x1 = str('Среда, нижняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Четверг'")
        x = cursor.fetchall()
        x1 = str('Четверг, нижняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Пятница2'")
        x = cursor.fetchall()
        x1 = str('Пятница, нижняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())

    elif message.text == 'Расписание на следующую неделю' and c == 1:
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Понедельник'")
        x = cursor.fetchall()
        x1 = str('Понедельник, верхняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Вторник1'")
        x = cursor.fetchall()
        x1 = str('Вторник, верхняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Среда1'")
        x = cursor.fetchall()
        x1 = str('Среда, верхняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Четверг'")
        x = cursor.fetchall()
        x1 = str('Четверг, верхняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, "
                       "teacher.full_name FROM public.timetable INNER JOIN public.teacher ON timetable.teacher_id ="
                       " teacher.id WHERE day ='Пятница1'")
        x = cursor.fetchall()
        x1 = str('Пятница, верхняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=keyboard())


@bot.message_handler(commands=['button'])
async def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("button")
    markup.add(item1)
    await message.answer("Выберите действие", reply_markup=markup)

bot.infinity_polling()

import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def main_menu(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🔈 О нас")
    item2 = types.KeyboardButton("📎Квартиры")
    item3 = types.KeyboardButton('❓Помощь')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Здравствуйте, {0.first_name}! 👋".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
    bot.send_message(message.chat.id,
                     "\nЯ - Бот \"Забота\" компании \"9 Ночей\". Со мной Вы легко "
                     "выберите и забронируете лучшие апартаментыв нашем любимом городе, сможете узнать о знаменитых "
                     "святынях и достопримечательностях. ⛪️".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
    bot.send_message(message.chat.id,
                     "Пожалуйста выберите один из пунктов меню ниже:".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def inline_menu(message):
    if message.chat.type == 'private':
        if message.text == '🔈 О нас':
            bot.send_message(message.chat.id,
                             "Наша сеть партнеров \"9 Ночей\" предоставляет в краткосрочную аренду уютные "
                             "квартиры и апартаменты посуточно, полностью укомплектованные и оборудованные "
                             "всем необходимым для комфортной жизни. Бронируйте онлайн на сайте или звоните нам! ")

            bot.send_message(message.chat.id, "Видео о нас: \n(Дождитель заргузки 🙃)")

            bot.send_video(message.chat.id, open("Photo/9 ночей промо~2.mp4", "rb"))

            bot.send_message(message.chat.id, "К чему мы стремимся?")

            bot.send_message(message.chat.id, "Наша цель в том, чтобы гости 9 Ночей ощущали качественный "
                                              "сервис и домашний уют в каждом путешествии, бронируя "
                                              "апартаменты в нашей компании!")

            bot.send_message(message.chat.id, "Мы ждем Вас в гости! 😊")

        elif message.text == '📎Квартиры':

            markup = types.InlineKeyboardMarkup(row_width=2)

            item1 = types.InlineKeyboardButton("Однокомнатные", callback_data='1room')
            item2 = types.InlineKeyboardButton("Двухкомнатные", callback_data='2room')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, '🏘Сколько комнат Вам необходимо?', reply_markup=markup)

        elif message.text == '❓Помощь':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('Часто задаваемые вопросы', callback_data='questions')
            item2 = types.InlineKeyboardButton("Оборудование в квартирах", callback_data='equipment')
            item3 = types.InlineKeyboardButton('Список достопримечательностей', callback_data='attractions')
            item4 = types.InlineKeyboardButton('Кафе, рестораны и доставка еды', callback_data='food')
            item5 = types.InlineKeyboardButton("❗️Задать вопрос администратору", callback_data='admin')

            markup.add(item1, item2, item3, item4, item5)

            bot.send_message(message.chat.id, 'В этом разделе Вы узнаете ответы на часто задаваемые вопросы, а так же '
                                              'о интересных местах, которые Вы сможете посетить в нашем замечательном '
                                              'городе, узнаете о многочисленных святынях Радонежья, '
                                              'музеях, парках, зонах для прогулок, кафе, ресторанах и прочих '
                                              'замечательных развлечениях для взрослых и детей.')
            bot.send_message(message.chat.id, 'Пожалуйста, выберите соответствующий раздел:', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Список квартир
    try:
        if call.message:

            if call.data == '1room':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("ул. 1й Ударной Армии, 95",
                                                   callback_data='951')
                item2 = types.InlineKeyboardButton("ул. Инженерная, 21", callback_data='211')
                item3 = types.InlineKeyboardButton("пр. Красной Армии, 218", callback_data='2181')

                markup.add(item1, item2, item3)

                bot.send_message(call.message.chat.id, 'Однокомнатные апартаменты:', reply_markup=markup)

            elif call.data == '2room':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("ул. 1й Ударной Армии, 95",
                                                   callback_data='952')
                item2 = types.InlineKeyboardButton("ул. Инженерная, 21", callback_data='212')
                item3 = types.InlineKeyboardButton("пр. Красной Армии, 238", callback_data='2382')
                item4 = types.InlineKeyboardButton("пр. Красной Армии, 240", callback_data='2402')

                markup.add(item1, item2, item3, item4)

                bot.send_message(call.message.chat.id, 'Двухкомнатные апартаменты:', reply_markup=markup)

            elif call.data == 'backhelp':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Часто задаваемые вопросы', callback_data='questions')
                item2 = types.InlineKeyboardButton("Оборудование в квартирах", callback_data='equipment')
                item3 = types.InlineKeyboardButton('Список достопримечательностей', callback_data='attractions')
                item4 = types.InlineKeyboardButton('Кафе, рестораны и доставка еды', callback_data='food')
                item5 = types.InlineKeyboardButton("❗️Задать вопрос администратору", callback_data='admin')

                markup.add(item1, item2, item3, item4, item5)

                bot.send_message(call.message.chat.id,
                                 'В этом разделе Вы узнаете ответы на часто задаваемые вопросы, а '
                                 'так же о интересных местах, которые Вы сможете посетить в '
                                 'нашем замечательном городе, узнаете о многочисленных святынях '
                                 'Радонежья, музеях, парках, зонах для прогулок, кафе, ресторанах '
                                 'и прочих замечательных развлечениях для взрослых и детей.')
                bot.send_message(call.message.chat.id, 'Пожалуйста, выберите соответствующий раздел:',
                                 reply_markup=markup)

    except Exception as e:
        print(repr(e))

    # Кнопки квартир
    try:
        if call.data == '951':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Фотосет", callback_data='951Ph')
            item2 = types.InlineKeyboardButton('Забронировать / оплатить онлайн', callback_data='951Wb')
            item3 = types.InlineKeyboardButton('Назад', callback_data='rooms')

            markup.add(item1, item2, item3)
            bot.send_message(call.message.chat.id, '1й Ударной Армии, 95', reply_markup=markup)

        elif call.data == '211':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Фотосет", callback_data='211Ph')
            item2 = types.InlineKeyboardButton('Забронировать / оплатить онлайн', callback_data='211Wb')
            item3 = types.InlineKeyboardButton('Назад', callback_data='rooms')

            markup.add(item1, item2, item3)
            bot.send_message(call.message.chat.id, 'Инженерная, 21', reply_markup=markup)

        elif call.data == '2181':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Фотосет", callback_data='2181Ph')
            item2 = types.InlineKeyboardButton('Забронировать / оплатить онлайн', callback_data='2181Wb')
            item3 = types.InlineKeyboardButton('Назад', callback_data='rooms')

            markup.add(item1, item2, item3)
            bot.send_message(call.message.chat.id, 'Красной армии, 218', reply_markup=markup)

        elif call.data == '952':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Фотосет", callback_data='952Ph')
            item2 = types.InlineKeyboardButton('Забронировать / оплатить онлайн', callback_data='952Wb')
            item3 = types.InlineKeyboardButton('Назад', callback_data='rooms')

            markup.add(item1, item2, item3)
            bot.send_message(call.message.chat.id, '1й Ударной Армии, 95', reply_markup=markup)

        elif call.data == '212':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Фотосет", callback_data='212Ph')
            item2 = types.InlineKeyboardButton('Забронировать / оплатить онлайн', callback_data='212Wb')
            item3 = types.InlineKeyboardButton('Назад', callback_data='rooms')

            markup.add(item1, item2, item3)
            bot.send_message(call.message.chat.id, 'Инженерная, 21', reply_markup=markup)

        elif call.data == '2382':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Фотосет", callback_data='2382Ph')
            item2 = types.InlineKeyboardButton('Забронировать / оплатить онлайн', callback_data='2382Wb')
            item3 = types.InlineKeyboardButton('Назад', callback_data='rooms')

            markup.add(item1, item2, item3)
            bot.send_message(call.message.chat.id, 'Красной Армии, 238', reply_markup=markup)

        elif call.data == '2402':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Фотосет", callback_data='2402Ph')
            item2 = types.InlineKeyboardButton('Забронировать / оплатить онлайн', callback_data='2402Wb')
            item3 = types.InlineKeyboardButton('Назад', callback_data='rooms')

            markup.add(item1, item2, item3)
            bot.send_message(call.message.chat.id, 'пр. Красной Армии, 240', reply_markup=markup)

    except Exception as e:
        print(repr(e))

    # Ссылки
    try:

        if call.data == '951Wb':
            bot.send_message(call.message.chat.id, 'https://9nights.ru/sp/434')

        if call.data == '211Wb':
            bot.send_message(call.message.chat.id, 'https://9nights.ru/sp/45')

        if call.data == '2181Wb':
            bot.send_message(call.message.chat.id, 'https://9nights.ru/sp/11')

        if call.data == '952Wb':
            bot.send_message(call.message.chat.id, 'https://9nights.ru/sp/220')

        if call.data == '212Wb':
            bot.send_message(call.message.chat.id, 'https://9nights.ru/sp/221')

        if call.data == '2382Wb':
            bot.send_message(call.message.chat.id, 'https://9nights.ru/sp/12')

        if call.data == '2402Wb':
            bot.send_message(call.message.chat.id, 'https://9nights.ru/sp/213')

    except Exception as e:
        print(repr(e))
    # Фото
    try:

        markup = types.InlineKeyboardMarkup(row_width=2)

        if call.data == '951Ph':
            bot.send_photo(call.message.chat.id, open('Photo/Однокомнатные/Ударной Армии 95 1.JPG', 'rb'),
                           reply_markup=markup)
            bot.send_photo(call.message.chat.id, open('Photo/Однокомнатные/Ударной Армии 95 2.JPG', 'rb'),
                           reply_markup=markup)
            item1 = types.InlineKeyboardButton('Больше фотографий', callback_data='more 951')
            markup.add(item1)
            bot.send_photo(call.message.chat.id, open('Photo/Однокомнатные/Ударной Армии 95 3.JPG', 'rb', ),
                           reply_markup=markup)

        elif call.data == '211Ph':
            bot.send_photo(call.message.chat.id, open('Photo/Однокомнатные/Инженерная 1.jpg', 'rb'),
                           reply_markup=markup)
            bot.send_photo(call.message.chat.id, open('Photo/Однокомнатные/Инженерная 2.jpg', 'rb'),
                           reply_markup=markup)
            item1 = types.InlineKeyboardButton('Больше фотографий', callback_data='more 221')
            markup.add(item1)
            bot.send_photo(call.message.chat.id, open('Photo/Однокомнатные/Инженерная 3.jpg', 'rb'),
                           reply_markup=markup)

        elif call.data == '2181Ph':
            bot.send_photo(call.message.chat.id, open('Photo/Однокомнатные/Красной армии 218 1.JPG', 'rb'),
                           reply_markup=markup)
            bot.send_photo(call.message.chat.id, open('Photo/Однокомнатные/Красной армии 218 2.JPG', 'rb'),
                           reply_markup=markup)
            item1 = types.InlineKeyboardButton('Больше фотографий', callback_data='more 2181')
            markup.add(item1)
            bot.send_photo(call.message.chat.id, open('Photo/Однокомнатные/Красной армии 218 3.JPG', 'rb'),
                           reply_markup=markup)

        elif call.data == '952Ph':
            bot.send_photo(call.message.chat.id, open('Photo/Двухкомнатные/Ударной армии 95 1.jpg', 'rb'),
                           reply_markup=markup)
            bot.send_photo(call.message.chat.id, open('Photo/Двухкомнатные/Ударной армии 95 2.jpg', 'rb'),
                           reply_markup=markup)
            item1 = types.InlineKeyboardButton('Больше фотографий', callback_data='more 952')
            markup.add(item1)
            bot.send_photo(call.message.chat.id, open('Photo/Двухкомнатные/Ударной армии 95 3.jpg', 'rb'),
                           reply_markup=markup)

        elif call.data == '212Ph':
            bot.send_photo(call.message.chat.id, open('Photo/Двухкомнатные/Инженерная 1.jpg', 'rb'),
                           reply_markup=markup)
            bot.send_photo(call.message.chat.id, open('Photo/Двухкомнатные/Инженерная 2.jpg', 'rb'),
                           reply_markup=markup)
            item1 = types.InlineKeyboardButton('Больше фотографий', callback_data='more 212')
            markup.add(item1)
            bot.send_photo(call.message.chat.id, open('Photo/Двухкомнатные/Инженерная 3.jpg', 'rb'),
                           reply_markup=markup)

        elif call.data == '2382Ph':
            bot.send_photo(call.message.chat.id, open('Photo/Двухкомнатные/Красной Армии 238 1.jpg', 'rb'),
                           reply_markup=markup)
            bot.send_photo(call.message.chat.id, open('Photo/Двухкомнатные/Красной Армии 238 2.jpg', 'rb'),
                           reply_markup=markup)
            item1 = types.InlineKeyboardButton('Больше фотографий', callback_data='more 2382')
            markup.add(item1)
            bot.send_photo(call.message.chat.id, open('Photo/Двухкомнатные/Красной Армии 238 3.jpg', 'rb'),
                           reply_markup=markup)

        elif call.data == '2402Ph':
            bot.send_photo(call.message.chat.id, open('Photo/Двухкомнатные/Красной Армии 240 1.jpg', 'rb'),
                           reply_markup=markup)
            bot.send_photo(call.message.chat.id, open('Photo/Двухкомнатные/Красной Армии 240 2.jpg', 'rb'),
                           reply_markup=markup)
            bot.send_photo(call.message.chat.id, open('Photo/Двухкомнатные/Красной Армии 240 3.jpg', 'rb'),
                           reply_markup=markup)
            item1 = types.InlineKeyboardButton('Больше фотографий', callback_data='more 2402')
            markup.add(item1)
            bot.send_photo(call.message.chat.id, open('Photo/Двухкомнатные/Красной Армии 240 4.jpg', 'rb'),
                           reply_markup=markup)

    except Exception as e:
        print(repr(e))
    # Вопросы
    try:
        markup = types.InlineKeyboardMarkup(row_width=2)

        if call.data == 'questions':
            bot.send_message(call.message.chat.id, '⭕ Можно ли оплатить проживание онлайн?', reply_markup=markup)
            bot.send_message(call.message.chat.id, 'Да, можно! На нашем портале 9Ночей.рф вы можете воспользоваться '
                                                   'сервисом онлайн '
                                                   'оплаты проживания при оформлении бронирования.',
                             reply_markup=markup)
            bot.send_message(call.message.chat.id, '⭕️ Как подключить wi-fi?', reply_markup=markup)
            bot.send_message(call.message.chat.id, 'Во всех квартирах на видном месте размещены таблички с паролем от '
                                                   'бесплатного wi-fi', reply_markup=markup)
            bot.send_message(call.message.chat.id, '⭕️ Какие условия заселения?', reply_markup=markup)
            bot.send_message(call.message.chat.id,
                             'Для заезда Гостю необходимо иметь при себе паспорт и залог от 2000 руб, который '
                             'возвращается при выезде (сумму залога уточняйте у менеджера). В апартаменты без '
                             'сопровождения взрослых не заселяются Гости младше 23 лет. '
                             'Также запрещено проведение шумных мероприятий.', reply_markup=markup)
            bot.send_message(call.message.chat.id, '⭕️ Расчётное время заезда / выезда?', reply_markup=markup)
            bot.send_message(call.message.chat.id, 'Стандартное время заезда с 14 часов, выезда до 12 часов. Иную '
                                                   'возможность уточняйте у нас.',
                             reply_markup=markup)
            bot.send_message(call.message.chat.id, '⭕️ Какие способы оплаты апартаментов существуют для гостей?',
                             reply_markup=markup)
            bot.send_message(call.message.chat.id, 'Гость может оплатить своё проживание любым удобным способом: '
                                                   'наличными, с помощью банковской карты при заселении, а также '
                                                   'безналичным расчётом (по выставленному счёту). Дополнительно оплату'
                                                   ' можно произвести на нашем сайте 9nights.ru в личном кабинете, '
                                                   'предварительно сообщив нам о желании оплатить онлайн (способ '
                                                   'оплаты онлайн доступен не во всех городах. Возможность уточняйте '
                                                   'у нас).', reply_markup=markup)
            bot.send_message(call.message.chat.id, '⭕️ Есть ли в апартаментах принадлежности для приготовления еды?',
                             reply_markup=markup)
            bot.send_message(call.message.chat.id, 'Конечно. Кухни в наших апартаментах оборудованы всей необходимой '
                                                   'мебелью, техникой, а также посудой для приготовления и '
                                                   'приёма пищи.', reply_markup=markup)

            bot.send_message(call.message.chat.id, '⭕️ Нужно ли вносить предоплату?', reply_markup=markup)
            bot.send_message(call.message.chat.id, 'Предоплата необходима в периоды большого спроса и в большие '
                                                   'праздники, такие как Новый Год или Рождество. Предоплату можно '
                                                   'перевести на карту '
                                                   'Сбербанка или по выставленному счёту. Предоплата возвращается при '
                                                   'отмене бронирования, не позднее, чем за 10 дней до заезда.'
                                                   '\nРазмер предоплаты зависит от количества дней прибывания. '
                                                   'Пожалуйста уточняйте при бронировании.',
                             reply_markup=markup)
            bot.send_message(call.message.chat.id, '⭕️ Делаете ли вы скидки при длительном проживании?',
                             reply_markup=markup)
            bot.send_message(call.message.chat.id, 'Конечно! У нас гибкая система скидок: помимо скидок постоянным '
                                                   'Гостям, мы предоставляем дополнительное снижение цен при длительном'
                                                   ' проживании. Кроме того, Гости всегда могут обратиться за '
                                                   'консультацией к нам по бронированию: они подберут '
                                                   'вариант размещения, который подходит именно Вам по '
                                                   'месторасположению, интерьеру и стоимости. Также мы предлагаем самые'
                                                   'выгодные предложения по стоимости за проживание, при заключении '
                                                   'корпоративного договора.', reply_markup=markup)

            bot.send_message(call.message.chat.id, '⭕️ Где нам получить ключи?', reply_markup=markup)
            bot.send_message(call.message.chat.id, 'Накануне заезда мы связываемся с Гостем для обсуждения '
                                                   'деталей маршрута, заселения и прочего. Мы встречаем Гостя в '
                                                   'апартаментах в день приезда и '
                                                   'провожаем проводить в день выезда, (забрать ключи, вернуть залог и '
                                                   'прочее). Таким образом, нашим'
                                                   ' Гостям не приходится тратить время на поездки в наш офис, чтобы '
                                                   'получить или сдать ключи.', reply_markup=markup)
            bot.send_message(call.message.chat.id, '⭕️ Может ли Гость заехать / выехать раньше установленного времени?',
                             reply_markup=markup)
            bot.send_message(call.message.chat.id, 'Если Гостю необходимо заехать раньше и выехать позднее стандартного'
                                                   ' времени заезда/выезда, взимается дополнительная плата '
                                                   '200 рублей/каждый доп. час при заезде с 8 до 14 часов и выезде с '
                                                   '12 до 20 часов. Если же заезд планируется ранее 8.00, а выезд – '
                                                   'позднее 20.00, оплачиваются предыдущие/последующие сутки.',
                             reply_markup=markup)
            bot.send_message(call.message.chat.id, '⭕️ Встретим ли мы Гостя поздно ночью?', reply_markup=markup)
            bot.send_message(call.message.chat.id, 'Мы связываемся с Гостем заранее, и Гость может сообщить '
                                                   'время своего приезда. Администратор встречает Гостя в заранее '
                                                   'оговоренное время. Поздний заезд оплачивается дополнительно от '
                                                   '200 руб.', reply_markup=markup)
            bot.send_message(call.message.chat.id,
                             '⭕️ Предоставляется ли дополнительное спальное место для ребёнка/взрослого?',
                             reply_markup=markup)
            bot.send_message(call.message.chat.id, 'Да, по предварительному запросу при бронировании мы '
                                                   'можем предоставить '
                                                   'дополнительное место. Для маленьких Гостей у нас есть манеж-кровать'
                                                   ', для взрослых предоставляется дополнительное спальное место.',
                             reply_markup=markup)
            bot.send_message(call.message.chat.id, '⭕️ Как и где Гость может забронировать апартаменты 9 Ночей?',
                             reply_markup=markup)
            item1 = types.InlineKeyboardButton('Назад', callback_data='backhelp')
            markup.add(item1)
            bot.send_message(call.message.chat.id, '\n1. На сайте 9ночей.рф'
                                                   '\n2. Через стороннюю площадку или сервис по бронированию, например,'
                                                   ' booking.com , airbnb.ru и пр.'
                                                   '\n3. Позвонив напрямую напрямую нам по телефону +79856846999. '
                                                   '\nВоспользоваться одним из месенджеров WhatsApp, Telegram или Viber'
                                                   ', зракреплённым за телефоном бронирования.',
                             reply_markup=markup)

        elif call.data == 'equipment':
            bot.send_message(call.message.chat.id, '⭕ В каждой из наших квартир обязательно есть всё необходимое для '
                                                   'комфортного проживания. От постельного белья и банных '
                                                   'пренадлежностей до чая и конфет. \nПодробное описание оснащения '
                                                   'каждой квартиры вы сможете увидеть, нажав кнопку "Забронировать '
                                                   'онлайн" при выборе понравившихся апартаментов', reply_markup=markup)
            item1 = types.InlineKeyboardButton('Назад', callback_data='backhelb')
            markup.add(item1)

        elif call.data == 'attractions':
            bot.send_message(call.message.chat.id, '⭕ Достопримечательности и интересные места Сергиева Посада, '
                                                   'и окрестностей', reply_markup=markup)
            item1 = types.InlineKeyboardButton('Назад', callback_data='backhelp')
            markup.add(item1)
            bot.send_message(call.message.chat.id, '🔺Свято-Троицкая Сергиева Лавра \n🔺 Гефсиманско-Черниговский скит.'
                                                   '\n🔺 Пещерный храм.'
                                                   '\n🔺 Парк Скитские пруды ''\n🔺 Покровский Хотьков женский монастырь '
                                                   '(г.Хотьково). \n       Мощи родителей Сергия Радонежского'
                                                   '\n🔺 Музей-усадьба Абрамцево''\n🔺 Музей-Усадьба '
                                                   'Тютчевых-Боратынских в '
                                                   'Мураново \n       (это совсем недалеко)''\n🔺 Гремячий водопад '
                                                   '(Источник '
                                                   'преп. '
                                                   'Сергия)''\n🔺 Комплекс Конный двор (в центре)''\n🔺 Музей Игрушки '
                                                   'обязательно)''\n🔺 Музей советского детства (центр ул.Карла Маркса)'
                                                   '\n🔺 Музей Русской матрешки (рядом с Лаврой, на проспекте)''\n🔺 '
                                                   'Радонеж '
                                                   '(церковь Сергия, источник)''\n🔺 Этно парк Кочевник (в Морозово '
                                                   'рядом'
                                                   ' с Хотьково)''\n🔺 Веревочный парк, тир, пейнтбол, лазертаг в '
                                                   'Морозово''\n        https://adventure-park.ru/''\n🔺 Музей '
                                                   'впечатлений'
                                                   '\n        Московское ш., д. 25',
                             reply_markup=markup)

        elif call.data == 'food':
            item1 = types.InlineKeyboardButton('Назад', callback_data='backhelp')
            markup.add(item1)
            bot.send_message(call.message.chat.id, '🔺 Шеф на районе: \nhttps://www.gyrmanov.com \n '
                                                   '\n🔺 Шашлычок: \nhttps://xn--80aqgcq7cdb.xn--p1acf \n '
                                                   '\n🔺Ресторан Мануфактура: \nhttps://manufaktura1858.ru \n''\n🔺 '
                                                   'Лагманная: \nhttp://lagman-cafe.ru \n'
                                                   '\n🔺 Пироговая ОГОGO: \nhttp://pirogovaya-ogogo.ru \n'''
                                                   '\n🔺 Сержио Пицца: \nhttps://www.sergiopizza.ru \n'
                                                   '\n🔺 Модная столовка "Наша-Раша": \nhttps://instagram.com/stolovka_'
                                                   'nasha_russia?igshid=sgdsh0d3wv0u \n'
                                                   '\n🔺 Домашняя кухня СВЕЖОВ: \nhttps://svezhov.com \n',
                             reply_markup=markup)

        elif call.data == 'admin':
            bot.send_message(call.message.chat.id,
                             '⭕️ Ваш личный администратор Елена всегда на связи.'
                             ' Она с радостью поможет Вам в WhatsApp, Viber, Telegram или по телефону '
                             'разобраться в вопросах, которые могут у Вас возникнуть!')
            bot.send_message(call.message.chat.id, '📞 Телефон для связи: +79856846999')

        elif call.data == 'rooms':
            markup = types.InlineKeyboardMarkup(row_width=2)

            item1 = types.InlineKeyboardButton("Однокомнатные", callback_data='1room')
            item2 = types.InlineKeyboardButton("Двухкомнатные", callback_data='2room')

            markup.add(item1, item2)

            bot.send_message(call.message.chat.id, '🏘Сколько комнат Вам необходимо?', reply_markup=markup)

        elif call.data == 'more 951':
            markup = types.InlineKeyboardMarkup(row_width=1)
            bot.send_photo(call.message.chat.id, open('Photo/Доп фото/1 Уд Ар 95 о/1 Уд Ар 95 о 1.JPG', 'rb'))
            item2 = types.InlineKeyboardButton('Смотреть другие апартаменты', callback_data='rooms')
            item1 = types.InlineKeyboardButton('Забронировать / оплатить онлайн', callback_data='951Wb')
            markup.add(item1, item2)
            bot.send_photo(call.message.chat.id, open('Photo/Доп фото/1 Уд Ар 95 о/1 Уд Ар 95 о 2.JPG', 'rb'),
                           reply_markup=markup)

        elif call.data == 'more 2181':
            markup = types.InlineKeyboardMarkup(row_width=1)
            bot.send_photo(call.message.chat.id, open('Photo/Доп фото/Кр Ар 218 о/Кр Ар 218 о 1.JPG', 'rb'))
            item2 = types.InlineKeyboardButton('Смотреть другие апартаменты', callback_data='rooms')
            item1 = types.InlineKeyboardButton('Забронировать / оплатить онлайн', callback_data='2181Wb')
            markup.add(item1, item2)
            bot.send_photo(call.message.chat.id, open('Photo/Доп фото/Кр Ар 218 о/Кр Ар 218 о 2.JPG', 'rb'),
                           reply_markup=markup)

        elif call.data == 'more 952':
            markup = types.InlineKeyboardMarkup(row_width=1)
            bot.send_photo(call.message.chat.id, open('Photo/Доп фото/1 Уд Ар 95 д/1 Уд Ар 95 д 1.jpg', 'rb'))
            bot.send_photo(call.message.chat.id, open('Photo/Доп фото/1 Уд Ар 95 д/1 Уд Ар 95 д 2.jpg', 'rb'))
            item2 = types.InlineKeyboardButton('Смотреть другие апартаменты', callback_data='rooms')
            item1 = types.InlineKeyboardButton('Забронировать / оплатить онлайн', callback_data='952Wb')
            markup.add(item1, item2)
            bot.send_photo(call.message.chat.id, open('Photo/Доп фото/1 Уд Ар 95 д/1 Уд Ар 95 д 3.jpg', 'rb'),
                           reply_markup=markup)

        elif call.data == 'more 212':
            markup = types.InlineKeyboardMarkup(row_width=1)
            bot.send_photo(call.message.chat.id, open('Photo/Доп фото/Инж 21 д/Инж 21 д 1.jpg', 'rb'))
            bot.send_photo(call.message.chat.id, open('Photo/Доп фото/Инж 21 д/Инж 21 д 2.jpg', 'rb'))
            item2 = types.InlineKeyboardButton('Смотреть другие апартаменты', callback_data='rooms')
            item1 = types.InlineKeyboardButton('Забронировать / оплатить онлайн', callback_data='212Wb')
            markup.add(item1, item2)
            bot.send_photo(call.message.chat.id, open('Photo/Доп фото/Инж 21 д/Инж 21 д 3.jpg', 'rb'),
                           reply_markup=markup)

        elif call.data == 'more 2382':
            markup = types.InlineKeyboardMarkup(row_width=1)
            bot.send_photo(call.message.chat.id, open('Photo/Доп фото/Кр Ар 238 д/Кр Ар 238 д 1.jpg', 'rb'))
            item2 = types.InlineKeyboardButton('Смотреть другие апартаменты', callback_data='rooms')
            item1 = types.InlineKeyboardButton('Забронировать / оплатить онлайн', callback_data='2382Wb')
            markup.add(item1, item2)
            bot.send_photo(call.message.chat.id, open('Photo/Доп фото/Кр Ар 238 д/Кр Ар 238 д 2.jpg', 'rb'),
                           reply_markup=markup)

        elif call.data == 'more 2402':
            markup = types.InlineKeyboardMarkup(row_width=1)
            bot.send_photo(call.message.chat.id, open('Photo/Доп фото/Кр Ар 240 д/Кр Ар 240 д 1.jpg', 'rb'))
            item2 = types.InlineKeyboardButton('Смотреть другие апартаменты', callback_data='rooms')
            item1 = types.InlineKeyboardButton('Забронировать / оплатить онлайн', callback_data='2402Wb')
            markup.add(item1, item2)
            bot.send_photo(call.message.chat.id, open('Photo/Доп фото/Кр Ар 240 д/Кр Ар 240 д 2.jpg', 'rb'),
                           reply_markup=markup)

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)

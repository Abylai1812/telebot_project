import telebot
from telebot import types

BOT_TOKEN = '6855583118:AAFqwYraLGVW57YECgKExepN5Dsvexprnsc'

bot = telebot.TeleBot(BOT_TOKEN)

movies_today = [
    {"title": "Заветное желание", "genre": "мультфильм, музыка, фэнтези, комедия, приключения", "duration": "90 минут", "country": "США", "plot": "Аша — остроумная идеалистка, которая загадывает настолько сильное желание, что на него отвечает космическая сила — маленький шарик безграничной энергии по имени Звезда. Вместе, Аша и Звезда противостоят самому грозному врагу — правителю Росаса, королю Магнифико. Защищая своих близких, Аша доказывает, что, когда воля одного отважного человека соединяется с магией звезд, могут происходить удивительные вещи.", "image_url": "https://new.chaplin.kz/images/uploads/c5e8d97b43ab23fc244891554c1515cc.webp"},
    {"title": "Паранормальные явления: Другое измерение", "genre": "ужасы", "duration": "100 минут", "country": "Тайвань", "plot": "Команда разработчиков игр на основе городских страшилок решает провести тестирование нового продукта в настоящем доме с паранормальными явлениями. По легенде, местные призраки заводят непрошенных гостей в другое измерение и заставляют плутать там в бесконечном лабиринте ужаса. Специалисты по хоррор-играм столкнутся здесь с настоящими потусторонними силами и должны будут переиграть призраков в их собственной игре.", "image_url": "https://new.chaplin.kz/images/uploads/30a870122f9e81b44207264b57e522c8.webp"},
    {"title": "Наполеон", "genre": "биографический, военный, драма, исторический", "duration": "160 минут", "country": "Великобритания, США", "plot": "«Наполеон» — зрелищный эпический боевик, в котором подробно рассказывается о взлёте и падении легендарного французского императора Наполеона Бонапарта (лауреат премии «Оскар» Хоакин Феникс). По-настоящему масштабный фильм легендарного Ридли Скотта показывает тяжёлый путь Бонапарта к власти через призму его изменчивых отношений с единственной настоящей любовью,", "image_url": "https://i.ibb.co/hR5TL7N/image-2023-10-27-T153313-297.webp"},
    {"title": "Елки 10", "genre": "комедия", "duration": "90 минут", "country": "Россия", "plot": "«В новогоднюю ночь всегда есть место чуду, даже если ты вдруг перестал в него верить. Геннадьич, коротающий свой век в доме престарелых под Санкт-Петербургом, обретёт свою настоящую семью. Начинающей блогерше Ларисе из Тюмени предстоит узнать, на что ради своих близких готов решиться её супруг. Марине из Татарстана — научиться любить то, что действительно важно для её мужа. А девушка-геймерша по имени Таня из Нижнего Новгорода поймёт, что настоящая любовь — это совсем не игра. Ведь в самую волшебную ночь года каждый имеет шанс обрести своё персональное счастье.", "image_url": "https://ms1.relax.by/images/d4b21593f3f04b3b118e37d5e68927ff/thumb/w%3D400%2Ch%3D600%2Cq%3D90/afisha_event_photo/5a/2d/26/5a2d266f7850cae1e1641ef53bbe6b8f.jpg"},
     {"title": "Немая ярость", "genre": "боевик", "duration": "100 минут", "country": "США", "plot": "В ходе бандитской разборки случайная пуля лишает счастливую семью маленького сына, а прикрывавшего его отца — голоса. Спустя год усиленной подготовки папа мальчика становится кошмаром для врагов в любой перестрелке, погоне или рукопашной. В годовщину трагедии он намерен разыграть безостановочную симфонию возмездия всем, кто встанет у него на пути. Теперь его действия скажут всё громче любых слов.", "image_url": "https://i.ibb.co/cw7q2CF/image-2023-10-27-T163810-146.webp"},
]

movie_schedule = {
    "Заветное желание": {
        "сегодня": {
            "Kinopar 4 Globus": ["10:10", "12:20"],
            "Kinopark 6 Sputnik": ["11:20", "13:20", "14:40"],
            "Kinpark 11 Esentai": ["14:30", "16:40", "18:40"],
        },
        "завтра": {
            "Kinoplexx 6 Almaty Mall": ["10:00", "11:50", "15:30"],
            "Kinoplexx 7 Aport": ["10:00", "10:40", "12:40"],
            "Kinopark 8 Moskva": ["10:30", "13:00"],
        },
    },
    "Паранормальные явления: Другое измерение": {
        "сегодня": {
            "Kinopark 6 Sputnik": ["10:00"],
            "Kinpark 11 Esentai": ["22:10"],
        },
        "завтра": {
            "Kinoplexx 6 Almaty Mall": ["00:30"],
            "Kinopark 8 Moskva": ["00:10"],
        },
    },
    "Напалеон": {
        "сегодня": {
            "Kinopark 5 Forum": ["23:30"],
            "Kinopark 6 Sputnik": ["23:30"],
            "Kinpark 11 Esentai": ["20:00","22:00","23:00"],
        },
        "завтра": {
            "Kinoplexx 6 Almaty Mall": ["11:30","14:20"],
            "Kinoplexx 7 Aport":["10:00"],
            "Kinopark 8 Moskva": ["15:30","17:30"],
        },
    },
    "Елки 10": {
        "сегодня": {
            "Kinopark 5 Forum": ["23:30"],
            "Kinopark 6 Sputnik": ["23:30"],
            "Kinpark 11 Esentai": ["15:10","12:30"],
        },
        "завтра": {
            "Kinoplexx 6 Almaty Mall": ["11:30"],
            "Kinoplexx 7 Aport":["13:10"],
            "Kinopark 8 Moskva": ["11:20","21:50"],
        },
    },
    "Немая ярость": {
        "сегодня": {
            "Kinopark 5 Forum": ["21:00"],
            "Kinopark 6 Sputnik": ["22:30"],
            "Kinpark 11 Esentai": ["14:10","17:30"],
        },
        "завтра": {
            "Kinoplexx 6 Almaty Mall": ["18:30"],
            "Kinoplexx 7 Aport":["20:10"],
            "Kinopark 8 Moskva": ["19:20","21:30"],
        },
    },
}

movie_ticket_prices = {
    "Заветное желание": {
        "детский": 900,
        "студенческий": 1300,
        "взрослый": 1700,
    },
    "Паранормальные явления: Другое измерение": {
        "детский": "18+ Детям нельзя смотреть",
        "студенческий": 2000,
        "взрослый": 3000,
    },
    "Напалеон": {
        "детский": "18+ Детям нельзя смотреть",
        "студенческий": 1700,
        "взрослый": 1900,
    },
    "Елки 10": {
        "детский": 900,
        "студенческий": 1300,
        "взрослый": 1700,
    },
    "Немая ярость": {
        "детский": 1300,
        "студенческий": 1600,
        "взрослый": 2300,
    },
}

@bot.message_handler(commands=['start'])
def start(message):
    show_movie_selection(message)

def show_movie_selection(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for movie in movies_today:
        button = types.KeyboardButton(movie["title"])
        markup.add(button)

    bot.send_message(message.chat.id, "Сегодня в кино", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_movie_selection(message):
    for movie in movies_today:
        if message.text == movie["title"]:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            details_button = types.KeyboardButton("Описание")
            schedule_button = types.KeyboardButton("Расписание")
            back_button = types.KeyboardButton("Назад")

            markup.add(details_button, schedule_button, back_button)

            bot.send_message(message.chat.id, f'Вы выбрали "{movie["title"]}"', reply_markup=markup)
            bot.register_next_step_handler(message, handle_movie_options, movie)

def handle_movie_options(message, selected_movie):
    if message.text == "Описание":
        details_text = f"Жанр: {selected_movie['genre']}\nПродолжительность: {selected_movie['duration']}\nСтрана: {selected_movie['country']}\n\nСюжет: {selected_movie['plot']}"
        bot.send_message(message.chat.id, details_text)
        bot.send_photo(message.chat.id, selected_movie['image_url'])
        show_movie_selection(message)
    elif message.text == "Расписание":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for day, theaters in movie_schedule[selected_movie['title']].items():
            button = types.KeyboardButton(day)
            markup.add(button)
        bot.send_message(message.chat.id, "Выберите день:", reply_markup=markup)
        bot.register_next_step_handler(message, handle_day_selection, selected_movie)

def handle_day_selection(message, selected_movie):
    selected_day = message.text
    theaters = movie_schedule[selected_movie['title']].get(selected_day, {})

    if theaters:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for theater, times in theaters.items():
            button = types.KeyboardButton(theater)
            markup.add(button)
        bot.send_message(message.chat.id, "Выберите кинотеатр:", reply_markup=markup)
        bot.register_next_step_handler(message, handle_theater_selection, selected_movie, selected_day)
    else:
        bot.send_message(message.chat.id, "Извините, на выбранный день нет расписания.")
        show_movie_selection(message)

def handle_theater_selection(message, selected_movie, selected_day):
    selected_theater = message.text
    times = movie_schedule[selected_movie['title']].get(selected_day, {}).get(selected_theater, [])

    if times:
        prices_text = "\n\nСтоимость билетов:\n"
        for category, price in movie_ticket_prices[selected_movie['title']].items():
            prices_text += f"{category}: {price} тг\n"
        bot.send_message(message.chat.id, f"Расписание на {selected_day} в кинотеатре {selected_theater}:\n{', '.join(times)}" + prices_text)
    else:
        bot.send_message(message.chat.id, "Извините, на выбранный день в выбранном кинотеатре нет сеансов.")

    show_movie_selection(message)

bot.polling()
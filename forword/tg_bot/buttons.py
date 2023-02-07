from telegram import KeyboardButton, ReplyKeyboardMarkup


def btns(type=None):
    btn = []
    if type == "menu":
        btn = [
            [KeyboardButton('Lokatsiya📍'), KeyboardButton('Instagram')],
            [KeyboardButton("www.forward_academy.com"), KeyboardButton('Telegram')],
        ]

    elif type == 'contact':
        btn = [
            [KeyboardButton('Raqamni yuborish 📲', request_contact=True)]
        ]

    return ReplyKeyboardMarkup(btn, resize_keyboard=True)


def admin_btn(type=None):
    btn = []
    if type == "admin_menu":
        btn = [
            [KeyboardButton("Reklama yuborish"), KeyboardButton("Users 👤")],
            [KeyboardButton("Botga qaytish 🏘")]
        ]
    elif type == 'conf':
        btn = [
            [KeyboardButton("Ha"), KeyboardButton("Yo'q")]
        ]

    return ReplyKeyboardMarkup(btn, resize_keyboard=True)

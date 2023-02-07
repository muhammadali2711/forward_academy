from tg_bot.buttons import btns
from tg_bot.models import Log, User


def start(update, context):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    tg_user = User.objects.filter(user_id=user.id).first()

    if not tglog:
        tglog = Log()
        tglog.user_id = user.id
        tglog.save()

    log = tglog.messages

    if not tg_user:
        tg_user = User()
        tg_user.user_id = user.id
        tg_user.username = user.username
        tg_user.first_name = user.first_name
        tg_user.save()
        log['state'] = 1
        update.message.reply_html(
            f"Assalomu alaykum <b>Forward Academy</b> botiga xush kelibsiz.\nIltimos ismingizni yozib qoldiring ☺️")

    else:
        if log['state'] >= 10:
            log.clear()
            log['state'] = 10
            update.message.reply_text("O'zingizni qizitirgan malumot olishingiz mumkin 📎", reply_markup=btns('menu'))

        else:
            log['state'] = 1
            update.message.reply_html(
                f"Assalomu alaykum <b>Forward Academy</b> botiga xush kelibsiz.\nIltimos ismingizni yozib qoldiring ☺️")

    tglog.messages = log
    tglog.save()


def message_handler(update, context):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    tg_user = User.objects.filter(user_id=user.id).first()
    log = tglog.messages

    msg = update.message.text

    if log['state'] == 1:
        if msg.isalpha():
            log['name'] = msg
            log['state'] = 2
            update.message.reply_text("Siz bilan bog'lanishimiz uchun raqamingizni kiriting 📞",
                                      reply_markup=btns('contact'))
        else:
            update.message.reply_text("Iltimos ismingizni text formatida kiriting. !!!")
    elif log['state'] == 2:
        update.message.reply_text('Iltimos Raqamni yuborish 📲 tugmasini bosing 👇')
        print(msg)

    if msg == "Lokatsiya📍":
        log['state'] = 10
        update.message.reply_text("https://yandex.uz/maps/-/CCUruXCP3B")

    elif msg == "Instagram":
        log['state'] = 10
        update.message.reply_text("https://www.instagram.com/forwardacademy.uz/")

    elif msg == 'www.forward_academy.com':
        log['state'] = 10
        update.message.reply_text("oka saytila ishga tushsa link ulavormiz muamomas ")

    elif msg == 'Telegram':
        log['state'] = 10
        update.message.reply_text("https://t.me/ForwardAcademy_uz")

    tglog.messages = log
    tglog.save()


def contact_handler(update, context):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    tg_user = User.objects.filter(user_id=user.id).first()
    log = tglog.messages

    msg = update.message.contact
    contact = update.message.contact
    log['contact'] = contact.phone_number

    if log['state'] == 2:
        tg_user.phone = log['contact']
        tg_user.save()
        log.clear()
        log['state'] = 10
        update.message.reply_text("Sizning ma`lumotlaringiz saqlandi siz bilan tez orada bog'lanamiz!🥳", reply_markup=btns('menu'))

    tglog.messages = log
    tglog.save()
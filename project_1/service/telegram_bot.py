import django
import telebot
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service.settings')
django.setup()

from django.conf import settings

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))


def setup_database():

    db_config = settings.DATABASES['default']
    db_url = f"postgresql://{db_config['USER']}:{db_config['PASSWORD']}@{db_config['HOST']}:{db_config['PORT']}/{db_config['NAME']}"
    engine = create_engine(db_url)
    session = sessionmaker(bind=engine)
    return session


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Привет! Для регистрации в системе отправьте мне ваш номер телефона.\n\n"
        "Формат: +79123456789 или 89123456789"
    )


@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text.strip()

    if any(char.isdigit() for char in text) and len(text) >= 10:
        process_phone_number(message, text)
    else:
        bot.send_message(
            message.chat.id,
            "Пожалуйста, отправьте номер телефона в формате: +79123456789"
        )


def process_phone_number(message, phone):
    cleaned_phone = ''.join(filter(str.isdigit, phone))
    if cleaned_phone.startswith('7') or cleaned_phone.startswith('8'):
        cleaned_phone = '7' + cleaned_phone[1:]

    session = setup_database()
    if not session:
        bot.send_message(message.chat.id, "Ошибка системы. Попробуйте позже.")
        return

    with session() as session:
        query = text("""
            UPDATE accounts_customuser 
            SET telegram_id = :telegram_id 
            WHERE phone LIKE :phone 
            RETURNING id, username
        """)

        result = session.execute(
            query,
            {'telegram_id': message.chat.id, 'phone': f'%{cleaned_phone}%'}
        ).fetchone()

        if result:
            session.commit()
            bot.send_message(
                message.chat.id,
                f"Вы успешно зарегистрированы в системе!\n\n"
                f"Ваш Telegram ID: {message.chat.id}\n"
                f"Привязан к пользователю: {result[1]}"
            )
        else:
            bot.send_message(
                message.chat.id,
                "Пользователь с таким номером телефона не найден.\n\n"
                "Проверьте номер или обратитесь к администратору."
            )


def send_notification(chat_id, text):
    try:
        bot.send_message(chat_id, text)
        return True
    except Exception as e:
        return False


def run_bot():
    bot.polling(none_stop=True)

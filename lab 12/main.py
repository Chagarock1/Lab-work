import telebot
from telebot import types
import requests
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

# Головне меню
menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add("⛅ Погода (Івано-Франківськ)", "🏙 Інше місто")
menu.add("ℹ️ Норма тиску", "🌐 Сайт погоди")
menu.add("🤖 Про бота")


def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=j1&lang=uk"
        headers = {"User-Agent": "TelegramBot"}
        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code == 200:
            data = response.json()
            current = data["current_condition"][0]

            temp = int(current["temp_C"])
            feels_like = current["FeelsLikeC"]
            humidity = current["humidity"]
            wind = current["windspeedKmph"]

            # Отримуємо опис погоди
            if "lang_uk" in current and current["lang_uk"]:
                desc = current["lang_uk"][0]["value"]
            else:
                desc = current["weatherDesc"][0]["value"]

            # Логіка визначення поради щодо одягу
            if temp < 0:
                advice = "На вулиці мороз, одягайте теплу куртку, шапку та рукавиці."
            elif 0 <= temp < 15:
                advice = "Досить прохолодно, краще одягнути куртку або пальто."
            else:
                advice = "Погода комфортна і тепла, підійде легкий одяг."

            message_text = (
                f"📍 Місто: {city.title()}\n"
                f"🌡 Температура: {temp}°C (відчувається як {feels_like}°C)\n"
                f"☁️ Стан: {desc}\n"
                f"💧 Вологість: {humidity}%\n"
                f"💨 Вітер: {wind} км/год\n\n"
                f"💡 Порада: {advice}"
            )
            return message_text
        else:
            return None
    except Exception:
        return None


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    user_name = message.from_user.first_name
    bot.send_message(
        message.chat.id,
        f"Привіт, {user_name}! Я погодний бот.\n"
        "Оберіть потрібну дію на кнопках або просто напишіть назву міста:",
        reply_markup=menu
    )


# Обробка інлайн-кнопки
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    bot.answer_callback_query(call.id)
    if call.data == "bot_features":
        bot.send_message(
            call.message.chat.id,
            "📌 Особливості роботи бота:\n"
            "• Дані оновлюються в реальному часі через сервіс wttr.in\n"
            "• Працює безкоштовно і без реєстрацій\n"
            "• Підтримує пошук будь-якого міста світу"
        )


# Обробка тексту та кнопок
@bot.message_handler(content_types=["text"])
def handle_text(message):
    text = message.text.strip()

    if text == "⛅ Погода (Івано-Франківськ)":
        result = get_weather("Івано-Франківськ")
        if result:
            bot.send_message(message.chat.id, result)
        else:
            bot.send_message(message.chat.id, "Не вдалося отримати дані про погоду.")

    elif text == "🏙 Інше місто":
        bot.send_message(message.chat.id, "Введіть назву міста (наприклад: Львів, Київ, Коломия):")

    elif text == "ℹ️ Норма тиску":
        bot.send_message(
            message.chat.id,
            "ℹ️ Нормальний атмосферний тиск для людини становить 760 мм рт. ст. (1013 гПа)."
        )

    elif text == "🌐 Сайт погоди":
        inline_kb = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("Укргідрометцентр ↗", url="https://meteo.gov.ua/")
        inline_kb.add(btn)
        bot.send_message(message.chat.id, "Офіційний погодний сайт України:", reply_markup=inline_kb)

    elif text == "🤖 Про бота":
        about_text = (
            "Погодний помічник (Weather Bot)\n\n"
            "Можливості бота:\n"
            "- Швидкий прогноз для Івано-Франківська в один клік\n"
            "- Пошук поточної погоди для будь-якого міста\n"
            "- Відображення температури, вологості, вітру та хмарності\n"
            "- Поради щодо підбору одягу під погоду\n\n"
            "Технології: Python 3, telebot, requests, wttr.in API\n"
            "Лабораторна робота №12"
        )
        inline_kb = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("Дізнатися більше", callback_data="bot_features")
        inline_kb.add(btn)
        bot.send_message(message.chat.id, about_text, reply_markup=inline_kb)

    else:
        result = get_weather(text)
        if result:
            bot.send_message(message.chat.id, result)
        else:
            bot.send_message(
                message.chat.id,
                "⚠️ Місто не знайдено або команда невідома. Перевірте правильність написання."
            )


if __name__ == "__main__":
    print("Бот успішно запущений")
    bot.infinity_polling(skip_pending=True)

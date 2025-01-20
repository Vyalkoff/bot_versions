import json
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

# Загрузим данные из файла JSON
def load_routes():
    with open('routes.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# Функция для обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Отправьте код маршрута, и я найду для него ссылку на 2GIS.')

# Функция для обработки текста (кода маршрута)
def handle_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text.strip()

    # Попробуем преобразовать текст в число
    try:
        route_code = int(user_input)
    except ValueError:
        update.message.reply_text('Пожалуйста, отправьте числовой код маршрута.')
        return

    # Ищем ссылку для данного кода маршрута
    routes = load_routes()
    link = None

    for route in routes:
        if route['КодМаршрута'] == route_code:
            link = route['Ссылка']
            break

    # Отправляем результат пользователю
    if link:
        update.message.reply_text(f'Ссылка на маршрут {route_code}: {link}')
    else:
        update.message.reply_text(f'Маршрут с кодом {route_code} не найден.')

# Основная функция для запуска бота
def main() -> None:

    token = '6048932941:AAG3bb9C8sPcZUp4KnisNBcxoMRCYtDr8z0'

    updater = Updater(token)

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик сообщений
    dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, handle_message))

    # Запускаем бота
    updater.start_polling()

    # Работаем до остановки
    updater.idle()

if __name__ == '__main__':
    main()

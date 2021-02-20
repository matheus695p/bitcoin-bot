import requests


def send_message_telegram(message, fecha, nombre="!!!"):
    fecha = fecha.strftime("%d-%b-%Y %H:%M:%S")
    # filtrar por el evento
    first_line = f"BITCOIN ALERTA {nombre}"
    second_line = "Fecha actual: " + fecha
    final_message = first_line + '\n' + second_line + '\n' + message
    telegram_bot_sendtext(final_message)


def telegram_bot_sendtext(bot_message):
    bot_token = "1653175116:AAH7bvLbiDSIwHuoW-FYXoE5Usj6IORXsQA"
    bot_chatID = '-546189367'
    send_text = ('https://api.telegram.org/bot' + bot_token +
                 '/sendMessage?chat_id=' + bot_chatID +
                 '&parse_mode=Markdown&text=' + bot_message)
    response = requests.get(send_text)
    return response.json()

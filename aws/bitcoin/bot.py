import json
import requests


def send_message_telegram(message, fecha, nombre="!!!"):
    """
    Customizar el mensaje a telegram
    Parameters
    ----------
    message : string
        mensaje de telegram.
    fecha : datetime
        fecha actual.
    nombre : string, optional
        alguna alerta en especifico. The default is "!!!".
    Returns
    -------
    Mandar mensaje.

    """
    fecha = fecha.strftime("%d-%b-%Y %H:%M:%S")
    # filtrar por el evento
    first_line = f"BITCOIN INFO {nombre}"
    second_line = "Fecha actual: " + fecha
    final_message = first_line + '\n' + second_line + '\n' + message
    telegram_bot_sendtext(final_message)


def telegram_bot_sendtext(bot_message):
    """
    Mandar mensaje de texto
    Parameters
    ----------
    bot_message : string
        mandar mensaje a un .

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    with open('keys.json') as json_file:
        dict_ = json.load(json_file)
        bot_token = dict_["bot_token"]
        bot_chat_id = dict_["bot_chat_id"]

    send_text = ('https://api.telegram.org/bot' + bot_token +
                 '/sendMessage?chat_id=' + bot_chat_id +
                 '&parse_mode=Markdown&text=' + bot_message)
    response = requests.get(send_text)
    return response.json()

from datetime import datetime
from module import (ask_coindesk_price, ask_coindesk_porcentual_increase)
from bot import send_message_telegram


def handler(event, context):
    "Lambda handler para implementar"
    now = datetime.now().replace(microsecond=0)
    request = ask_coindesk_price()
    variation = ask_coindesk_porcentual_increase()
    text_1 =\
        f"precio bitcoin: {round(request, 9)} dolares"
    text_2 =\
        f"aumento procentual: {variation}"
    message = text_1 + '\n' + text_2
    print(message)
    send_message_telegram(message, now)

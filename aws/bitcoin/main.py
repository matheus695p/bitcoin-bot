from datetime import datetime
from module import (ask_coindesk_price, ask_coindesk_porcentual_increase)
from bot import (send_message_telegram, create_message)


def handler(event, context):
    "Lambda handler para implementar"
    now = datetime.now().replace(microsecond=0)

    cryptos = ["bitcoin", "ethereum", "xrp", "stellar", "cardano", "polkadot",
               "dogecoin", "litecoin", "neo"]
    final_message = ""
    for crypto in cryptos:
        price = ask_coindesk_price(crypto=crypto)
        variation = ask_coindesk_porcentual_increase(crypto=crypto)
        message = create_message(price, variation,
                                 crypto=crypto.upper())
        final_message = final_message + "\n" + message
    print(final_message)
    send_message_telegram(final_message, now)

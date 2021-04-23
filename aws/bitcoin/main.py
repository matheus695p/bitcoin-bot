from datetime import datetime
from module import (ask_coindesk_price, ask_coindesk_porcentual_increase)
from bot import (send_message_telegram, create_message)


def handler(event, context):
    "Lambda handler para implementar"
    now = datetime.now().replace(microsecond=0)
    bitcoin_price = ask_coindesk_price(crypto="bitcoin")
    bitcoin_variation = ask_coindesk_porcentual_increase(crypto="bitcoin")

    ethereum_price = ask_coindesk_price(crypto="ethereum")
    ethereum_variation = ask_coindesk_porcentual_increase(crypto="ethereum")
    # mensajes
    bitcoin_message = create_message(bitcoin_price, bitcoin_variation,
                                     crypto="BTC")
    ethereum_message = create_message(ethereum_price, ethereum_variation,
                                      crypto="ETH")
    # Mandar mensaje
    message = bitcoin_message + "\n" + ethereum_message
    print(message)
    send_message_telegram(message, now)

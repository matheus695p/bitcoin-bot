import time
import pandas as pd
from datetime import datetime
from src.module import (ask_google_general_questions, add_lagged_values,
                        get_close_price, parser)
from src.bot import send_message_telegram


def main():
    # historial de precios
    historial = []
    contador = 0
    # frecuencia de la consulta cada 60 segundos
    freq_consulta = 60
    min_iteraciones = 10
    while True:
        print("iteracion número: ", contador)
        ahora = datetime.now().replace(microsecond=0)
        consulta = parser(ask_google_general_questions())
        historial.append([ahora, consulta])
        texto =\
            f"precio bitcoin: {round(consulta, 9)} dolares"
        if contador <= min_iteraciones:
            pass
            send_message_telegram(texto, ahora)
        else:
            fecha, valor = get_close_price()
            analisis = pd.DataFrame(
                historial, columns=["fecha", "valor_dolar"])
            analisis["diff"] = analisis["valor_dolar"].diff()
            analisis["media_movil"] = analisis["valor_dolar"].rolling(5).mean()
            analisis = add_lagged_values(analisis, n=10)
            # implementar inteligencia sobre logicas de vender o comprar
            analisis["valor_cierre"] = valor

            send_message_telegram(texto, ahora)
        contador += 1
        # tiempo entre consultas
        time.sleep(freq_consulta)


if __name__ == '__main__':
    main()

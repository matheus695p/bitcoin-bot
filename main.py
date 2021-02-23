import time
import pandas as pd
from datetime import datetime
from src.module import (ask_coindesk_price, add_lagged_values,
                        get_close_price, ask_coindesk_porcentual_increase)
from src.bot import send_message_telegram


def main():
    # historial de precios
    historial = []
    contador = 0
    # frecuencia de la consulta cada 60 segundos
    freq_consulta = 10
    min_iteraciones = 10
    while True:
        print("iteracion número: ", contador)
        ahora = datetime.now().replace(microsecond=0)
        consulta = ask_coindesk_price()
        variacion = ask_coindesk_porcentual_increase()
        historial.append([ahora, consulta])
        texto1 =\
            f"precio bitcoin: {round(consulta, 9)} dolares"
        texto2 =\
            f"aumento procentual: {variacion}"
        texto = texto1 + '\n' + texto2

        if contador <= min_iteraciones:
            pass
            # send_message_telegram(texto, ahora)
        else:
            fecha, valor = get_close_price()
            analisis = pd.DataFrame(
                historial, columns=["fecha", "valor_dolar"])
            analisis["diff"] = analisis["valor_dolar"].diff()
            analisis["media_movil"] = analisis["valor_dolar"].rolling(5).mean()
            analisis = add_lagged_values(analisis, n=10)
            # implementar inteligencia sobre logicas de vender o comprar
            analisis["valor_cierre"] = valor

            # send_message_telegram(texto, ahora)
        contador += 1
        # tiempo entre consultas
        time.sleep(freq_consulta*2)


if __name__ == '__main__':
    main()

import pandas as pd
import time
from datetime import datetime
from src.module import (get_bt_price_pesos, add_lagged_values,
                        get_close_price)
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
        consulta = get_bt_price_pesos()
        historial.append([ahora, consulta])
        texto =\
            f"precio bitcoin: {round(consulta / 10**6, 9)} Millones de pesos"
        if contador <= min_iteraciones:
            pass
            send_message_telegram(texto, ahora)
        else:
            fecha, valor = get_close_price()
            analisis = pd.DataFrame(
                historial, columns=["fecha", "valor_pesos"])
            analisis["diff"] = analisis["valor_pesos"].diff()
            analisis["media_movil"] = analisis["valor_pesos"].rolling(5).mean()
            analisis = add_lagged_values(analisis, n=10)
            # implementar inteligencia sobre logicas de vender o comprar
            analisis["valor_cierre"] = valor * 750

            send_message_telegram(texto, ahora)
        contador += 1
        # tiempo entre consultas
        time.sleep(freq_consulta)


if __name__ == '__main__':
    main()

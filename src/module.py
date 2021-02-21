import requests
import pandas_datareader as pdr
from datetime import datetime, timedelta
from bs4 import BeautifulSoup


def ask_google(coin="bitcoin"):
    # url donde ir a buscar la info de google
    url = "https://www.google.com/search?q="+coin+"+precio"
    print(url)
    # hacer request de html
    HTML = requests.get(url)
    # parsear html
    soup = BeautifulSoup(HTML.text, 'html.parser')
    # encontrar el div que tenga el precio
    text = soup.find("div", attrs={'class': 'BNeawe iBp4i AP7Wnd'}).find(
        "div", attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    print(text)
    return text


def ask_coindesk_price():
    url = "https://www.coindesk.com/price/bitcoin/"
    print(url)
    # hacer request de html
    HTML = requests.get(url)
    # parsear html
    soup = BeautifulSoup(HTML.text, 'html.parser')
    # encontrar el div que tenga el precio
    job_elems = soup.find_all('section', class_='default global-content')
    for job_elem in job_elems:
        precio = job_elem.find('div', class_='price-large').text
        print(precio)
    precio = precio.replace(",", "").replace("$", "")
    return float(precio)


def ask_coindesk_porcentual_increase():
    url = "https://www.coindesk.com/price/bitcoin/"
    print(url)
    # hacer request de html
    HTML = requests.get(url)
    # parsear html
    soup = BeautifulSoup(HTML.text, 'html.parser')
    # encontrar el div que tenga el precio
    job_elems = soup.find_all('section', class_='default global-content')
    for job_elem in job_elems:
        variacion = job_elem.find('div', class_='percent-change-medium').text
        print(variacion)
    variacion = variacion.replace("%", "")
    variacion = variacion + " %"
    return variacion


def ask_google_general_questions(pregunta="precio del bitcoin en dolares"):
    # url donde ir a buscar la info de google
    url = "https://www.google.com/search?q=" + pregunta
    print(url)
    # hacer request de html
    HTML = requests.get(url)
    # parsear html
    soup = BeautifulSoup(HTML.text, 'html.parser')
    # encontrar el div que tenga el precio
    text = soup.find("div", attrs={'class': 'BNeawe iBp4i AP7Wnd'}).find(
        "div", attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    print(text)
    return text


def parser(price_text):
    print(price_text)
    text = price_text.replace(",", "")
    index = text.index('.')
    text = text[0:index]
    base = float(''.join(filter(str.isdigit, text)))
    decimal = price_text[index+1:index+4]
    decimal = float("0" + decimal)
    precio = base + decimal
    return precio


def get_bt_price_pesos():
    # sacar el precio del bitcoin en unidad de fomento
    precio_bt = ask_google(coin="bitcoin")
    precio_bt = parser(precio_bt)
    # sacar el precio de la unidad de fomento
    pricio_uf = ask_google(coin="unidad de fomento")
    pricio_uf = parser(pricio_uf)
    # sacar el precio del bitcoin en pesos
    precio_pesos = pricio_uf * precio_bt
    print(precio_pesos)
    return precio_pesos


def add_lagged_values(df, n=5):
    # crear columnas a lo maldito para analizar tendencia al alza o baja
    for i in range(1, n+1):
        column = f"lag_value_{i}"
        print(i, column)
        df[column] = df["valor_dolar"].shift(i)
    return df


def get_close_price():
    # fecha de inicio de la consulta
    end_date = datetime.now().replace(microsecond=0)
    start_date = end_date - timedelta(days=30)
    # lectura del dataframe como pdr
    btc_data = pdr.get_data_yahoo(['BTC-USD'],
                                  start=start_date,
                                  end=end_date)
    btc_data = btc_data['Close']
    btc_data.reset_index(drop=False, inplace=True)
    btc_data.rename(columns={"Date": "fecha", "BTC-USD": "valor"},
                    inplace=True)
    fecha = btc_data["fecha"].iloc[-1]
    valor = btc_data["valor"].iloc[-1]
    precio_dolar = ask_google(coin="dolar")
    precio_dolar = parser(precio_dolar)
    return fecha, valor


def diff_lagged_values(df, column="valor_dolar", n=5):
    # crear columnas a lo maldito para analizar tendencia al alza o baja
    for i in range(1, n+1):
        column = f"lag_value_{i}"
        df[column] = df["valor_dolar"].shift(i)
    return df

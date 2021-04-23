import requests
# import pandas_datareader as pdr
# from datetime import datetime, timedelta
from bs4 import BeautifulSoup


def ask_google(coin="bitcoin"):
    """
    Preguntar el precio del bitcoin en google

    Parameters
    ----------
    coin : string, optional
        DESCRIPTION. The default is "bitcoin".

    Returns
    -------
    text : string
        precio del bitcoin.

    """
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
    """
    Preguntar el precio del bitcoin en www.coindesk.com

    Returns
    -------
    string
        precio del bitcoin.

    """
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
    """
    Dentro de la pregunta preguntar también por la variación porcentual
    Returns
    -------
    variacion : string
        variación porcentual del bitcoin.

    """
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


def parser(price_text):
    """
    Parsear el string que recibimos de la consulta

    Parameters
    ----------
    price_text : string
        precio recién preguntado.

    Returns
    -------
    precio : string
        precio en flotante.
    """
    print(price_text)
    text = price_text.replace(",", "")
    index = text.index('.')
    text = text[0:index]
    base = float(''.join(filter(str.isdigit, text)))
    decimal = price_text[index+1:index+4]
    decimal = float("0" + decimal)
    precio = base + decimal
    return precio


def add_lagged_values(df, n=5):
    """
    En el caso del precio cerrado del bitcoin sacar los n valores anteriores

    Parameters
    ----------
    df : dataframe
        precio del bitocin, con las distintas fases que tiene.
    n : TYPE, optional
        string. The default is 5.

    Returns
    -------
    df : TYPE
        DESCRIPTION.

    """
    # crear columnas a lo maldito para analizar tendencia al alza o baja
    for i in range(1, n+1):
        column = f"lag_value_{i}"
        # print(i, column)
        df[column] = df["valor_dolar"].shift(i)
    return df


# def get_close_price():
#     """
#     Obtener el precio de cierre del mercado

#     Returns
#     -------
#     fecha : datetime
#         fecha de cierre.
#     valor :  float
#         varlor del bitcoin.

#     """
#     # fecha de inicio de la consulta
#     end_date = datetime.now().replace(microsecond=0)
#     start_date = end_date - timedelta(days=30)
#     # lectura del dataframe como pdr
#     btc_data = pdr.get_data_yahoo(['BTC-USD'],
#                                   start=start_date,
#                                   end=end_date)
#     btc_data = btc_data['Close']
#     btc_data.reset_index(drop=False, inplace=True)
#     btc_data.rename(columns={"Date": "fecha", "BTC-USD": "valor"},
#                     inplace=True)
#     fecha = btc_data["fecha"].iloc[-1]
#     valor = btc_data["valor"].iloc[-1]
#     precio_dolar = ask_google(coin="dolar")
#     precio_dolar = parser(precio_dolar)
#     return fecha, valor

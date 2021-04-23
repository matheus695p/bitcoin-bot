from tradingview_ta import TA_Handler, Interval
# from tradingview_ta import Exchange

cryptos = ["BTCUSDT", "ETHUSD"]

for crypto in cryptos:
    print("Sancando info de:", crypto, "...")
    handler = TA_Handler(
        symbol=crypto,
        screener="crypto",
        exchange="binance",
        interval=Interval.INTERVAL_1_DAY
    )

    handler = TA_Handler()
    handler.set_symbol_as("BTCUSDT")
    handler.set_exchange_as_crypto_or_stock("binance")
    handler.set_screener_as_crypto()
    handler.set_interval_as(Interval.INTERVAL_1_DAY)

    analysis = handler.get_analysis()

    summary = analysis.summary
    oscillators = analysis.oscillators
    moving_averages = analysis.moving_averages
    indicators = analysis.indicators
    time = analysis.time

    print("Resumen:", summary)
    print("Osciladores:", oscillators)
    print("Medias Moviles:", moving_averages)
    print("Precios:", indicators)
    print("Tiempo:", time)

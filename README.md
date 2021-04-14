![Build Status](https://www.repostatus.org/badges/latest/active.svg)

# bitcoin
La idea del repo, cambió, ahora metí plata en las cryptos:

La idea es sacar info de trading desde acá:


* https://www.tradingview.com/


Ya sea mandandolas a telegram o whatsapp, la idea es tener el precio a tiempo real de cada una de las cryptos que estoy comprando, tendencias diarias, es decir si comviene comprar, vender o quedarse con lo que estámos y alertas en casos especifícos como que el precio de alguna crypto se venga muy a abajo y haya que vender lo más rápido posible.


Entonces:
* Precio a tiempo real en un grupo
* Tendencias cada hora en un grupo
* Alertas de caídas brutales en otro grupo

De esta manera se pueden silenciar los dos primeros y quedarse solo con el tercero, pero tener toda la info disponible para cuando se queira hacer.



## setup del bot
Pasos a seguir para hacer ambiente de trabajo del bot:
```sh
$ git clone https://github.com/matheus695p/bitcoin.git
$ cd bitcoin
$ echo instalar los requirements, si usas conda, haz el conda activate del ambiente
$ pip install -r requirements.txt
$ python main.py
```

descripción:
 
```sh
│   .gitignore
│   main.py            ------> archivo a ajecutar en un pc o servidor
│   README.md
│   requirements.txt
└───src
    │   bot.py        ------> funciones del bot
    │   module.py     ------> funciones de las consultas a google acerca del precio del bitcoin

```

# bitcoin
bot de telegram con alertas personalizadas para un par de jiles que están comprando bitcoin y viendo cada 5 minutos el precio

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

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

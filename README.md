# turbofan-engines-predictive-mantenaince
end-to-end proyecto de mantenimiento predictivo, proyecto pensado para ser ejecutado on-premise 

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## setup del proyecto 
Este trabajo se desarrollará en dos ramas:
-  main: rama de cara al cliente
-  develop: rama de desarrollo de las nuevas funcionalidades
Por lo tanto, todas las personas que contribuyan en el desarrollo del repo, deben hacer chechout a la rama de develop y trabjar única y exclusivamente en esta rama.
La rama main, no se tocará y solo se harán las transferencias vía Pull Request (PR), en el cual los owners del repo deberán aprobar.

Pasos a seguir para hacer ambiente de trabajo del producto:
```sh
$ git clone https://github.com/matheus695p/turbofan-engines-predictive-mantenaince.git
$ cd turbofan-engines-predictive-mantenaince
$ echo instalar los requirements
$ pip install -r requirements.txt
```

descripción:
  - baseline de modelo, definición de RUL como una parte constante más lineal
  - análisis de series de tiempo
 

```sh
│   README.md
│   readme.txt
│   requirements.txt
│
├───codes
│   ├───baseline
│   │       exploratory_baseline.py
│   │       __init__.py
│   │
│   ├───survival-analysis
│   │       survival.py
│   │       __init__.py
│   │
│   └───time-series
│           lagging_test.py
│           stationary_lagging.py
│           __init__.py
│
├───data
│       RUL_FD001.txt
│       RUL_FD002.txt
│       RUL_FD003.txt
│       RUL_FD004.txt
│       test_FD001.txt
│       test_FD002.txt
│       test_FD003.txt
│       test_FD004.txt
│       train_FD001.txt
│       train_FD002.txt
│       train_FD003.txt
│       train_FD004.txt
│
├───documents
│       Damage Propagation Modeling.pdf
│
└───src
    │   turbo_fan_module.py
    │   __init__.py
```

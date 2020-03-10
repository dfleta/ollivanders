# API REST con Flask y Mongo Atlas

## Instala el proyecto

### Manual

- Instala virtualenv:

    `$ sudo apt-get install python3.6-venv`

- Crea el directorio y sitúate en él:

    ```bash
    $ mkdir ./ollivanders
    $ cd ollivanders
    ```

- Clona el projecto:

    `$ git clone https://github.com/dfleta/api-rest-gildedrose.git`

- Inicializa el entorno virtual e instala dependencias:

    ```bash
    $ python3.6 -m venv venv
    $ source venv/bin/activate
    (venv) $ pip3 install -r requirements.txt
    ```

### Como distribución

- Crea el directorio y sitúate en él:

    ```bash
    $ mkdir ./ollivanders
    $ cd ollivanders
    ```

- Clona el projecto:

    `git clone https://github.com/dfleta/api-rest-gildedrose.git`

- Inicializa el entorno virtual y actívalo.

    ```bash
    $ python3.6 -m venv venv
    $ source venv/bin/activate
    ```
    
- Instala el proyecto:

    `$ pip3 install API_REST_GildedRose-0.0.1-py3-none-any.whl`


### Prepara tu proyecto para distribuirlo

1. Instala las `setuptools`

    `$ pip install setuptools`

2. Instala el paquete `wheel`

    `$ pip3 install wheel`

2. Prepara el fichero `setup.py`

    [Flask tutorial deploy](https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/)

3. Genera el fichero de distribución:

    `$ python setup.py bdist_wheel` 
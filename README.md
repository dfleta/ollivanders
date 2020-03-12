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


### Ejecuta la aplicación

0. Antes has de dispone de una cuenta en Mongo Atlas y un cluster disponible. Crea una usuaria con su password correspondiente. Luego, obtén el drive para y escribe la URI en el fichero `db_atlas.py` en:

    ```Python
    connect(
        host='mongodb+srv://<usuaria>:<password>@cluster0-ud3ms.mongodb.net/test?retryWrites=true&w=majority')
    ```

    Esto conectará tu app con la base de datos `test` que por defecto ofrece MongoDB. 
    Si dispones de otra base de datos en Atlas, sustituye `test` por su nombre en la URI.

1. Activa el entorno virtual:

    `$ source venv/bin/activate`

2. Configura las variables de entorno FLASK:

    ```Bash
    `$ export FLASK_APP=controller.py`
    `$ export FLASK_EN=development`
    ```
3. Comprueba que tendrás acceso a MongoDB desde Atlas:

    `$ curl portquiz.net:27017`

3. Si es la primera vez que arrancas la app y no dispones de items en la base de datos, inicializala con el comando:

    `$ flask init-db`

4. Arranca la app para que corra en el localhost:

    `$ flask run --host 0.0.0.0`

    Comprueba en tu navegador o con `curl` que corre en:
    `http://127.0.0.1:5000/`

5. Si quieres que esté disponible en la red local en la ip de tu máquina, ejecuta:

    `$ flask run --host 0.0.0.0`

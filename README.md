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
        host='URI')
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


### Dependencias

Chequear si los paquetes instalados tienen dependencias compatibles:

```sh
$ pip3 check
No broken requirements found.
```

Chequear si las dependencias no están actualizadas.

```sh
$ pip list --outdated
Package           Version Latest Type 
----------------- ------- ------ -----
aniso8601         8.0.0   9.0.1  wheel
astroid           2.9.0   2.10.0 wheel
Click             7.0     8.0.4  wheel
dnspython         1.16.0  2.2.0  wheel
Flask             1.1.1   2.0.3  wheel
Flask-Cors        3.0.8   3.0.10 wheel
flask-mongoengine 0.9.5   1.0.0  wheel
Flask-RESTful     0.3.7   0.3.9  wheel
Flask-WTF         0.14.2  1.0.0  wheel
```

un buen jaleo... vamos a automatizar el proceso de mantener las dependencias de manera determinista, es decir, siempre generando la misma instalación de las mismas versiones al ejecutar `pip install requirements.txt`

Intalar pip-tools:

`$ pip3 install pip-tools`

Crear el fichero `requirements.in` para pinned (==) todas las dependencias:

`Flask==2.0.3`  OK

`Flask-Cors>=3.0.9`  NOTOK

Incluir sólo las dependencias de alto nivel:

```txt
Flask==2.0.3
Flask-Cors==3.0.10
flask-mongoengine==1.0.0
Flask-RESTful==0.3.9
mongoengine==0.24.0
pymongo==4.0
gunicorn==20.0.4
```

**Sin** `setup.py` ejecutamos

`pip-compile requirements.in`

para generar el fichero `requirements.txt` con las versiones exactas de los paquetes de `.in` más sus dependencias (usando las últimas versiones que satisfacen las dependencias). Si hay incompatibilidades seguimos sus indicaciones:

```sh
There are incompatible versions in the resolved dependencies:
  pymongo==4.0.1 (from -r requirements.in (line 6))
  pymongo<=4.0,>=3.4 (from mongoengine==0.24.0->-r requirements.in (line 5))
```

```sh
requirements.txt
#
# This file is autogenerated by pip-compile with python 3.8
# To update, run:
#
#    pip-compile
#
aniso8601==9.0.1
    # via flask-restful
click==8.0.4
    # via flask
...
```

Para forzar a `pip-compile` a actualizar todos los paquetes en el `requirements.txt` existente, ejecutamos:

`pip-compile --upgrade`


Sincronizar venv con requirements:

`$ pip-sync`

#### dev dependencies

Crear el fichero `dev-requirements.txt` incluyendo las dependencias para el desarrollo de la app.
En la primera línea escribir `-c requirements.txt` para constrñir los dev requirements a los paquetes ya seleciconados para producción en `requirements.txt`.

```sh
# dev-requirements.in
-c requirements.txt
pytest

$ pip-compile dev-requirements.in
```

Para instalar las dependencias dev y producción:

`pip-sync requirements.txt dev-requirements.txt`


#### Recursos sobre dependency management

https://github.com/jazzband/pip-tools

https://nvie.com/posts/better-package-management/

https://hynek.me/articles/python-app-deps-2018/


### Docker

```sh
$ docker build -t ollivanders_pinned .

$ docker container run --name ollivanders_pin -dp 5000:5000 ollivanders_pinned:latest

$ docker container stop ollivanders_pin 

# Comprobar si .dockerignore ha hecho su trabajo
$ docker exec -it ollivanders_pin sh
$ ls
```

# Uso

```sh
curl -w "\n" http://localhost:5000/inventario -H "Content-Type: application/x-www-form-urlencoded"

curl -w "\n" http://localhost:5000/inventario -H "Content-Type: application/json"

curl -d '{"name": "Sombrero seleccionador", "sell_in": 80, "quality": 30}' -H "Content-Type: application/json" -X POST http://localhost:5000/

curl -d name="Conjured Mana Cake" -d sell_in=3 -d quality=6 http://127.0.0.1:5000/items -X POST

curl -d name="Conjured Mana Cake" -d sell_in=3 -d quality=6 http://127.0.0.1:5000/items -X DELETE

curl -w "\n" http://localhost:5000/items/name/Aged%20Brie -H "Content-Type: application/json" -v

curl -w "\n" http://localhost:5000/items/quality/80 -H "Content-Type: application/json" -v

curl -w "\n" http://localhost:5000/items/sellin/0 -H "Content-Type: application/json"
```
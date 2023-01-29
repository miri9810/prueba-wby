# PRUEBA WBY


Este repositorio es para la prueba solicitada por WeBookYou proyecto de API REST que use Django.

La finalidad es tener el manejo y control de Códigos Postales de México


## Tecnologías incluidas:
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [psycopg2](https://pypi.org/project/psycopg2/)
- [Python decouple](https://pypi.org/project/python-decouple/)
- [SimpleJWT](https://pypi.org/project/djangorestframework-simplejwt/)



## Para la creación del entorno del proyecto
1. [venv](#)

### Comandos útiles de pipenv

- Instalar una nueva dependencia

        $ pipenv install <dependencia>

    - Opcional: instalar una dependencia de desarrollo

            $ pipenv install <dependencia> --dev

- Actualizar las dependencias

        $ pipenv update

- Ejecutar un comando en el entorno virtual sin lanzar un nuevo shell

        $ pipenv run <comando>

    - Ejemplos:

            $ pipenv run django-admin startproject <nombre_proyecto>
            $ pipenv run python manage.py startapp <nombre_app>
            $ pipenv run python manage.py makemigrations
            $ pipenv run python manage.py migrate
            $ pipenv run python manage.py createsuperuser --email admin@example.com --username admin
            $ pipenv run python manage.py runserver

- Para transformar el archivo Pipfile en formato requirements.txt

        $ pipenv lock -r > requirements.txt

        $ pipenv lock -r -d > dev-requirements.txt

- Cuando todo funcione en desarrollo y se quiera pasar a producción. Se debe crear / actualizar el archivo Pipfile.lock ejecutando

        $ pipenv lock


## Cómo levantar el proyecto usando venv (2):

- Crear el entorno virtual. En este caso se está usando la herramienta incluida de Python

        $ python3 -m venv env

- Activar el entorno virtual

        $ source env/bin/activate

- Instalar las dependencias del `requirements.txt` existente

        $ python3 -m pip install -r requirements.txt

- Levantar el servidor

        $ cd api

        $ python manage.py runserver

- Para desactivar el entorno virtual

        $ deactivate

- Tener instalado o levantado una base de datos ya sea local o en la nube. Los datos de conexión tienen que ser incluidos en el archivo `.env` donde corresponda, una vez hecho esto se puede levantar el servidor, aunque intenté deployarlo, no logré concluirlo

![Deploy en Render](/deploy-render.png)



## Archivo env

- Dejo de ejemplo el archivo .env-example, desde este archivo se puede apoyar para la creación de la base de datos para alojar las tablas con los modelos que he creado


# ¡¡¡   EXTRA   !!!

- Descargué el archivo excel de los CP, algo con lo que no había trabajado, por lo que no sabía como importar los datos, así que opté por cambiar los datos, pero sería un problema guardar los datos de 32 hojas diferentes, así que solo hice unas pruebas con unos cuantos, solo le puse una capa de seguridad que fue con autenticacion mediante SIMPLEJWT, por lo que es muy sencillo de levantar, pero si tiene faltas muy grandes, también intenté crear el contenedor, pero no logré completar la tarea. 

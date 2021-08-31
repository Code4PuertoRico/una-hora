## Developers

Este proyecto no sería posible sin la colaboración de otros developers que han donado su tiempo para crear esta aplicación. Si encuentras un error por favor crea un [issue](https://github.com/Code4PuertoRico/una-hora/issues) y si puedes arreglarlo te invitamos a hacer y someter un pull request.

### Para correr el proyecto

Hay dos opciones para correr el proyecto, la primera usando Docker y la segunda instalandolo en tu ambiente local.

#### Opción 1: Docker

**Instalación**

**Linux**

Puedes encontrar instrucciones de como instalar Docker para diferentes distribuciones de Linux [aqui](https://docs.docker.com/engine/installation/#docker-editions).


**Mac OS**

La mejor manera de utilizar Docker en Mac OS o Windows PC es utilizando [Docker Desktop](https://www.docker.com/products/docker-desktop).

** Cómo crear imágenes de `Una Hora` con Docker **

```bash
# Clonear repositorio
$ git clone https://github.com/Code4PuertoRico/una-hora.git


# Copiar archivo de variables de ambiente
$ cp .env.example .env


# Crear la imagen de Docker y correrla en un contenedor separado del terminal
$ docker-compose up --build --detach
```

El archivo docker-compose.yml contiene toda la configuración de los servicios de Docker necesarios tener una instancia de Una Hora corriendo.

Abre tu browser en [http://0.0.0.0:8000/](http://0.0.0.0:8000/). Para accesar la sección de administración ve a [http://0.0.0.0:8000/admin/](http://0.0.0.0:8000/admin/), y usa el username **admin** y el password **abc123**.

#### Opción 2: Local

**Requisitos**

- [Python 3.9](https://www.python.org/)
- [Pipenv](https://docs.pipenv.org/en/latest/)
- [Node.js 14 o más reciente](https://nodejs.org) (incluye npm)

```bash
# Clonear repositorio
$ git clone https://github.com/Code4PuertoRico/una-hora.git

# Copiar archivo de variables de ambiente
$ cp .env.example .env

# Instalar dependencias Python
$ pipenv install --dev

# Instalar dependencias para el frontend
$ pipenv run python manage.py tailwind install


# Migración y data inicial
$ pipenv run python manage.py migrate
$ pipenv run python manage.py loaddata una_hora/users/fixtures/initial.json

# Correr servidor de Django
$ pipenv run python manage.py runserver
```

Abre tu browser en [http://localhost:8000/](http://localhost:8000/). Para accesar la sección de administración ve a [http://localhost:8000/admin/](http://localhost:8000/admin/), y usa el username **admin** y el password **abc123**.


#### Para correr tests
```
$ pipenv run pytest
```

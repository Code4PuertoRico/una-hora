## Developers

This project would not be possible without other developers contributing their time. If you find an error please create an [issue](https://github.com/Code4PuertoRico/una-hora/issues) and if you can fix it we invite you to create and submit a pull request :smile:.

### Running the project

There's a couple of ways to run this project locally:

#### Option 1: Docker

**Installation**

**Linux**

You can find instructions on how to install Docker for a number of Linux distributions [here](https://docs.docker.com/engine/installation/#docker-editions).

**Mac OS or Windows**

The best/easiest way to have Docker on your Mac or Windows PC is using [Docker Desktop](https://www.docker.com/products/docker-desktop).


** Creating the Una Hora Docker images **

```bash
# Clone the repo
$ git clone https://github.com/Code4PuertoRico/una-hora.git

# Make a copy of the .env.example file
$ cp .env.example .env

# Build the Docker image and run it in detached mode
$ docker-compose up --build --detach

# After writing code, run pre-commit
$ docker-compose run web pre_commit
```

The docker-compose.yml file contains all the configuration needed to have a running instance of Una Hora.

Now you can point your browser to [http://0.0.0.0:8000/](http://0.0.0.0:8000/). To access the admin panel go to [http://0.0.0.0:8000/admin/](http://0.0.0.0:8000/admin/), and use the following credentials:

* username: **admin**
* password: **abc123**

#### Option 2: Local

**Requirements**

- [Python 3.9](https://www.python.org/)
- [Pipenv](https://docs.pipenv.org/en/latest/)
- [pre-commit](https://pre-commit.com/#install)
- [Node.js 14 or newer](https://nodejs.org) (includes npm)

```bash
# Clone the rep
$ git clone https://github.com/Code4PuertoRico/una-hora.git

# Install pre-commit hooks
$ pre-commit install

# Make a copy of the .env.example file
$ cp .env.example .env

# Install Python dependencies
$ pipenv install --dev

# Build frontend dependencies
$ pipenv run python manage.py tailwind install

# Django migrate and initial data load
$ pipenv run python manage.py migrate
$ pipenv run python manage.py loaddata una_hora/users/fixtures/initial.json

# Run the Django server
$ pipenv run python manage.py runserver
```

Now you can point your browser to [http://localhost:8000/](http://localhost:8000/). To access the admin panel go to [http://localhost:8000/admin/](http://localhost:8000/admin/), and use the following credentials:

* username: **admin**
* password: **abc123**

#### Running the Tests
```
$ pipenv run pytest
```

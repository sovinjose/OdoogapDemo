# Odoogap Demo

## Setup

The first thing to do is to clone the repository:

```sh
$ git https://github.com/
$ cd odoogap_demo
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv demo_env
$ source demo_env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```


Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd odoogap_demo
(env)$ python manage.py runserver

There are two end point 

1. Eu region, using eu DB for this
```
And navigate to `http://127.0.0.1:8000/eu`.

2. Other region, using default DB for this
```
And navigate to `http://127.0.0.1:8000/`.


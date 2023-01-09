# C to API

Expose a command line C program as a web api

## ** INSECURE WARNING ** 

Take care on how you call the C program, path to the C program, sanitize the arguments to it, etc., as you can do bad things :)

## Clone project

```
git clone TKTK
```

## Python + Flask

Use [Flask](https://flask.palletsprojects.com/en/2.2.x/) to server the API endpoints

## Setup venv and install requirements

```
python -m venv .venv
souce .venv/bin/activate
pip install -r requirements.txt  # will install Flask and any other requirements
```

## Test Flask

Edit `app.py` to alter API arguments and invocation command for C program

```
FLASK_APP=app.py flask run --port 8000
# open http://127.0.0.1:8000/run
# CTRL-C to quit the running server
```

With Flask server running, test hits top your API and expected responses:
* http://127.0.0.1:8000/run
* http://127.0.0.1:8000/run/%Y-%m-%d
* http://127.0.0.1:8000/run/%Y-%m-%d%20%H:%M:%S

## Host at [Fly.io](https://fly.io/docs/languages-and-frameworks/python/)

Host on the free tier at Fly.io

### Install `flyctl` and create account

Install `flyctl` CLI following as per [Install flyctl](https://fly.io/docs/hands-on/install-flyctl/)

```
brew install flyctl  # refer to docs for other OS
flyctl auth signup  # and select free tier
```

### Build and deploy app

`flyctl` will prompt you to overwrite existing files and create a new deploy app

```
flyctl launch  # allow it to overwrite fly.toml and assign a random app name or specify one
flyctl open    # open and run the app
```

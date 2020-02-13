# coffee-api
API for our our local coffee maschine

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/finncyr/coffee-api)


## API Calls

### `GET /info`
**Gets you some system information**

### `POST /brew`
**Brews you some nice default coffee**

Arguments: (json)
```
{
    "key": "The secret key only availiable to the chosen ones!"
}
```


## How to use pipenv

Install using 
```
$ sudo apt install pipenv
```

Install dependencies with 
```
/coffee-api $ pipenv install 
```

Run gunicorn Server (linux only) with
```
/coffee-api $ gunicorn app:app
```

You can test the API with curl (for example)
```
$ curl localhost:8000/info
```

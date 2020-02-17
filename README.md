# coffee-api
API for our our local coffee maschine

![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/finncyr/coffee-api)
![GitHub](https://img.shields.io/github/license/finncyr/coffee-api)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

## ToDo

- [x] protect coffee maschine with a global password
- [x] usernames
- [x] User-bound custom Passwords
- [] Statisticts (with own API-Endpoint)
- [] make the brewCoffee() function actually do something
- [] WebInterface (maybe)
 
## API Calls

### `GET /info`
**Gets you some system information**

### `POST /brew`
**Brews you some nice default coffee**

Arguments: (json)
```
{
    "key":  "<The secret key only availiable to the chosen ones! (username-bound password)>"
    "user": "<Username>"
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

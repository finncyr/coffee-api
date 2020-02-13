# coffee-api
API for our our local coffee maschine

## API Calls

### `GET /info`
**Gets you some system information**


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
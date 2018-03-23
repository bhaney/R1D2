# R1D2 
A robot that extracts the menus of the CERN restaurants (R1, R2, R3) for you.

## Setup

R1D2 uses [Flask](http://flask.pocoo.org) and Python >= 3.5. 
```
$ git clone https://github.com/bhaney/R1D2.git r1d2
$ cd r1d2
$ pip3 install -r requirements.txt
$ export FLASK_APP=app.py
$ flask run 
```
This will serve the app by default on `http://127.0.0.1:5000`. To see today's
menu, use your browser to go to `http://127.0.0.1:5000/today/`.

## API
`GET`-only API using [Flask](http://flask.pocoo.org). There are three types of
commands that can be composed to query the menu.

Specify the date
```
/week/
/today/
/tomorrow/
/monday/
/…
/friday/
```

Specify the restaurant
```
/r1/
/r2/
/r3/
```

Specify the type of dish
```
/menu1/
/menu2/
/menu3/
/vegetarian/
/speciality/
/grill/
/pasta/
/pizza/
```

Please note that due to the super simple way this API is implemented the order
of the parameters does not matter but using two mutually exclusive parameters
together will result in an empty menu.

The server uses `shelve` to store the menu on the server and thus reduce the
number of times the data needs to be extracted from the Novae website.


import string
import random
from flask import Flask
from flask import render_template

app = Flask(__name__)

def get_random_letters():
    
    l = []
    for x in range(1, 11):
        l.append(random.choice(string.letters))
    return l

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/<name>")
def hello_name(name):    
    return "Hello <b>%s</b>! How are you?" % (name)

class Car(object):
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def get_seats(self):
        if self.model == 'sedan':
            return 4
        return 2

@app.route("/<name1>/<name2>")
def two_names(name1, name2):
    
    #car = Car('honda', 'blue')
    numbers = range(1,11)
    letters = list(string.letters[:10])
    pairs = zip(numbers, get_random_letters())
    print pairs
    d = { 'name1' : name1,
        'name2' : name2,
        'numbers' : numbers,
        'pairs' : pairs,
        'car' : Car('honda', 'blue')
    }
    return render_template('two_names.html', **d)
    
   
    
    

if __name__ == "__main__":
    app.debug = True
    app.run()
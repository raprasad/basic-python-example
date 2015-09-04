from os.path import join, dirname, realpath
from flask import Flask
from flask import render_template
from parse_02 import get_country_info

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_name(name):    
    
    d = { 'name' : name 
        , 'list_of_things' : ['dog', 'cat', 'ball'] 
        }
    return render_template('hello.html', **d)


@app.route("/pop/<country>")
def view_country_population(country):

    if country == None:
        country = 'USA'
    
    (success, data_dict_or_err_msg) = get_country_info(country)
    
    if success:    
        d = data_dict_or_err_msg
    
    else:
        d = { 'err_found' : True,
              'err_msg' : data_dict_or_err_msg }
    
    return render_template('country_pop.html', **d)



if __name__ == "__main__":
    app.debug = True
    app.static_folder = join(dirname(realpath(__file__)), 'static')    
    app.run()
basic python example
=======

- files for 6/3/2015

----

## Local Install (on OS X and Windows 8.1)

This is a quick checklist to install virtualenv and virtualevnwrapper on an OS X or Windows 8.1 machine. 

#### Install [pip](http://pip.readthedocs.org/en/latest/installing.html)

* use sudo if needed
    * OS X: ```pip install -U pip```
* if on Windows, make sure [python](https://www.python.org/downloads/) is installed.

#### Install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)

* depends on pip
    * OS X: ```sudo pip install virtualenvwrapper```
* if on windows, either install [virtualenvwrapper-win-1.1.5](https://pypi.python.org/pypi/virtualenvwrapper-win) or [cygwin](https://www.cygwin.com/).
* remember to set the (shell startup file)[http://virtualenvwrapper.readthedocs.org/en/latest/install.html#shell-startup-file]
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
``` 
or, on windows, [this](http://stackoverflow.com/questions/2615968/installing-virtualenvwrapper-on-windows) might be helpful.

#### Pull down the [basic-python-example repository](https://github.com/raprasad/basic-python-example)

* Use the [mac client](https://mac.github.com/) if desired or [windows client](https://windows.github.com/)

### Setup on the local machine

#### cd into the ```basic-python-example``` repository

```
cd ~\basic-python-example
```

#### Install the virtualenv and the requirements

This may take a minute or two.  On Mac: Xcode needs to be installed.
    
```
mkvirtualenv basic-python-example
pip install -r requirements/base.txt
```

If you run into Xcode (or other errors) when running the install, google it.  Sometimes the [Xcode license agreement hasn't been accepted](http://stackoverflow.com/questions/26197347/agreeing-to-the-xcode-ios-license-requires-admin-privileges-please-re-run-as-r/26197363#26197363)


## Working with the project (post installation)

```
cd ~\basic-python-example\code
workon basic-python-example
```

### Web example


#### Parse example

- Open a Terminal/Shell
- Go to directory ```\basic-python-example\code``` 
    - With virtualenv activated (*workon basic-python-example*)
- Type:
```
python
```
- Use these commands: [shell_parse.py]( https://github.com/raprasad/basic-python-example/blob/master/code/shell_parse.py)

#### Basic server 1

- Open a Terminal/Shell
- Go to directory ```\basic-python-example\code```
    - With virtualenv activated (*workon basic-python-example*)
- Start [Flask](http://flask.pocoo.org/)
```
python web_01.py
```
- Go to local Flask server: http://127.0.0.1:5000/
- See file [web_01.py](https://github.com/raprasad/basic-python-example/blob/master/code/web_01.py)

#### Basic server 2

- Assume you are in directory ```\basic-python-example\code``` with virtualenv activated (*workon basic-python-example*)
- Start [Flask](http://flask.pocoo.org/)
```
python web_02.py
```
- Go to [hello with template](http://127.0.0.1:5000/hello/yourname)
    - See file [web_01.py](https://github.com/raprasad/basic-python-example/blob/master/code/web_02.py)

- Go to [country list](http://127.0.0.1:5000/pop/USA)
    - See template [https://github.com/raprasad/basic-python-example/blob/master/code/templates/country_pop.html#L26]


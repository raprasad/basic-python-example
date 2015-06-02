quick look at python
=======

Files for 6/3/2015

----

## Local Install (on OS X and Windows 8.1)

This is a quick checklist to install eyeData on an OS X or Windows 8.1 machine.  Currently, it installs the [twoscoops project template](https://github.com/twoscoops/django-twoscoops-project) for [Django 1.6](https://docs.djangoproject.com/en/1.6/), including creating a sqlite database and running a skeleton site. 

#### Install [pip](http://pip.readthedocs.org/en/latest/installing.html)

* use sudo if needed
* if on Windows, make sure [python](https://www.python.org/downloads/) is installed.

#### Install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)

* depends on pip
* if on windows, either install [virtualenvwrapper-win-1.1.5](https://pypi.python.org/pypi/virtualenvwrapper-win) or [cygwin](https://www.cygwin.com/).
* remember to set the (shell startup file)[http://virtualenvwrapper.readthedocs.org/en/latest/install.html#shell-startup-file]
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
``` 
or, on windows, [this](http://stackoverflow.com/questions/2615968/installing-virtualenvwrapper-on-windows) might be helpful.

#### Pull down the [github repository](https://github.com/raprasad/short-python-talk)

* Use the [mac client](https://mac.github.com/) if desired or [windows client](https://windows.github.com/)

### Setup on the local machine

#### cd into the eyeData repository

```
cd ~\basic-python-talk
```

#### Install the virtualenv and the requirements

This may take a minute or two.  Xcode needs to be installed.
    
```
mkvirtualenv eyedata
pip install -r requirements/local.txt
```

If you run into Xcode (or other errors) when running the install, google it.  Sometimes the [Xcode license agreement hasn't been accepted](http://stackoverflow.com/questions/26197347/agreeing-to-the-xcode-ios-license-requires-admin-privileges-please-re-run-as-r/26197363#26197363)


## Working with the project (post installation)

```
cd ~\eyeData\eyedata
workon eyedata
python manage.py runserver
```
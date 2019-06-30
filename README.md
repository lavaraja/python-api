# python-api

Setup :

Create a python 3.6 virtual environment and activate. 

Steps :

$ sudo pip install virtualenv
$ sudo apt-get install python3-venv
$ mkdir mstakxenv && cd  mstakxenv
$ python3 -m venv env
$ source env/bin/activate

Install required dependencies using pip module:

The project folder has requirements.txt file with all dependencies. So install them using python pip module.


if psycog2 plugin installaion failed with below error. .

./psycopg/psycopg.h:34:10: fatal error: Python.h: No such file or directory
     #include <Python.h>
              ^~~~~~~~~~
    compilation terminated.

    It appears you are missing some prerequisite to build the package from source.

#We need to install below system libraries at system level.
Note: if we are running centos or RHEL we need to use equivalent command which is sudo yum install

#sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib

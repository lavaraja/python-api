# python-api

Setup :

Create a python 3.6 virtual environment and activate. 

Step1 :

$ sudo pip install virtualenv
$ sudo apt-get install python3-venv
$ mkdir mstakxenv && cd  mstakxenv
$ python3 -m venv env
$ source env/bin/activate

Step2 :

Clone github  repo of our code. 

$ git clone https://github.com/lavaraja/python-api.git

Install required dependencies using pip module:

The project folder has requirements.txt file with all dependencies. So install them using python pip module.

$ cd python-api/pythonapi
$ pip install -r requirements.txt


Note:  
 
if psycog2 plugin installaion failed with below error. .

./psycopg/psycopg.h:34:10: fatal error: Python.h: No such file or directory
     #include <Python.h>
              ^~~~~~~~~~
    compilation terminated.

    It appears you are missing some prerequisite to build the package from source.

We need to install below system libraries at system level and then rerun the $ pip install -r requirements.txt

$ sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib

Note: if we are running centos or RHEL we need to use equivalent command which is sudo yum install


Step3 :

Install PostgreSQL database as backend database for our local API. 
Download and install PostgreSQL server if you are not already having an PostgreSQL instance running.

$ wget https://get.enterprisedb.com/postgresql/postgresql-10.9-2-linux-x64.run
$ chmod +x postgresql-10.9-2-linux-x64.run
$ sudo ./postgresql-10.9-2-linux-x64.run

Accept the defaults and install.We can customize postgres installation directory,log directory,data directory and all..but our purpose is to have a simple postgres server for our API so we are not doing any highend configuration here for database.

Once the installation complete. 

Go to PostgreSQL installed binary path.

$ pwd
/opt/PostgreSQL/10/bin


Create a new database cluster.

$ ./initdb -D /home/lavaraja/database/pgdata
.....
.....
Success. You can now start the database server using:

    ./pg_ctl -D /home/lavaraja/database/pgdata -l logfile start


Go to datadirectory given above and make the pg_hba.conf file have an entry like below.

# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     trust

The authenication method is trust.which means by default any user on the local system is allowed to connect to database. 

****Note : On production systems this is not recommended. We need to specify profer authenication mechanism like LDAP or MD5 along allowed hosts IP's. 

Since we are using it for test purpose we not changing the default auth mechanism.

Start the server.

/pg_ctl -D /home/lavaraja/database/pgdata -l logfile start

Once the servers is started. Connect to server and create a test database bookapi for using in our python project. 

$ ./psql -u postgres -p 5432

psql.bin (10.3)
Type "help" for help.

Cannot read termcap database;
using dumb terminal settings.
postgres=# create database bookapi;

Step4 :

Create a file name config.py under /home/lavaraja/mstakxenv/python-api/pythonapi/pythonapi.

-rw-r--r-- 1 lavaraja lavaraja  395 Jun 30 09:44 wsgi.py
-rw-r--r-- 1 lavaraja lavaraja  844 Jun 30 09:44 urls.py
-rw-r--r-- 1 lavaraja lavaraja 3377 Jun 30 09:44 settings.py
-rw-r--r-- 1 lavaraja lavaraja    0 Jun 30 09:44 __init__.py
-rw-r--r-- 1 lavaraja lavaraja   78 Jun 30 10:25 config.py

config.py should have database connection  details. 

DB_USER='postgres'
DB_PASSWORD=*******
DB_HOST= 'localhost'
DB_PORT='5433'


Step5 :

Run the migrations on django project and apply migrations. 

$ python manage.py makemigrations
$ python manage.py migrate. 

After this step our models will be created in database.

Step6 : Start the server. 

~/python-api/pythonapi$ python manage.py runserver 8080

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 30, 2019 - 04:59:49
Django version 2.2.2, using settings 'pythonapi.settings'
Starting development server at http://127.0.0.1:8080/
Quit the server with CONTROL-C.

If everthing goes fine then the server will start and show the local url for our use. . 





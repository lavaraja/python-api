# python-api

if psycog2 plugin installaion failed with below error. .

./psycopg/psycopg.h:34:10: fatal error: Python.h: No such file or directory
     #include <Python.h>
              ^~~~~~~~~~
    compilation terminated.

    It appears you are missing some prerequisite to build the package from source.

#We need to install below system libraries at system level.
Note: if we are running centos or RHEL we need to use equivalent command which is sudo yum install

#sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
# App Engine Standard Flask Tutorial App

This sample shows how to use [Flask](http://flask.pocoo.org/) to handle
requests, forms, templates, and static files on Google App Engine Standard.

1. Set up your environment using the instructions at: https://cloud.google.com/appengine/docs/standard/python/quickstart
2. Set up your virtual environment using the instructions at https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env#setting_up_libraries_to_enable_development (step 4) - make sure it's for python 2.7
3. cd into this project directory
4. install the dependencies using [pip](http://pip.readthedocs.io/en/stable/):

    pip install -t lib -r requirements.txt
    
5. Run the project

    dev_appserver.py app.yaml
    
6. Go to localhost:8080 in your browser to see the live project
7. Go to localhost:8000 in your browser to see the database and some other goodies

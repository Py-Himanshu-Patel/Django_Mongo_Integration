# Integrate MongoDB in django project as a database

- Make a project *MongoConnect* and an app *MyApp*. When we connect MongoDB the data of sqlite do not get shifted to MongoDB thus do not start populating it now.

- Install a library `djongo` using `pip install djongo`.

- Create a database in MongoDB (let `django-database`)

- Change the database with following code

    ``` python
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'django-database',  # your database name
        }
    }
    ```

    for more info replace it with

    ``` python
    DATABASES = {
        'default': {
            'ENGINE' : 'djongo',
            'NAME' : 'your-db-name', # as per server
            # it is your connection url with your username and password and database name
            'HOST' : 'mongodb://<dbuser>:<dbpassword>@ds259144.mlab.com:59144/<db-name>', 
            'USER' : '<user>',
            'PASSWORD' : '<password>',
        }
    }
    ```

- run commands

    ``` shell
    python manage.py makemigrations
    python manage.py migrate
    ```

- Now insert data in model created in app and see data appear in MongoDB

- make *requirements.txt* in root folder (along manage.py)

- Hide sensitive data in *.env* file

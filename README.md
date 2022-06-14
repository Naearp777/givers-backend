# Givers
Givers is a Volunteer Management System developed as a part of college project for VI Semester of Computer Engineering undergraduate program.
This repo contains the backend source code for the **Volunteer Management** system. This was an academic project assigned by the [**Department of Electronics and Computer Engineering, Pulchowk Campus** ](http://doece.pcampus.edu.np/) under the subject _Database Management System (DBMS)_.

## Technologies Used

1. [Django](https://www.djangoproject.com/) for the backend system
2. [Postgres](https://www.postgresql.org/) for the database server
3. HTML, CSS for template mail

## Usage

### Install necessary requirements

You need to have [_python_](https://www.python.org/) as well as _pip_ installed in your system to run this project. [_Postgres_](https://www.postgresql.org/) also need to be explicitly installed and configured as per your convinience. 
To install python dependencies, follow the following steps.



**Create a virtual environment**

```sh
python -m venv venv
```

**Activate the environment**

```sh
.\venv\Scripts\activate
```

**Install python dependencies**

```sh
pip install -r requirements.txt
```

### Make changes to the database

To migrate the necessary changes to the newly created database run the following command.

```sh
python manage.py migrate
```


### First Time setup
During the first time setup, the **superadmin user** should be created.

```sh
python manage.py createsuperuser
```

### Run Backend Server

Now the schema of various tables are setup in your newly created database. You can now run the database server using the following command.

```sh
python manage.py runserver
```

This will run a development server in localhost on port 8000. The development server will not be accessible on the LAN just now.

### Access API Documentation

You can access the API documentation from the url : http://127.0.0.1:8000/swagger/ or BASE_URL/swagger/.

### Email Notifications
In order to send users notifications via E-mail. 

First you need to create App password

- Go to settings/security/app password from your Gmail settings

Change the following Values in settings.py.
```sh
EMAIL_HOST_USER='YOUR_EMAIL'
EMAIL_HOST_PASSWORD='YOUR_EMAIL_APPPASSWORD'
```



### Project Members

-   [**Arpan Pokharel** ](https://github.com/Naearp777/) (075BCT015)
-   [ **Chirag Lamsal** ](https://github.com/chiraqL/) (075BCT032)
-   [**Bibek Basyal**](https://github.com/Bibek99/) (075BCT097)
-   [**Saugat Kafley**](https://github.com/Saugatkafley/) (075BCT099)
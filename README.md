# ParityGo backend assignment

Base Django project.

The project is coded in django and rest-framework. Pycharm IDE was used for development.
My Python version is 3.7.4
## Packages that I installed

* django-rest_framework(Version 3.12.2)
* django (Version 3.1.7)
* auditlog3 (Version 1.0.1)
* django-rest-authtoken (Version 2.1.3)
* django-utils-six (Version 2.0)


## Running the project
Run the following commands to create the necessary migrations and tables:-
* python manage.py makemigrations
* python manage.py migrate

And finally run the following command to start the django server:-
python manage.py runserver

Results can be viewed at http://127.0.0.1:8000/api/house_list/ which will display the list of houses.
The  other urls for Thermostat,Room and light can be acccessed by following urls.py file.

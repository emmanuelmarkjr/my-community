# my-community

A Powerful Social Community that combines the features of twitter(timeline and feeds), nairaland(forum to post latest gists and stories) and stackoverflow(to ask questions and profer answers to others' problems).

Developed with django(Python).

go to http://www.techtv.pythonanywhere.com to see the DEMO.
User demo account 
username: mark
password: 1234

Admin account
username: admin
password: 1234

To Get Started
On your local server

Create a virtual environment.
sudo pip install -r requirements.txt to install all necessary dependencies and apps.
python manage.py makemigrations and migrate
python manage.py createsuperuser to create an admin account which can be accessed via localhost:port/admin
If you encounter a "no auth_profile table" error, then do the makemigrations and migrate for individual 3rd party apps in the settings.py file. and run the createsuperuser again.
configure the mail settings to enable email sending on password reset.
python manage.py runserver to start your server





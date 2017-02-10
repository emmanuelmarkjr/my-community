# my-community

A Powerful Social Community that combines the features of twitter(timeline and feeds), nairaland(forum to post latest gists and stories) and stackoverflow(to ask questions and profer answers to others' problems). <br/>

Developed with django(Python). <br/>

go to http://techtv.pythonanywhere.com to see the DEMO. <br/>
User demo account  <br/>
username: mark <br/>
password: 1234  <br/>


http://techtv.pythonanywhere.com/admin
Admin account  <br/> 
username: admin  <br/>
password: 1234  <br/>

To Get Started  <br/>
On your local server  <br/>

Create a virtual environment. <br/>
sudo pip install -r requirements.txt to install all necessary dependencies and apps.  <br/>
python manage.py makemigrations and migrate  <br/>
python manage.py createsuperuser to create an admin account which can be accessed via localhost:port/admin  <br/>
If you encounter a "no auth_profile table" error, then do the makemigrations and migrate for individual 3rd party apps in the settings.py file. and run the createsuperuser again.  <br/>
configure the mail settings to enable email sending on password reset.  <br/>
python manage.py runserver to start your server  <br/>





# my-community

A very Powerful Social Community that combines the features of twitter(timeline and feeds), nairaland(forum to post latest gists and stories) and stackoverflow(to ask questions and profer answers to others' problems). <br/>

Developed with django(Python). <br/>

go to http://mycommunity.pythonanywhere.com to see the DEMO. <br/>
User demo account  <br/>
username: mark <br/>
password: 1234  <br/>


http://mycommunity.pythonanywhere.com/admin
Admin account  <br/> 
username: admin  <br/>
password: 1234  <br/>

To Get Started  <br/>
On your local server on an Ubuntu Machine  <br/>

Create a virtual environment. <br/>
sudo pip install virtualenv to install virtual environment<br/>
sudo pip install virtualenvwrapper to install virtual environment wrapper<br/>
mkvirtualenv (your virtual environment name) <br/>
it sets up necessary python packages to start your development
then you see the name in rounded brackets before your machine's username. <br/>
If you get "command error" on creating the virtual environment.<br/>
sudo gedit .bashrc and add this at the bottom of the script <br>
#Virtualenvwrapper settings <br/>
export WORKON_HOME = $HOME/.virtualenvs<br/>
export PROJECT_HOME = $HOME/Projects<br/>
source /usr/local/bin/virtualenvwrapper.sh<br/>

then save and run source ~/.bashrc to effect changes<br/>
then run mkvirtualenv again. <br/>
sudo pip install -r requirements.txt to install all necessary dependencies and apps.  <br/><br/>
python manage.py makemigrations and migrate  <br/><br/>
python manage.py createsuperuser to create an admin account which can be accessed via localhost:port/admin  <br/><br/>
If you encounter a "no auth_profile table" error, then do the makemigrations and migrate one after the other for each individual 3rd party app in the settings.py file. and run the createsuperuser again.  <br/><br/>
configure the mail settings to enable email sending on password reset.  <br/><br/>
python manage.py runserver to start your server  <br/>





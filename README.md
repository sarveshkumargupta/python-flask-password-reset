# Login-password-reset
This code will create a token and send it to registered users, so that he can create a new password.
This piece of code can be useful when you are creating a website, and your users are forgotten their password. So that user can got to (forgot password) link and reset their password.
This code is in python and it uses flask framework and MYSQL for database since we are using flask-sqlalchemy you can change database easily according to your requirements. I am assuming that you know basics of python.

Requirements:
pip install flask
pip install flask-sqlalchemy
pip install flask-wtf
pip install flask-mail
pip install flask-bootstrap(just for decoration)

Explanations:
The run.py file is the main file from where you can run your program. There are four python file models, forms, routes and init file.
Models - here i have created a database for user registration so user can register, but in my code i have not used this part because the purpose of this code is only to give you idea about how forgot password works. So i assumed that you already have regisstration page and database for that.
Now in my models there is two fuction which i created, get_reset_token for generating a token and verify_reset_token is for verifying a token. In generating i have parameter expire_time which shows the time until that it is valid. after that perticular time it gets expire.
Routes - here all the routes are exist, i have only created three route which is enough for us to explain this. There is one fuction which is doing nothing but sending token to users via email.
Forms - In my forms there are three forms, Login form is just for show piece and others two we are using here.
init - This is the place where i did my all the configuration.
Templates - This file is responsible for front-end work. Since i am using flask-bootstrap extension so i can simply call all my forms by inheriting wtf from bootstrap.

I have used gmails server for mail you can use your server as well, this is only for explation.

"""You can simply pull the code and install all the pip requirements and ready to gooo"""

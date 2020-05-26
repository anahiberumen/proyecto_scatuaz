# scatuaz

INSTALLATION:

    1-Create an env.
    2-Activate the env.
    3-Run 'pip install -r requirements.txt'.
    4-Create database:

CREATE DATABASE scatuaz CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

CREATE USER 'tigrito'@'localhost' identified by 'tigrito123@';

GRANT ALL PRIVILEGES ON scatuaz.* TO tigrito@localhost;

FLUSH PRIVILEGES;

GRANT ALL PRIVILEGES ON *.* TO 'tigrito'@'localhost' IDENTIFIED BY 'tigrito123@';
    
    5-Create a django super-user with 'python manage.py createsuperuser'.
    6-Run server with 'python manage runserver'
    7-Done.
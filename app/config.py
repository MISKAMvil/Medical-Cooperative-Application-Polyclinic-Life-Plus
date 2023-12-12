import os

SECRET_KEY = 'secret-key'

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@172.16.238.11/mcaplpv1'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

# UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'images')

ADMINISTRATOR_ROLE_ID = 1
USER_ROLE_ID = 2
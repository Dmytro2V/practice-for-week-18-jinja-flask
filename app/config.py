import os


class Config(object):
     # Property used by multiple Flask add-ons for security
    GREETING = 'Salutations, superior students!'
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default-key-for-devs'

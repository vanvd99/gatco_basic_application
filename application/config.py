class Config(object):
    DEBUG = True
    STATIC_URL = "static"
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Dinhvan99@192.168.0.126:5432/students'
    AUTH_LOGIN_ENDPOINT = 'login'
    AUTH_PASSWORD_HASH = 'sha512_crypt'
    AUTH_PASSWORD_SALT = 'ruewhndjsa17heaw'
    SECRET_KEY = 'e2q8dhaushdauwd7qye'
    SESSION_COOKIE_SALT = 'dhuasud819wubadhysagd'

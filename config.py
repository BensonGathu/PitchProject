import os
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ghost:Bkubwa@localhost/pitch'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    "development":DevConfig,
    "production":ProdConfig
}
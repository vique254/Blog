import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:vique@localhost/blog'


class ProdConfig:
    pass
class DevConfig:
    DEBUG =True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}   
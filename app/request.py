import requests

base_url = None

def configure_request(app):
    global base_url
    
    base_url = app.config['BASE_URL']

def get_quotes();
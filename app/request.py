import requests
from .models import Quotes

base_url = None

def configure_request(app):
    global base_url
    
    base_url = app.config['BASE_URL']

def get_quotes():
    data = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    response = data.json()
    results=response
    
    return results
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

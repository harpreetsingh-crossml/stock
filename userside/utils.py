import requests

def get_stock_price(symbol,price):
   
    response = requests.get({symbol,price})
    data = response
    return data['price']
    


    
    

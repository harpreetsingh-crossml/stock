import requests

def fetch_stock_price(stock_symbol):
    # You should replace this with a real API call to get stock prices
    api_url = f"https://api.example.com/stock/{stock_symbol}/price"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("price", 0.0)
    else:
        return 0.0
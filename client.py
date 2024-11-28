import requests

# API base URL
BASE_URL = "http://127.0.0.1:5000"

def add_product(name, description, price):
    response = requests.post(f"{BASE_URL}/products", json={
        "name": name,
        "description": description,
        "price": price
    })
    print(response.json())

def get_products():
    response = requests.get(f"{BASE_URL}/products")
    print(response.json())

# Test the client
if __name__ == "__main__":
    # Add products
    add_product("Laptop", "A powerful gaming laptop", 1500.0)
    add_product("Mouse", "Wireless mouse", 25.5)
    
    # Retrieve products
    get_products()

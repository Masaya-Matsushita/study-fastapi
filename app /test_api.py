# FIXME:requestsがインポートできない(ModuleNotFoundError)
import requests

def main():
    url = 'http://localhost:8000/item/'
    body = {
        "name": "T-shirt",
        "description": "This is T-shirt.",
        "price": 5980,
        "tax": 1.1
    }
    res = requests.post(url, body)
    print(res)

if __name__ == "__main__":
    main()

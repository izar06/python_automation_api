import requests
import pytest

base_url_reqreqres = 'https://reqres.in/api'
base_url_typicode = 'https://jsonplaceholder.typicode.com/todos/1'
url_post = 'https://fakestoreapi.com/products'
url_update_reqres = 'https://reqres.in/api/users/1'
url_delete_reqres = 'https://reqres.in/api/users/2'

# r = requests.get(f'{base_url}/users/2')
# print(r.text)



def test_method_post():
    payload = {'title': 'New Product', 'price': 29.99}

    # headers = {
    #     'Content-Type': 'application/json'
    # }

    response = requests.post(url_post, json=payload)
    print(response.status_code)
    print(response.text)
    print(response.json())
    
    assert response.status_code == 201

def test_method_get():
    r = requests.get(base_url_typicode)
    response_code = r.status_code
    print(response_code)
    print(r.text)
    print(r.json())
    
    assert response_code == 200
    
def test_method_put():
    payload = {'name': 'Jane Doe', 'price': 'Product Manager'}
    response = requests.put(f'{url_post}/1', json=payload)
    print(response.status_code)
    print(response.text)
    print(response.json())
    
    assert response.status_code == 200

def test_method_delete():
    response = requests.delete(f'{url_post}/1')
    print(response.status_code)
    print(response.text)
    print(response.json())
    
    assert response.status_code == 200
    
test_method_post()
test_method_get()
test_method_put()
test_method_delete()
    
    
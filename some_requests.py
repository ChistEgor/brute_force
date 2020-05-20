import requests


def request_local_server(login, password):
    """
    Requests are made to local servers
    The function returns true or false if login or password is right
    """
    response = requests.post('http://127.0.0.1:5000/auth',
                             json={'login': login, 'password': password})
    return response.status_code == 200


def request_local_secure_server(login, password):
    """
    Port is 4000
    Do you know what does mean NGINX?
    a tool that protects 'against' attacks
    nginx.conf
    It limits the speed of requests from users
    """
    response = requests.post('http://127.0.0.1:4000/auth',
                             json={'login': login, 'password': password})
    return response.status_code == 200

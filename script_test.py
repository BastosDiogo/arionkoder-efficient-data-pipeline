import requests

url = 'http://127.0.0.1:8000/webhook/data-pipeline'

usuarios = [
    {
        "first_name": "Diogo",
        "last_name": "Bastos",
        "age": 17,
        "document": "011.111.111-11",
        "web_site": "https://www.linkedin.com/in/diogo-bastos-81003046/"
    },
    {},
    {
        "first_name": "Diogo",
        "last_name": "Bastos",
        "age": 27,
        "document": "111.111.111-11",
        "web_site": "https://www.linkedin.com/in/diogo-bastos-81003046/"
    },
    {
        "first_name": "Diogo",
        "last_name": "Bastos",
        "age": 37,
        "document": "21111111115",
        "web_site": "https://www.linkedin.com/in/diogo-bastos-81003046/"
    },
]

consulta = requests.post(url=url, json=usuarios)

print(consulta.json())
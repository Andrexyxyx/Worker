import requests
import json

# GET-ЗАПРОС
res_get = requests.get(f"https://petfriends.skillfactory.ru/api/key", headers={"accept": "application/json", "email": "test_mail90@mail.ru", "password": "-andrew25-"})
if 'application/json' in res_get.headers['Content-Type']:
    res_get.json()
else:
    res_get.text
print(res_get.status_code)
print(res_get.text)


# POST-ЗАПРОС
data_example = {"name" : "Rex", "animal_type" : "dog", "age" : "3"}
res_post = requests.post(f"https://petfriends.skillfactory.ru/api/create_pet_simple", headers={'accept': 'application/json', "auth_key" : json.loads(res_get.text)["key"]}, data = data_example)
print(res_post.status_code)
print(res_post.text)


# PUT-ЗАПРОС
data_change = {"name" : "RexChange", "animal_type" : "dogChange", "age" : "7"}
res_post = requests.put(f"https://petfriends.skillfactory.ru/api/pets/" + json.loads(res_post.text)["id"], headers={'accept': 'application/json', "auth_key" : json.loads(res_get.text)["key"]}, data = data_change)
print(res_post.status_code)
print(res_post.text)


# DELETE-ЗАПРОС
res_delete = requests.delete(f"https://petfriends.skillfactory.ru/api/pets/" + json.loads(res_post.text)["id"], headers = {'accept': 'application/json', "auth_key" : json.loads(res_get.text)["key"]})
print(res_delete.status_code)
print(res_delete.text)
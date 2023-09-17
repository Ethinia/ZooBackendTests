
import requests
import datetime

current_time = datetime.datetime.now()
date = str(f"{current_time.year}-0{current_time.month}-{current_time.day}")

url = "http://localhost:3001/animals"

def test_getlist():
    r = requests.get(url)
    assert r.status_code == requests.codes.ok

def test_post_animal():
    animal = {
        "species":"Lion",
        "name":"George",
        "age":26,
        "habitat":"Fields"
    }
    r = requests.post(url, json=animal)
    assert r.status_code == requests.codes.created

"""
# post something into database then get the DB id for that item (last item in DB) and input that id into the delete url.
def test_delete_animal():
    animal = {
        "species":"Zebra",
        "name":"DestroyMe",
        "age":17,
        "habitat":"Glasshouse"
    }
    requests.post(url, json=animal)
    r = requests.get(url)
    data = r.json()
    d = requests.delete(url+"/"+(data[-1]['animalID']))
    assert d.status_code == requests.codes.ok


# test edit. post something then get last items id in DB and use that in the url part and then put/edit that 

def test_edit_animal():
    animal = {
        "species":"Lion",
        "name":"George",
        "age":26,
        "habitat":"Fields"
    }
    animalE = {
        "species":"Lion",
        "name":"George",
        "age":26,
        "habitat":"Fields"
    }

    requests.post(url, json=animal)
    r = requests.get(url)
    data = r.json()
    d = requests.put(url+"/"+(data[-1]['id']), json=animalE)
    assert d.status_code == requests.codes.ok

"""
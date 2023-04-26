import json

person = {
    "name":"Mahsum",
    "age": "24",
    "city":"mardin"
}

person_json = json.dumps(person)


print(person_json)


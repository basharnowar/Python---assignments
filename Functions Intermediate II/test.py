# Iterate Through a List of Dictionaries
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def iterateDictionary(some_list):
    for i in some_list:
        print(i['first_name'])
        print(i['last_name'])
        print(f"first_name {i['Michael']}, last_name {i['Jordan']}")
iterateDictionary(students)

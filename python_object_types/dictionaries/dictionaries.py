
employees = {
'employee1': {
    'name': 'alba',
    'role': 'dev',
    'location': 'nyc',
    'age': 28,
    'remote': True,
    'promotions': ['intern', 'dev'],
    'place_of_birth': ('country', 'El Salvador')
},
'employee2': {
    'name': 'vicky',
    'role': 'senior manager',
    'location': 'los angeles',
    'age': 26,
    'remote': True,
    'promotions': [None],
    'place_of_birth': ('country', 'United States')
},
'employee3': {
    'name': 'daniel',
    'role': 'manager',
    'location': 'houston, tx',
    'age': 33,
    'remote': False,
    'promotions': ['instructor', 'lead instructor', 'manager'],
    'place_of_birth': ('country', 'Mexico')
},
'employee4': {
    'name': 'brandon',
    'role': 'NASA engineer',
    'location': 'DC',
    'age': 26,
    'remote': False,
    'promotions': ['intern', 'NASA engineer'],
    'place_of_birth': ('country', 'Canada')
},
}

print(employees)


# TODO: understand nested dictionaries

# print(D['emp1']['name'])

# print(D['emp1'].get('salary'))
# D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#      'emp2': {'name': 'Kim', 'job': 'Dev'},
#      'emp3': {'name': 'Sam', 'job': 'Dev'}}

# for id, info in D.items():
#     print("\nEmployee ID:", id)
#     for key in info:
#         print(key + ' ==>', info[key])
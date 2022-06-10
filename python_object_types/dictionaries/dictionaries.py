"""this dictionary employees
has a dictionary inside of it (nested) employee
it has a string variable, it has a num variable, it has a boolean variable, it has a list variable, it has a tuple variable"""
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

# print(employees['employee3']['name'])
# print(employees['employee3']['age'])
# print(employees['employee3']['remote'])
# print(employees['employee3']['promotions'])
# print(employees['employee3']['place_of_birth'])


# print(dir('employees'), type(employees))


# print("--------------------------------------------------")
# print(dir('employee1'), type(26))
# print("--------------------------------------------------")
# print(dir('name'), type(False))
# print("--------------------------------------------------")
# print(dir('name'), type(True))
# print("--------------------------------------------------")
# print(dir('name'), type(['intern', 'NASA engineer']))
# print("--------------------------------------------------")
# print(dir('name'), type(('country', 'Canada')))
# employees 
# 'employee1': {
#     'name': 'alba',
#     'role': 'dev',
#     'location': 'nyc',
#     'age': 28,
#     'remote': True,
#     'promotions': ['intern', 'dev'],
#     'place_of_birth': ('country', 'El Salvador')


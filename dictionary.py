my_dict = {}

my_dict = {1: 'camera', 2: 'recorder'}

my_dict = {'name': 'rio', 1: [2, 4, 3]}

my_dict = {'name': 'riyana', 'age': 12}

print(my_dict['name'])
print(my_dict.get('age'))

my_dict['age'] = 13
print(my_dict)

my_dict['address'] = 'Dhaka'
my_dict.pop('age')
print(my_dict)

print("address :", my_dict.get('address'))

my_dict.clear()
print(my_dict)
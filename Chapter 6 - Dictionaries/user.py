#Looping in Dictionaries
user_01 = {'first_name': 'joão',
           'middle_name': 'victor caetano',
           'last_name': 'narducci',
           'age': 22,
           'city': 'são paulo'}

#Printing all information about the user:
for k, v in user_01.items():
    print(f"\nKey: {k}")
    print(f"Value: {v}")
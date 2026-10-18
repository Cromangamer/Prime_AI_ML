# Dictionary
# key : value pair-> where key is unique

dict = {
    'name': 'Dhruv Pankhaniya',
    'subject':['maths','english','physics'],
    'marks':[99,20,98],
    'pass': True
}

# print value by using key
print(dict['name'])

# add a new key-value pair
dict['age'] = 19
print(dict['age'])

# update an existing value
dict['age'] = 18
print(dict['age'])

# delete a key 
dict.pop('age')
print(dict)

# copy 
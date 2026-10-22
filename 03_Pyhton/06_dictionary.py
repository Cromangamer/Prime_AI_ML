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

# get all keys
print(dict.keys())

# get all values
print(dict.values())

# get all key-value pairs
print(dict.items())


def get_student_info(student_dict):
    # this function are made for showing excution flow
    # print("Student name is: ", student_dict['name1']) # this throws error and stops the execution of the program
    # but this code will not stop the Execution
    print("Student subject is: ", student_dict.get('subject1')) # this will return None if key is not found

get_student_info(dict)

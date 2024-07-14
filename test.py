print('testing\'s')

text = "Hello, World!"
index = text.find('o')
print(index)  # Output: 4

name = "Alice"
age = 30
text = "My name is {} and I am {} years old. {} is learning Python.".format(name, age,name)
print(text)  # Output: My name is Alice and I am 30 years old. Alice is learning Python.

# Define variables of different types
integer_var = 10
float_var = 10.5
string_var = "Hello"
list_var = [1, 2, 3]

# Find and print the types of the variables
print(type(integer_var))  # Output: <class 'int'>
print(type(float_var))    # Output: <class 'float'>
print(type(string_var))   # Output: <class 'str'>
print(type(list_var))     # Output: <class 'list'>


print("###### Drop the decimal point ##########")
print(3//2)

print("###### Without drop the decimal point ########")
print(3/2)

print(name+'s')


print("########Dictionaries########")

new_dic = {'name':'test','agee':43,'courses':['kjdksjfs','safsfwefwef']}
print(new_dic)

print("######## Default value if item not present in dic ########:")
print(new_dic.get('phone','Not found'))
dict_ex = '''Dictionaries
A dictionary in Python is a collection of key-value pairs. The dictionary is surrounded by curly braces. Each pair is
separated by a comma and the key and value are separated by a colon. Here is an example:'''
print(dict_ex)

state_capitals = {
 'Arkansas': 'Little Rock',
 'Colorado': 'Denver',
 'California': 'Sacramento',
 'Georgia': 'Atlanta'
}
print(state_capitals)
print(f'''Capital of Arkansas is : {state_capitals['Arkansas']}''')
for k in state_capitals.keys():
   print(k)
for k in state_capitals.values():
   print(k)
for k in state_capitals.keys():
 print('{} is the capital of {}'.format(state_capitals[k], k))
 #print(dir(__builtins__))
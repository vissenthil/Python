tuplesEx = '''Tuples
A tuple is similar to a list except that it is fixed-length and immutable. So the values in the tuple cannot be changed
nor the values be added to or removed from the tuple. Tuples are commonly used for small collections of values
that will not need to change, such as an IP address and port. Tuples are represented with parentheses instead of
square brackets:'''

print(tuplesEx)
ip_address = ('10.20.30.40', 8080)
print(ip_address)
tupleIndx = '''The same indexing rules for lists also apply to tuples. Tuples can also be nested and the values can be any valid
Python valid.'''
print(tupleIndx)
print(ip_address[1])
print('''A tuple with only one member must be defined (note the comma) this way:
one_member_tuple = ('Only member',)
or
one_member_tuple = 'Only member', # No brackets''')
name = ('senthil',)
print(name)
print(type(name))
one_member_tuple = 'Only member',
print(one_member_tuple)
print(type(one_member_tuple))
one_member_tuple = tuple(['Only member'])
print(one_member_tuple)
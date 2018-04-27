# String Operator

string1 = 'Arhant'
string2 = 'Jain'

# Concate

print ( string1 + string2)

# Repetion

print (2*string1)

# Slicing

print(string1[1:2])
print(string1[1:-1])

# String Operation

print(string1.count("t",0,6))
print(string1.find("ant",0,6))
print(string2.find("Jain"))

# Srting Operation

print(string1.upper())
print(string1.lower())
print(string1.isalpha())
print(max(string1))
print(min(string1))

# Tuples

my_tup = ( 'Arhant','Aditi','Raja','Kamal')

# Concate
print(my_tup + ('Ron','Sanjay'))

# Repition

print( my_tup*3)

# Slicing

print ( my_tup[-1])
print(my_tup[1:5])


# Indexing

print( my_tup[2])


# LIST ( Square Braces )

my_list = ['Green','Red','Yellow','Pink']

my_list.append('Blue')
print(my_list)
my_list.extend(['X','Y'])
print(my_list)
my_list.insert(3,'Pyaar')
print(my_list)
my_list.pop()
print(my_list)

# Dictionary

my_dicto = {1:'Green',2:'Blue',3:'White'}
print(my_dicto[3])
print(my_dicto.values())
print(my_dicto.keys())
my_dicto.update({3:'Raja'})
print(my_dicto)


# Sets ( sets can have only unique elements)

my_set_1 = { 1,2,3,4,5}
my_set_2 = { 3,4,5,6,7}
print(my_set_1) # Only unique elements gets printed

print("Union is ",my_set_1 | my_set_2)
print("Intersection is ",my_set_1 & my_set_2)
print("Difference is ",my_set_1 - my_set_2)

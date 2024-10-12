my_dict = {'ГОСТ': 26633, 'год': 2015}
print(my_dict)
print(my_dict['ГОСТ'])
print(my_dict.get('Взамен'))
my_dict.update({'Протокол': 48, 'от': 10122015})
a = my_dict.pop('год')
print(a)
print(my_dict)

my_set = {8, 800, 5, 55, 3, 535, "проще", 800, 55, "позвонить", 535, "чем", 8, 8, "у кого-то", 535, 3, "занимать"}
print(my_set)
my_set.add("реклама")
my_set.add("!")
my_set.remove(8)
print(my_set)
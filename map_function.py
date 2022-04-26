user_names = ['Pedro', 'Juan', 'Paola']
email = list(map(lambda x: x+'@gmail.com', user_names))
print(email)

def add_email(x):
    new_item = x + '@gmail.com'
    return new_item

my_tuple = (2, 3, 4)
new_tuple = tuple(map(lambda x: x*2, my_tuple))
print(new_tuple)

string_number = ['3', '6', '7']
int_number = list(map(lambda x: int(x), string_number))
print(int_number)

countrys = {
    'Colombia': 'bogota',
    'Argentina': 'buenos aires',
    'Peru': 'lima',
    'Venezuela': 'caracas',
    'Mexico': 'mexico d.f.'
}
new_countrys = dict(map(lambda x: (x[0], x[1].title()), countrys.items()))
print(new_countrys)




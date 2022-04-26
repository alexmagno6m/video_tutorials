user_names = ['eduardo', 'juan', 'pedro']
email = list(map(lambda x: x + '@gmail.com', user_names))


def add_email(x):
    new_item = x + '@gmail.com'
    return new_item


email_2 = list(map(add_email, user_names))
print(email_2)


my_tuple = (2, 3, 4)
new_tuple = tuple(map(lambda x: x*2, my_tuple))
print(new_tuple)

thisdict = {"brand": "ford",
            "model": "mustang"
            }

thisdict['brand'] = thisdict.get('brand').title()
new_dict = dict(map(lambda x: (x[0], x[1].title()), thisdict.items()))
print(new_dict)
a = list(thisdict.items())
print(a[0][1])

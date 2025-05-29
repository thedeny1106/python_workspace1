class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f'Hello {self.name}')

p = Person('Tom', 12)
a = getattr(p, 'name')
print(a)

a = getattr(p, 'age')
print(a)

print(dir(p))

fields = [x for x in dir(p) if not x.startswith('__')]

import inspect
print(inspect.getmembers(p))
for item, value in inspect.getmembers(p):
    if inspect.ismethod(value) or inspect.isfunction(value): print('함수', item)
    else: print('변수', value)
var_fields = [(name, value) for name, value in inspect.getmembers(p) if not inspect.isfunction(value) and not name.startswith('__') ]
print(var_fields)
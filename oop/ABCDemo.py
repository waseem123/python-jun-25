import abc


class MySequence(metaclass=abc.ABCMeta):
    pass


MySequence.register(list)
MySequence.register(tuple)
MySequence.register(dict)

a = [1, 2, 3]
b = ('x', 'y', 'z')
c = {30, 25, 78, 89, 96}
d = {'language': 'Python'}
print('List instance:', isinstance(a, MySequence))
print('Tuple instance:', isinstance(b, MySequence))
print('Set instance:', isinstance(c, MySequence))
print('Dict instance:', isinstance(d, MySequence))

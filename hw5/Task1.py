from collections import deque


names = {'Marina': ['David', 'Miha', 'Danila'],
        'David': ['Danila', 'Diana'],
        'Miha': ['Nikita', 'Oleg'],
        'Danila': ['Elya', 'Ira', 'Denick']}


def doter(name):
    return(not len(name) % 2 and name[0] == 'D')


doters = set()
collection_names_key = deque(names)
for key in collection_names_key:
    if doter(key):
        doters.add(key)
    for friend in deque(names.get(key)):
        if doter(friend):
            doters.add(friend)

print(doters)

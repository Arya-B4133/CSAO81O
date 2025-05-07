from collections import Counter

d = {'a': 3, 'b': 3, 'c': 2, 'd': 1}
frequency = dict(Counter(d.values()))
print(frequency)

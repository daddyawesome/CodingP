#Dictionary as a counter

word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)

#Same as above but with get method 
letters =dict()
for l in word:
    letters[l] = letters.get(l, 0) +1
print(letters)

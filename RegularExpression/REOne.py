# Regular-expression
import re

search = 'search inside of this text, please!'
pattern = re.compile('this')

# result = re.search('this', search)
a = pattern.search(search)
b = pattern.findall(search)
c = pattern.fullmatch(search)
d = pattern.match(search)


print(a)
print(b)
print(c)
print(d)

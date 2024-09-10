
# Regular-expression
import re

search = 'search inside of this text, please!'
# ([a-zA-Z]) - any letter from A-Z lower or upper case
# . -> anything except line terminators
# ([a]) -> letter 'a'
pattern = re.compile(r'([a-zA-Z]).([a])')

# result = re.search('this', search)
a = pattern.search(search)

# ([a-zA-Z]) - any letter from A-Z lower or upper case
# 0-9 - any number from 0 to 9
# !@#$ symbols
# maxlength 8 characters
# ends with a number
pwd_pattern = re.compile(r'([A-Za-z0-9!@#$]{8,}\d$)')

password = 'Rafael@!1509test'
check = pwd_pattern.fullmatch(password)

print(check)
print(a.group())

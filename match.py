import re
m = re.search('foo', 'the food on the table')
if m is not None:
    print(m.group())
print("hello world")

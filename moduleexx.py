'''import re
s="Hello this is venkat@gmail.com"
math=re.findall(r'[\w\.-]+@[\w\.-]+',s)
print(math)'''


'''import re
s="Hello this is venkat@gmail.com"
my=re.search(r'[\w\.-]+@[\w\.-]+',s)
print(my)
vv=my.group(0)
print(vv)'''


import re
s="Hello this is venkat@gmail.com"
my=re.search(r'[\w+.com]+@[\w\.-]+',s)
print(my)
vv=my.group(0)
print(vv)

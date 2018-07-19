ac = input ("enter account")
pa = input("enter password")
 
import re 
pattern1 = r'(?P<account>[A-Z][a-z][a-z])'
pattern2 = r'(?P<password>[a-z][a-z][a-z][0][0-9]{5})'
 
match1 = re.search(pattern1,ac)
match2 = re.search(pattern2,pa)
 
# print(type(match2))
if (match1.groupdict()  is not None):
    print(match1.groupdict())
if (match2.groupdict()  is not None):
    print(match2.groupdict())
 
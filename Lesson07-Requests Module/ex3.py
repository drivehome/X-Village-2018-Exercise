import re 

# 設定兩個正規表示法，定義兩個格式。

pattern1 = r'(?P<username>[A-Z][a-z][a-z])'
pattern2 = r'(?P<password>[a-z][a-z][a-z][0][0-9][0-9][0-9][0-9][0-9])'

input_account = input ("enter account: ")
input_password = input("enter password: ")

match1 = re.search(pattern1, input_account)
match2 = re.search(pattern2, input_password)

if match1 is not None \
and match2 is not None \
and len(input_account) == 3 \
and len(input_password) == 9:
    print("Welcome, {}!".format(input_account))

elif match1 is not None \
and match2 is None:
    print("Password format error! Your password is {}".format(input_password))
 
elif match2 is not None and match1 is None:
    print("Username format error! Your password is {}".format(input_account))

elif len(input_account) > 3 \
or len(input_password) > 9:
    print("Account or password legnth error!")
    print("Your username length should be 3, and your password length should be 9")

else:
    print("Format or length error!!")
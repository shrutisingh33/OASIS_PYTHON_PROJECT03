import random
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
symbol = "[]{}#()*;._-"

ans = lower_case+upper_case+num+symbol

length = int(input("enter length  "))
# password = ""

password = "".join(random.sample(ans,length))
print(password)
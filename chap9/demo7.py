#教育机构 ：马士兵教育
#讲    师：杨淑娟
s='abc%'
s1='hellopython'
print(s.isidentifier()) #False
print(s1.isidentifier()) #True
print('\t'.isspace()) #True
print('abc'.isalpha()) #True
print('abc1'.isalpha()) #False
print('张三'.isalpha()) #True

print('123'.isdecimal()) #True
print('123四'.isdecimal())#False

print('123'.isnumeric()) #True
print('123四'.isnumeric()) #True
print('IIIIIIIV'.isnumeric())#False

print('abc123'.isalnum()) #True
print('123张'.isalnum()) #True
print('123!'.isalnum()) #False


import operator
from functools import reduce


User_Area = ['123', '454', '5665', '6767']
User_Area = reduce(operator.add, User_Area)
print(User_Area)
# print("User_Area转化成一维数组之后前20个数据是", User_Area[0:20], type(User_Area))
User_Area_set = list(set(User_Area))

print(User_Area_set)
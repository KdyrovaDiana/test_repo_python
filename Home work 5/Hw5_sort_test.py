str_list = ['potato', 'tomato', 'carrot']

test = sorted(str_list)
print(test, str_list)

test = str_list.sort()
print(test, str_list)

print(str_list == sorted(str_list))

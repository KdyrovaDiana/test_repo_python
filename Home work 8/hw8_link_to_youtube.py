params = {'v': 'some_id', 'list': 'some_list', 'index': '6', 't': '0s'}
k = 'https://www.youtube.com/watch?'

dict_keys = list(params.keys())
dict_values = list(params.values())
my_list = (list(map(lambda x, y: x + '=' + y, dict_keys, dict_values)))
my_list_1 = '&'.join(my_list)
result_link = k + my_list_1
print(f"result_link = '{result_link}'")

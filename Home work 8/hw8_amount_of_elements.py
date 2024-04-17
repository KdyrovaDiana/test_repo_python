result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'
res = {i: result_link.count(i) for i in result_link}
my_dict = dict(res)
print(f'my_result_link = {my_dict}')

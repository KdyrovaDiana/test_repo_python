course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}
key = (input("Enter the key: "))
key2 = key.lower()

if key2 in course:
    try:
        user = course.get(key2)
        print(f'Your key: {user}')
    except KeyError:
        user = course.get(key2)
else:
    print(f'Oops! Incorrect key entered.')

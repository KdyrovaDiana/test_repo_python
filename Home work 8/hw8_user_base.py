roles = {
    'admin': ['Leo', 'Inna'],
    'maintainer': ['Muhammad', 'Kira'],
    'manager': ['Isla', 'Dina', 'Lena'],
    'developer': ['Lily', 'Mark']
}
v = input("Enter the name: ")
v1 = v.capitalize()
for role in roles:
    if v1 in roles[role]:
        print(f"Hello, {role}")
        break
else:
    if v1 not in roles:
        print(f'Hello, Guest!')

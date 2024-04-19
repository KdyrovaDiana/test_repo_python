with open('new_text.txt', 'r', encoding='utf-8') as file:
    with open('new_2.txt', 'w', encoding='utf-8') as new_file:
        for line in file:
            new_file.write(line)
file.close()

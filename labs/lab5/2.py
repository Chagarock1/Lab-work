def find_whitespace(login):
    for index in range(len(login)):
        if login[index].isspace():
            return index
    return "Немає"

print(f'Тест 1 ("user 7"): {find_whitespace("user 7")}')

print(f'Тест 2 ("\\tadmin"): {find_whitespace("\tadmin")}')

print(f'Тест 3 ("super_user123"): {find_whitespace("super_user123")}')

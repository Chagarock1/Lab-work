def compare_strings(s1, s2):
    if len(s1) != len(s2):
        return "Неможливо порівняти: рядки мають різну довжину"

    differences = 0
    first_diff_index = -1

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            differences += 1
            if first_diff_index == -1:
                first_diff_index = i

    if differences == 0:
        return 0, -1

    return f"відмінностей {differences}; перша {first_diff_index}"

print(f'Тест 1 ("AB12CD", "AB92cD"): {compare_strings("AB12CD", "AB92cD")}')
print(f'Тест 2 ("Python", "Python"): {compare_strings("Python", "Python")}')
print(f'Тест 3 ("Hello", "Hi"): {compare_strings("Hello", "Hi")}')

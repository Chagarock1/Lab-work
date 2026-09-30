def count_spaces(text):
    if not text:
        return 0, 0

    if text.strip(" ") == "":
        return len(text), 0

    leading_spaces = len(text) - len(text.lstrip(" "))
    trailing_spaces = len(text) - len(text.rstrip(" "))

    return leading_spaces, trailing_spaces

res1_start, res1_end = count_spaces("  user7 ")
print(f'Тест 1 ("  user7 "): {res1_start}; {res1_end}')
res2_start, res2_end = count_spaces("    ")
print(f'Тест 2 ("    "): {res2_start}; {res2_end}')
res3_start, res3_end = count_spaces("user7")
print(f'Тест 3 ("user7"): {res3_start}; {res3_end}')

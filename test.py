import re

text = "Hello, !"
pattern = "world"
match = re.search(pattern, text)
if match:
    start = match.start()
    end = match.end()
    print(f"Начало вхождения: {start}, конец вхождения: {end}")
else:
    print("Совпадения не найдены")

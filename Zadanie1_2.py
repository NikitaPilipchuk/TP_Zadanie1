import re

str = input("Введите слово: ").lower()

count_vowels = len(re.findall(r'[aeiou]', str))
count_consonants = len(re.findall(r'[^aeiou]', str))

print(f"Количество гласных букв: {count_vowels}\nКоличество согласных букв: {count_consonants}")

def tanimoto_coefficient(word1, word2):
    intersec = len([char for char in word1 if char in word2])
    return intersec / (len(word1) + len(word2) - intersec)

word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

print(f'Коэффициент Танимото: {tanimoto_coefficient(word1, word2)}') 


# Задача №1. Пользователь вводит текст(строка). Словом считается последовательность 
# непробельных символов идущих подряд, слова разделены одним или большим числом 
# пробелов или символами конца строки.Определите, сколько различных
# слов содержится в этом тексте.

n=int(input("Введите кол-во строк: "))
words = set()
for a in range(n):
    for b in input().split():
        words.add(b)
print(len(words))

# Задача №2. Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и 
# их произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2

a, b = map(int, input("Введите два числа через пробел: ").split())
resultat = []
for i in range(a + b):
    if i == (a * i - b)**0.5:
        resultat.append(i)
print(*resultat if len(resultat) == 2 else resultat + resultat)

# Задача № 4. Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n=int(input("Введите число: "))
p=1
while p<=n:
    print(p,end=' ')
    p=p*2

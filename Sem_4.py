# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))

var_1 = [int(input("Введите элементы первого массива: "))
for i in range(n)]
var_1=set(var_1)

var_2 = [int(input("Введите элементы второго массива: "))
for i in range(m)]
var_2=set(var_2)

res = set()
res = var_1 & var_2

res = list(res)
res.sort()

print(var_1)
print(var_2)
print("Числа, которые встречаются в обоих наборах: ", res)


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное 
# число ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена 
# система автоматического сбора черники. Эта система состоит из управляющего модуля и 
# нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно 
# перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за 
# один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

n=int(input("Введите количество кустов на грядке: "))
arr=list()
for i in range(n):
    x=int(input("Введите количество ягод на кусте: "))
    arr.append(x)

count=list()
for i in range(len(arr)-1):
    count.append(arr[i-1]+arr[i]+arr[i+1])
count.append(arr[-2]+arr[-1]+arr[0])

print(arr)
print("Максимальное число ягод, собранное за ход: ", max(count))
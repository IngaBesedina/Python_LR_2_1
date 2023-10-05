import math

print("Введите стороны прямоугольника:")
a = int(input())
b = int(input())
print("Периметр =", 2 * (a + b))
print("Длина диагонали =", '%.2f' % math.sqrt(a*a+b*b))

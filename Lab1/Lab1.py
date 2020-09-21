import sys

sidesInStr = [i for i in input().split()]
for i in sidesInStr:
    if not i.isnumeric():
        print("Неизвестная ошибка")
        sys.exit()
sides = list(map(float, sidesInStr))
if len(sides) == 3:
    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        print("Не треугольник")  
    elif sides[0] == sides[1] and sides[1] == sides[2]:
        print("Равносторонний")
    elif max(sides) >= sum(sides) - max(sides):
        print("Не треугольник")
    elif sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
        print("Равнобедренный")
    else:
        print("Обычный")
else:
    print("Не треугольник")

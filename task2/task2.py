import math
x = open('test1.txt').read().split(' ')[0]
x = float(x)

y = open('test1.txt').read().split(' ')[1]
y = float(y)

r_circle = open('test1.txt').read().split(' ')[2]
r_circle= float(r_circle)


def coordinates(x_point,y_point):
    x_result = x_point - x
    y_result = y_point - y
    hypotenuse = math.sqrt(x_result ** 2 + y_result ** 2)
    if hypotenuse < r_circle:
        print(1)
    elif hypotenuse > r_circle:
        print(2)
    elif hypotenuse == r_circle:
        print(0)

x_point1 = open('test2.txt').read().split(' ')[0]
x_point1 = float(x_point1)
y_point1 = open('test2.txt').read().split(' ')[1]
y_point1 = float(y_point1)
x_point2 = open('test2.txt').read().split(' ')[2]
x_point2 = float(x_point2)
y_point2 = open('test2.txt').read().split(' ')[3]
y_point2 = float(y_point2)
x_point3 = open('test2.txt').read().split(' ')[4]
x_point3 = float(x_point3)
y_point3 = open('test2.txt').read().split(' ')[5]
y_point3 = float(y_point3)

coordinates(x_point1,y_point1)
coordinates(x_point2,y_point2)
coordinates(x_point3,y_point3)
# 0 -точка лежит на окружности
# 1 - точка внутри
# 2 - очка снаружи
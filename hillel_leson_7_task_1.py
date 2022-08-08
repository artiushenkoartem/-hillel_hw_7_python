"""1) написать функцию которая в качестве аргумента принимает размер стороны квадрата,
а возвращает кортеж в котором лежат три значения:

периметр квадрата
диагональ квадрата
площадь квадрата"""
# create a function called math
def maths(x: int):
    # the function returns a tuple with the values of the perimeter , diagonal and area of the square
    return (4*x, (2*x**2)**.5, x**2)
#
print(maths(7))

def func1(x):
    return x**3-3*x**2+7*x-10


def func2(x):
    return -2*x**3-4*x**2+8*x-4


def func3(x):
    return 2*x**3-3*x**2+4*x-22


def method_left_rectangle(func, a, b, n):
    h = (b-a)/n
    x = a
    ans = 0
    for i in range(n):
        ans += func(x)
        x += h
    return ans*h


def method_right_rectangle(func, a, b, n):
    h = (b-a)/n
    x = a+h
    ans = 0
    for i in range(n):
        ans += func(x)
        x += h
    return ans*h


def method_middle_rectangle(func, a, b, n):
    h = (b-a)/n
    x = a
    ans = 0
    for i in range(n):
        ans += func(x+h/2)
        x += h
    return ans*h


def method_trapezoid(func, a, b, n):
    h = (b-a)/n
    summ = 0
    x = a
    for i in range(1, n):
        summ += func(x)
        x += h
    return h*((func(a)+func(b))/2 + summ)


def Simpsons_method(func, a, b, n):
    h = (b-a)/n
    summ1 = 0
    summ2 = 0
    x = a+h
    for i in range(1,n):
        if i % 2 == 1:
            summ1 += func(x)
        else:
            summ2 += func(x)
        x += h
    return (h/3)*(func(a)+4*summ1+2*summ2+func(b))


def count_integral(func, method, accuracy, a, b, n):
    R = accuracy
    if method == 3:
        ans0 = method_left_rectangle(func, a, b, n)
    elif method == 4:
        ans0 = method_right_rectangle(func, a, b, n)
    elif method == 5:
        ans0 = method_middle_rectangle(func, a, b, n)
    elif method == 1:
        ans0 = method_trapezoid(func, a, b, n)
    else:
        ans0 = Simpsons_method(func, a, b, n)
    while R >= accuracy:
        n *= 2
        if method == 3:
            ans = method_left_rectangle(func, a, b, n)
        elif method == 4:
            ans = method_right_rectangle(func, a, b, n)
        elif method == 5:
            ans = method_middle_rectangle(func, a, b, n)
        elif method == 1:
            ans = method_trapezoid(func, a, b, n)
        else:
            ans = Simpsons_method(func, a, b, n)
        R = abs(ans-ans0)
        ans0 = ans
    return ans, n


def Newtone_Kotes_method(func, a, b, n=8):
    summ = 0
    c = [989/28350*(b-a), 5888/28350*(b-a), -928/28350*(b-a), 10496/28350*(b-a), -4540/28350*(b-a), 10496/28350*(b-a), -928/28350*(b-a), 5888/28350*(b-a), 989/28350*(b-a)]
    h = (b-a)/n
    x = a
    for i in range(n):
        summ += func(x)*c[i]
        x += h
    return summ


def main():
    print("1. x^3-3x^2+7x-10")
    print("2. -2x^3-4x^2+8x-4")
    print("3. 2x^3-3x^2+4x-22")
    function_choose = None
    while function_choose is None:
        function_choose = input("Выберите функцию ")
        if function_choose.isnumeric():
            function_choose = int(function_choose)
            if function_choose < 1 or function_choose > 3:
                print("Введите число от 1 до 3 ")
                function_choose = None
        else:
            print("Ошибка ввода")
            function_choose = None
    accuracy = None
    while accuracy is None:
        try:
            accuracy = float(input("Введите погрешность "))
            if accuracy <= 0:
                print("Погрешност должна быть положительной")
                accuracy = None
        except ValueError:
            print("Ошибка ввода")
    n = 4
    if function_choose:
        func = func1
    a, b = None, None
    while a is None:
        try:
            a = int(input("Введите левую границу интегрирования "))
        except:
            print("Ошибка ввода")
    while b is None:
        try:
            b = int(input("Введите правую границу интегрирования "))
        except:
            print("Ошибка ввода")
    if a > b:
        a, b = b, a
        print("Ошибка границ. Интегралл будет посчитан на отрезке от", a, "до", b)
    method_choose = 0
    while method_choose == 0:
        try:
            method_choose = int(input("Выберите метод:\n"
                                      "1. Метод прямоугольника\n"
                                      "2. Метод трапеций\n"
                                      "3. Метод Симпсона\n"))
            if method_choose < 1 or method_choose > 3:
                print("Введите число от 1 до 3")
                method_choose = 0
        except ValueError:
            print("Ошибка ввода")
            method_choose = 0
    if method_choose == 1:
        method_choose = 0
        while method_choose == 0:
            try:
                method_choose = int(input("Выберите конфигурацию:\n"
                                          "1. Метод левого прямоугольника\n"
                                          "2. Метод правого прямоугольника\n"
                                          "3. Метод среднего прямоугольника\n"))
                if method_choose < 1 or method_choose > 3:
                    print("Введите число от 1 до 3")
                    method_choose = 0
            except ValueError:
                print("Ошибка ввода")
                method_choose = 0
        ans, n_ans = count_integral(func, method_choose+2, accuracy, a, b, n)
    else:
        ans, n_ans = count_integral(func, method_choose-1, accuracy, a, b, n)
    print("Интеграл на отрезке от ", a, " до ", b, " равен ", ans, ". Ответ получен с точностью до ", accuracy, " за ", n_ans, " разбиений", sep='')


main()
# newtone_count = Newtone_Kotes_method(func1, 2, 4)
# rectangle = method_middle_rectangle(func1, 2, 4, 8)
# trapezoid = method_trapezoid(func1, 2, 4, 8)
# Simpsons = Simpsons_method(func1, 2, 4, 8)
# print("Точное значение интеграла: 26")
# print("Интеграл, посчитанный методом Ньютона-Котеса равен", newtone_count)
# print("Относительная погрешность равна", (newtone_count-26)/26)
# print("Интеграл, посчитанный методом средних прямоугольников равен", rectangle)
# print("Относительная погрешность равна", (rectangle-26)/26)
# print("Интеграл, посчитанный методом трапеций равен", trapezoid)
# print("Относительная погрешность равна", (trapezoid-26)/26)
# print("Интеграл, посчитанный методом Симпсона равен", Simpsons)
# print("Относительная погрешность равна", (Simpsons-26)/26)


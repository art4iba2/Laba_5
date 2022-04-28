"""
Формируется матрица F следующим образом: скопировать в нее А и
если в Е максимальный элемент в нечетных столбцах больше, чем сумма чисел в нечетных строках,
то поменять местами С и В симметрично, иначе
В и Е поменять местами несимметрично.
При этом матрица А не меняется.
После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то
вычисляется выражение: A-1*AT – K * F-1, иначе
вычисляется выражение (AТ +G-FТ)*K, где G-нижняя треугольная матрица, полученная из А.
Выводятся по мере формирования А, F и все матричные операции последовательно.
"""

import time
import numpy as np

def print_matrix(M, matr_name):
    print("матрица " + matr_name )
    for i in M:  # делаем перебор всех строк матрицы
        for j in i:  # перебираем все элементы в строке
            print("%5d" % j, end=' ')
        print()

try :
    N = int(input("Введите количество строк (столбцов) квадратной матрицы больше 3 : "))
    while N < 4 :
        N = int(input(
            "Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы больше 3 :"))
    K = int(input("Введите число К="))
    start = time.time()
    A = np.zeros((N,N),dtype=int)
    F = np.zeros((N, N), dtype=int)

    for i in range (N):            #задаем матрицу А
        for j in range(N):
            A[i][j]=np.random.randint(-10,10)
            #A[i][j] = i*10+j

    middle = time.time()
    print("A time = ", middle - start)
    print_matrix(A,"A")

    for i in range (N):            #копируем элементы из матрицы А в F
        for j in range(N):
            F[i][j]=A[i][j]
    E=[]
    n = N // 2
    E = np.zeros((n,n),dtype=int)

    for i in range (n):          #формируем подматрицу E для проверки условий
        for j in range (n):
            E[i][j]=A[i][j]
    print ("E time = ", 0)
    print_matrix(E,"E")
    enumeration = []
    for i in range(n):
        for j in range(n):
            if i%2==0 :
                enumeration.append(E[i][j])
    maxima=max(enumeration)
    print(enumeration, "\nMaximum element in lines= ",maxima )     #ищем нечетный элемент в нечетных строках

    enumeration = []
    for i in range(n):
        for j in range(n):
            if j%2 == 0:
                enumeration.append(E[i][j])
    summ=sum(enumeration)
    print(enumeration, "\nSum element in columns = ",summ )      #находим сумму элементов в нечетных столбцах

    if summ < maxima:
        print("Так как Сумма элементов < максимального элемента => меняем B и С симметрично")
        for i in  range (n):
            for j in range (n):
                F[i][n+j]=A[N-1-i][n+j]
                F[N-1-i][n+j]=A[i][n+j]

    else:
        print("Так как Сумма элементов > максимального элемента => меняем B и E несимметрично")
        F[0:n ,0:n] = A[0:n ,n+N%2 : N]
        F[0:n ,n+N%2 : N] = A[0:n ,0:n]
    middle2 = time.time()
    print_matrix(A,"A")
    print("F new time = ",middle2-middle )
    print_matrix(F,"F")

    if np.linalg.det(A) == 0 or np.linalg.det(F) == 0:
        print("Матрица A или F вырождена => нельзя вычислить")
    elif np.linalg.det(A) > sum(F.diagonal()):

        print("определитель матрицы А больше суммы диагональных элементов матрицы F")
        A = (A - np.dot(1,np.transpose(A)) - np.dot(K,(F-1)))
        finish = time.time()
        print("A time = :", finish - middle2)
        print_matrix(A,"A")
    else:
        print("определитель матрицы А меньше суммы диагональных элементов матрицы F")
        print("Треугольная матрица из А :\n",np.tril(A))

        A = np.dot(np.transpose(A) + np.tril(A) - np.transpose(F) ,K)
        finish = time.time()
        print("A time = :", finish - middle2)
        print_matrix(A,"A")

except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")


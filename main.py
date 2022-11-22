#a, b = int(input('Введите первое число')), int(input('Введите второе число'))
#if a**2 == b:
 #   print('Первое число является квадратом второго')
#elif b**2 == a:
 #   print('Второе число является квадратом первого')
#else:
 #   print('Квадратов нет')


#a, b, c, d, e = int(input('Введите первое число')), int(input('Введите второе число')), int(input('Введите третье число')), int(input('Введите четвертое число')), int(input('Введите пятое число'))
#max = 0
#if a > max:
 #   max = a
#if b > max:
  #  max = b
#if c > max:
#    max = c
#if d > max:
  #  max = d
#if e > max:
   # max = e
#print(f'Максимальное число равно: {max}')

numbers = []
for i in range(1, 6):
    numbers.append(int(input(f'Введите {i} число:')))
max = numbers[0]
for j in range(5):
        if numbers[j] > max:
            max = numbers[j]
            print(f'максимальное число{max}')
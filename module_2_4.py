numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []  # Пустой список простых чисел
not_primes = []  # Пустой список не простых чисел

for i in numbers:  # 1 не простое и не составное число
    if i == 1:     # поэтому пропускаем итерацию цикла, если i=1
        continue

    is_prime = True  # Флаг числа - простое/не простое

    for divisor in range(2, i): 
        if i % divisor == 0:
            is_prime = False
            break  # Выходим из цикла, если найден делитель

    if is_prime:
        primes.append(i)  # Если флаг числа = истина, то добавляем число в список простых чисел
    else:
        not_primes.append(i)  # Иначе, добавляем число в список не простых чисел

print("Primes:", primes)
print("Not Primes:", not_primes)

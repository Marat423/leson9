
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # Дан список

primes = [] # Создаем пустые списки
not_primes = []

for i in range(len(numbers) + 1): # Перебераем список
    if i < 2: # 1 не простое и не сложное
        continue
    is_prime = True # флажок
    for j in range(2, int(i ** 0.5) + 1): # извлекаем корень
        if i % j == 0:
            is_prime = False # флажок
            break

            # Добавляем числа в сушествующий список
    if is_prime:
            primes.append(i)
    else:
            not_primes.append(i)

print(f'Простые числа: {primes}')
print(f'Не простые числа: {not_primes}')

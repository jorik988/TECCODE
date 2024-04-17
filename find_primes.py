# Функция для поиска всех простых чисел в заданном диапазоне
def find_primes(min_num, max_num):
    primes = []
    for num in range(min_num, max_num + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes


print(find_primes(10, 100))

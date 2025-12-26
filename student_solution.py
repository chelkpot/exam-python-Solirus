# student_solution.py

# ---------- ЗАДАНИЕ 1 ----------
def task1():
    s = input()
    sub1, sub2 = s.split(',')
    print(len(sub1) > len(sub2))
    print(sub1 == sub2)
    print(sub2 in sub1)
    # s — строка вида "подстрока1,подстрока2"
    # вернуть кортеж: (len(sub1) > len(sub2), sub1==sub2, sub2 in sub1)
    ...

# ---------- ЗАДАНИЕ 2 ----------
def task2():
    s = input()
    
    print(s.strip())
    print(len(s))
    print(s.count('a'))
    print(s.replace('a', '@'))
    print(s.istitle())
    # s — любая строка
    # вернуть кортеж:
    # (s.strip(), len(s), s.count('a'), s.replace('a','@'), s.istitle())
    ...

# ---------- ЗАДАНИЕ 3 ----------
def task3():
    s = input()
    
    print(s[1:-1])
    print(s[::2])
    print(s.lower()[::-1])
    # s — строка
    # вернуть кортеж: (без первого и последнего символа, каждый второй символ, строка.lower() в обратном порядке)
    ...

# ---------- ЗАДАНИЕ 4 ----------
def task4():
    nums = list(map(int, input().split()))
    
    print(sorted(nums))
    print(sum(nums))
    print(min(nums), max(nums))
    # nums — список чисел
    # вернуть кортеж: (отсортированный список, сумма, (min, max))
    ...


# ---------- ЗАДАНИЕ 5 ----------
def task6():
    s = input()
    lower_s = s.lower()
    is_palindrome = lower_s == lower_s[::-1]
    has_no_spaces = ' ' not in s
    print(is_palindrome and has_no_spaces)
    # s — строка
    # вернуть True если палиндром (без учёта регистра) и нет пробелов, иначе False
    ...

# ---------- ЗАДАНИЕ 6 ----------
def task7():
    n = int(input())
    hex_str = hex(n)[2:]
    print(hex_str)
    print(len(hex_str))
    print('a' in hex_str)
    # n — целое число
    # вернуть кортеж: (hex(n) без '0x', len(hex), True если 'a' есть в hex)
    ...

# ---------- ЗАДАНИЕ 7 ----------
def task8():
    month_num = int(input())
    print(months[month_num - 12])
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # вернуть название месяца по номеру (1-12)
    ...

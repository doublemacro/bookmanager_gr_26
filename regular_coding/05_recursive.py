import sys
sys.setrecursionlimit(10**6)

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, etc
# 0  1  2  3  4  5  6   7   8   9  10....
# bubble-up


# nr urmator -> nr anterior + nr anterior al doiea.


def fibonacci(n, count, memory):
    # daca am ajuns la n = 0, returnam 0
    # n == 1, returnam 1
    # print(f"fibonacci called with n:{n}")
    count[0] += 1

    # verifica daca avem numarul in memorie.
    checked_number = memory.get(n)
    if checked_number is None:
        if n == 0:
            memory[n] = 0
            return 0
        if n == 1:
            memory[n] = 1
            return 1
        result = fibonacci(n-1, count, memory) + fibonacci(n - 2, count, memory)
        memory[n] = result
        return result
    else:
        # daca numarul este deja salvat in memorie, putem sa-l returnam direct si aia e
        return memory[n]

count = [0]
memory = {}

result = fibonacci(2000, count, memory) # calculeaza-mi al 10-lea numar fibonacci.
print(result)
print(f"count: {count}")


# lst = [0, 1, 1, 2, 3]
# #      0  1  2  3  4
# for i in range(len(lst)):
#     print(f"pentru indexul {i} avem valoare {lst[i]}")

# lst = []
# print(lst[4])


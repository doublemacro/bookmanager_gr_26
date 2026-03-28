
# fibonacci
# (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...)


numbers = [2, 3, 5, 10, 20, 100]
it = iter(numbers)

# print(next(it))

# while True:
#     try:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         break

# for x in it:
#     print(x)

# for i in range(10_000_000_000):
#     print(i)

# custom iterator:

class Counter:
    def __init__(self, max_val):
        self.max_val = max_val
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        # aici se face pasul:
        self.current = self.current + 1

        # verificam daca am ajuns la maxim. daca am ajuns, aruncam exceptie.
        if self.current >= self.max_val:
            # aruncam/cream o exceptie.
            raise StopIteration

        return self.current


# for i in Counter(10):
#     print(i)

# fibonacci iterator:
# (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...)

class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration

        self.count += 1
        value = self.b

        intermediar = self.a
        self.a = self.b
        self.b = intermediar + self.b

        return value


for x in Fibonacci(10):
    print(x)

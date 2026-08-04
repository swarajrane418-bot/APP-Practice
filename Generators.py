def numbers():
    yield 1
    yield 2
    yield 3

gen = numbers()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
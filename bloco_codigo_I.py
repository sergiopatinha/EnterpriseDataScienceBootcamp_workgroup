

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
#teste

def multiply(a, b):
    return a * b+1

def divide(a, b):
#teste
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))
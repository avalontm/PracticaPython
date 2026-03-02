# ============================================================
# Practica: Programacion Funcional en Python
# ============================================================

from functools import reduce

# ------------------------------------------------------------
# Ejercicio 1: Funcion pura suma(a, b)
# Solo depende de sus parametros (sin efectos secundarios)
# ------------------------------------------------------------

def suma(a, b):
    return a + b

print("=" * 50)
print("Ejercicio 1: Funcion pura suma(a, b)")
print(f"  suma(3, 7)   = {suma(3, 7)}")
print(f"  suma(10, 25) = {suma(10, 25)}")


# ------------------------------------------------------------
# Ejercicio 2: Funcion recursiva factorial(n)
# ------------------------------------------------------------

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("\n" + "=" * 50)
print("Ejercicio 2: Factorial recursivo")
for i in [0, 1, 5, 7, 10]:
    print(f"  factorial({i:2}) = {factorial(i)}")


# ------------------------------------------------------------
# Ejercicio 3: Funcion recursiva Fibonacci(n)
# Retorna el n-esimo numero de la serie de Fibonacci
# ------------------------------------------------------------

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\n" + "=" * 50)
print("Ejercicio 3: Fibonacci recursivo")
serie = [fibonacci(i) for i in range(11)]
print(f"  Fibonacci(0..10) = {serie}")
print(f"  fibonacci(8)     = {fibonacci(8)}")


# ------------------------------------------------------------
# Ejercicio 4: map, filter y reduce sobre [1..10]
# ------------------------------------------------------------

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\n" + "=" * 50)
print("Ejercicio 4: map, filter y reduce")
print(f"  Lista original: {numeros}")

# -- 4a: Cuadrados con map --
cuadrados = list(map(lambda x: x ** 2, numeros))
print(f"\n  4a) Cuadrados con map:")
print(f"      {cuadrados}")

# -- 4b: Numeros pares con filter --
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"\n  4b) Numeros pares con filter:")
print(f"      {pares}")

# -- 4c: Suma de [1..10] con reduce --
suma_total = reduce(lambda acc, x: acc + x, numeros)
print(f"\n  4c) Suma de [1..10] con reduce:")
print(f"      {suma_total}")

# -- 4d: Producto de [1..5] con reduce --
primeros_cinco = [1, 2, 3, 4, 5]
producto = reduce(lambda acc, x: acc * x, primeros_cinco)
print(f"\n  4d) Producto de [1..5] con reduce:")
print(f"      {producto}  (equivale a 5! = {factorial(5)})")

print("\n" + "=" * 50)
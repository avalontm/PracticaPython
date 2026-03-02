# PracticaPython

Repositorio de practica sobre Programacion Funcional en Python.

---

## Descripcion

Este proyecto contiene ejercicios practicos que demuestran los conceptos fundamentales
de la programacion funcional aplicados en Python. Los ejercicios cubren funciones puras,
recursividad y el uso de funciones de orden superior como `map`, `filter` y `reduce`.

---

## Contenido

### Ejercicio 1 - Funcion pura

Implementacion de una funcion `suma(a, b)` que solo depende de sus parametros de entrada,
sin efectos secundarios ni dependencias externas. Este es el principio basico de una
funcion pura en el paradigma funcional.

### Ejercicio 2 - Factorial recursivo

Funcion recursiva `factorial(n)` que calcula el factorial de un numero entero no negativo.
Utiliza un caso base para `n == 0` y `n == 1`, y se llama a si misma para los demas casos.

### Ejercicio 3 - Fibonacci recursivo

Funcion recursiva `fibonacci(n)` que retorna el n-esimo numero de la serie de Fibonacci.
Aplica recursion doble con casos base para `n == 0` y `n == 1`.

### Ejercicio 4 - map, filter y reduce

Operaciones funcionales sobre la lista `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`:

- `map` para generar una nueva lista con los cuadrados de cada elemento.
- `filter` para obtener unicamente los numeros pares.
- `reduce` para calcular la suma de los numeros del 1 al 10.
- `reduce` para calcular el producto de los numeros del 1 al 5.

---

## Requisitos

- Python 3.8 o superior
- No se requieren librerias externas (solo `functools` de la libreria estandar)

---

## Uso

```bash
git clone https://github.com/avalontm/PracticaPython.git
cd PracticaPython
python main.py
```

---

## Conceptos cubiertos

| Concepto              | Descripcion                                              |
|-----------------------|----------------------------------------------------------|
| Funcion pura          | Salida determinada unicamente por sus argumentos         |
| Recursividad          | Funcion que se invoca a si misma con un caso base        |
| Funcion de orden superior | Funcion que recibe o retorna otras funciones         |
| map                   | Aplica una funcion a cada elemento de una coleccion      |
| filter                | Filtra elementos segun una condicion booleana            |
| reduce                | Acumula los elementos de una coleccion en un solo valor  |

---

## Autor

**avalontm**  
[https://github.com/avalontm](https://github.com/avalontm)

---

## Licencia

Este proyecto se distribuye con fines educativos y de practica personal.
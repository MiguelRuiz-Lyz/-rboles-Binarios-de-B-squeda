# Apuntes de teoría — Árboles Binarios de Búsqueda

## Árbol binario vs. Árbol binario de búsqueda
Ambos tienen como máximo dos hijos por nodo. En el ABB, además, el hijo izquierdo es siempre menor que el nodo y el hijo derecho es siempre mayor.

## Modelo estático vs. dinámico
- **Estático:** capacidad fija. Si se llena, no se puede insertar más.
  ```python
  CAPACIDAD = 6
  vector = [None] * CAPACIDAD
  ```
- **Dinámico:** la estructura crece según se necesite (`append`, `insert`, `pop`, `remove`, `len`).

## ¿Qué es `None`?
Valor especial de Python (`NoneType`) que representa la ausencia de un valor. **No** es `0`, **ni** `""`, **ni** `False`. Permite reservar posiciones vacías y asignarlas luego por índice sin provocar `IndexError`.

## Representación vectorial de un árbol completo
```
         15                        índice:  0   1   2   3   4   5   6
       /    \                      vector: [15,  6, 20,  3,  9, 18, 24]
      6      20
    /  \    /  \
   3    9  18   24

hijo_izquierdo = 2*i + 1
hijo_derecho   = 2*i + 2
```
(En este proyecto se usa otra variante: cada nodo guarda los índices de sus hijos.)

## Recorridos
Para el árbol anterior:

| Recorrido | Regla | Resultado |
|---|---|---|
| Inorden | Izquierda → Raíz → Derecha | `[3, 6, 9, 15, 18, 20, 24]` |
| Preorden | Raíz → Izquierda → Derecha | `[15, 6, 3, 9, 20, 18, 24]` |
| Postorden | Izquierda → Derecha → Raíz | `[3, 9, 6, 18, 24, 20, 15]` |

El recorrido **inorden** de un ABB siempre devuelve los elementos **ordenados**.

## Operaciones primitivas
`crear()`, `vacio()`, `insertar(elemento)`, `eliminar(elemento)`, `buscar(elemento)`.

Casos de `eliminar`: (1) hoja, (2) nodo con un hijo, (3) nodo con dos hijos.

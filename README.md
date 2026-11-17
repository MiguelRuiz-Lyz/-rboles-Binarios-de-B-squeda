# 🌳 Árbol Binario de Búsqueda (ABB) con modelo estático

> **Materia:** Estructura de Datos II (INF-310)
> **Unidad 1:** Árboles Binarios de Búsqueda
> **Práctica:** Entender el ATD Árbol Binario
> **Autor:** Miguel Ruiz Loayza · **Fecha:** 19/08/2026

Implementación en **Python** del ATD (Árbol Binario de Búsqueda) usando un **vector de capacidad fija** (modelo estático) para almacenar **nombres**, con recorrido **inorden**.

---

## 📚 ¿Qué es un Árbol Binario de Búsqueda?

Un árbol binario es una estructura donde cada nodo tiene **como máximo dos hijos**. Se vuelve un **ABB** cuando además cumple:

- El hijo **izquierdo** es **menor** que el nodo.
- El hijo **derecho** es **mayor** que el nodo.

Gracias a esa regla, en cada comparación se descarta una mitad del árbol, lo que da búsquedas muy rápidas (eficiencia logarítmica cuando el árbol está balanceado).

```
              Miguel
             /      \
        Carlos      Pedro
        /    \          \
     Ana    Luis        Rosa
                            \
                            Zoe
```

## 🧱 Modelo estático

El árbol se guarda en un **vector de tamaño fijo** (`capacidad = 50` por defecto). Python no tiene arreglos estáticos, así que se simula con:

```python
vector = [None] * capacidad
```

- `None` indica una **posición libre**.
- Si todas las posiciones están ocupadas, `insertar` retorna `False`.
- Cada posición guarda un objeto `Nodo` cuyos hijos son **índices del vector** (no referencias).

> **Nota:** esta implementación **no** usa las fórmulas `2*i+1` / `2*i+2` (esa es la representación de heap/árbol completo). Aquí cada nodo guarda el **índice** de su hijo izquierdo y derecho, y los nodos pueden ir en cualquier posición libre.

Ejemplo real del vector tras insertar `Miguel, Carlos, Pedro, Ana, Luis, Rosa, Zoe`:

```
[0] Miguel  Izq: 1     Der: 2
[1] Carlos  Izq: 3     Der: 4
[2] Pedro   Izq: None  Der: 5
[3] Ana     Izq: None  Der: None
[4] Luis    Izq: None  Der: None
[5] Rosa    Izq: None  Der: 6
[6] Zoe     Izq: None  Der: None
```

## ⚙️ Operaciones primitivas del ATD

| Operación | Descripción | Retorno |
|---|---|---|
| `crear()` | Inicializa el árbol vacío | — |
| `vacio()` | ¿La raíz es `None`? | `True` / `False` |
| `insertar(elemento)` | Inserta respetando la regla del ABB. No permite duplicados | `True` si insertó, `False` si hay duplicado o no hay espacio |
| `buscar(elemento)` | Busca un elemento | Índice en el vector, o `None` |
| `eliminar(elemento)` | Elimina un elemento | `True` si lo eliminó, `False` si no existe |
| `inorden()` | Recorrido Izquierda → Raíz → Derecha | Lista de elementos **ordenados** |
| `mostrar_vector()` | Imprime el contenido interno del vector | — |

### Casos de eliminación

1. **Hoja:** se desconecta del padre y se libera su posición.
2. **Un hijo:** el padre se conecta directamente con ese hijo.
3. **Dos hijos:** se copia el valor del **sucesor inorden** (el menor del subárbol derecho) al nodo y luego se elimina físicamente el sucesor.

### Complejidad

| Operación | Tiempo |
|---|---|
| `buscar` | O(h) |
| `insertar` | O(n) por la búsqueda de espacio libre en el vector + O(h) del descenso |
| `eliminar` | O(h) |
| `inorden` | O(n) |

*(h = altura del árbol, n = cantidad de nodos. En un árbol balanceado h ≈ log n; en el peor caso h = n.)*

## 🗂️ Estructura del proyecto

```
arbol-binario-nombres/
├── .vscode/
│   ├── launch.json          # Configuración para ejecutar/depurar con F5
│   └── settings.json        # Configuración de tests en VS Code
├── docs/
│   └── teoria.md            # Apuntes de teoría de la práctica
├── src/
│   ├── __init__.py
│   ├── nodo.py              # Clase Nodo
│   └── arbol_binario_busqueda.py   # ATD Árbol Binario de Búsqueda
├── tests/
│   ├── __init__.py
│   └── test_arbol.py        # Pruebas unitarias (unittest)
├── .gitignore
├── main.py                  # Programa de demostración
└── README.md
```

## ✅ Requisitos

- [Python 3.8 o superior](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/) con la extensión **Python** (opcional pero recomendado)
- [Git](https://git-scm.com/) (para control de versiones)

No se necesitan librerías externas.

## ▶️ Cómo ejecutarlo

Desde la carpeta raíz del proyecto:

```bash
python main.py
```

En Windows, si `python` no funciona, prueba con `py main.py`. En Linux/macOS, `python3 main.py`.

## 🧪 Cómo ejecutar las pruebas

```bash
python -m unittest -v
```

Deberías ver `Ran 12 tests ... OK`.

## 🖥️ Ejemplo de salida

```
¿El árbol está vacío?
False

Recorrido inorden:
['Ana', 'Carlos', 'Luis', 'Miguel', 'Pedro', 'Rosa', 'Zoe']

Contenido del vector:
[0] Elemento: Miguel, Izq: 1, Der: 2
[1] Elemento: Carlos, Izq: 3, Der: 4
[2] Elemento: Pedro, Izq: None, Der: 5
[3] Elemento: Ana, Izq: None, Der: None
[4] Elemento: Luis, Izq: None, Der: None
[5] Elemento: Rosa, Izq: None, Der: 6
[6] Elemento: Zoe, Izq: None, Der: None

¿Existe Carlos? (índice en el vector)
1

Eliminando Ana (hoja)...
Inorden después de eliminar Ana:
['Carlos', 'Luis', 'Miguel', 'Pedro', 'Rosa', 'Zoe']

Eliminando Carlos (un hijo)...
Inorden después de eliminar Carlos:
['Luis', 'Miguel', 'Pedro', 'Rosa', 'Zoe']

Eliminando Miguel (raíz con dos hijos)...
Inorden después de eliminar Miguel:
['Luis', 'Pedro', 'Rosa', 'Zoe']

Contenido final del vector:
[0] Elemento: Pedro, Izq: 4, Der: 5
[4] Elemento: Luis, Izq: None, Der: None
[5] Elemento: Rosa, Izq: None, Der: 6
[6] Elemento: Zoe, Izq: None, Der: None
```

## 🚀 Posibles mejoras

- [ ] Agregar recorridos **preorden** y **postorden**.
- [ ] Versión **dinámica** (nodos enlazados, sin capacidad fija).
- [ ] Autobalanceo (AVL).
- [ ] Mejorar `insertar` para que no recorra el vector buscando espacio (lista de posiciones libres).

## 👤 Autor

**Miguel Ruiz Loayza** — Estructura de Datos II (INF-310)

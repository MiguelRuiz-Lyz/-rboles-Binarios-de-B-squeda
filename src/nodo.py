# Título :  Nodo del Árbol Binario de Búsqueda
# Autor  :  Miguel Ruiz Loayza
# Fecha  :  19/08/2026
# ====================================================


class Nodo:
    """Representa un nodo almacenado dentro del vector.

    En el modelo estático los hijos no son referencias a otros nodos,
    sino ÍNDICES (posiciones) dentro del vector. Si un hijo no existe,
    su valor es None.
    """

    def __init__(self, elemento):
        self.elemento = elemento
        self.hijo_izquierdo = None
        self.hijo_derecho = None

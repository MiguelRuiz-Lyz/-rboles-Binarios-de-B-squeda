# Título :  Árbol Binario con recorrido en Inorden y modelo estático
# Autor  :  Miguel Ruiz Loayza
# Fecha  :  19/08/2026
# ====================================================
from src.nodo import Nodo


class ArbolBinarioBusqueda:
    """ATD Árbol Binario de Búsqueda implementado mediante un vector."""

    def __init__(self, capacidad=50):
        """Creo un árbol vacío con capacidad."""
        self.vector = [None] * capacidad
        self.raiz = None
        self.capacidad = capacidad

    def crear(self):
        """Inicializo el árbol como vacío."""
        self.vector = [None] * self.capacidad
        self.raiz = None

    def vacio(self):
        """Retorna True si el árbol está vacío."""
        return self.raiz is None

    def _obtener_espacio(self):
        """Busca una posición libre dentro del vector."""
        for i in range(self.capacidad):
            if self.vector[i] is None:
                return i

        return None

    def insertar(self, elemento):
        """
        Inserta un elemento manteniendo la propiedad del ABB.

        No se permiten elementos duplicados.
        Retorna True si se insertó y False si no fue posible.
        """
        nuevo_indice = self._obtener_espacio()

        if nuevo_indice is None:
            return False

        nuevo_nodo = Nodo(elemento)

        if self.vacio():
            self.vector[nuevo_indice] = nuevo_nodo
            self.raiz = nuevo_indice
            return True

        actual = self.raiz

        while True:
            nodo_actual = self.vector[actual]

            if elemento == nodo_actual.elemento:
                return False

            if elemento < nodo_actual.elemento:
                if nodo_actual.hijo_izquierdo is None:
                    self.vector[nuevo_indice] = nuevo_nodo
                    nodo_actual.hijo_izquierdo = nuevo_indice
                    return True

                actual = nodo_actual.hijo_izquierdo

            else:
                if nodo_actual.hijo_derecho is None:
                    self.vector[nuevo_indice] = nuevo_nodo
                    nodo_actual.hijo_derecho = nuevo_indice
                    return True

                actual = nodo_actual.hijo_derecho

    def buscar(self, elemento):
        """
        Busca un elemento en el árbol.

        Retorna el índice del nodo si existe.
        Retorna None si no existe.
        """
        actual = self.raiz

        while actual is not None:
            nodo_actual = self.vector[actual]

            if elemento == nodo_actual.elemento:
                return actual

            if elemento < nodo_actual.elemento:
                actual = nodo_actual.hijo_izquierdo
            else:
                actual = nodo_actual.hijo_derecho

        return None

    def eliminar(self, elemento):
        """
        Elimina un elemento del árbol.

        Retorna True si el elemento fue eliminado.
        Retorna False si el elemento no existe.
        """
        indice = self.buscar(elemento)

        if indice is None:
            return False

        padre = self._buscar_padre(indice)

        # Caso 1: el nodo es una hoja.
        if self._es_hoja(indice):
            self._desconectar_padre(padre, indice)
            self.vector[indice] = None

        # Caso 2: el nodo tiene un solo hijo.
        elif self._tiene_un_hijo(indice):
            hijo = self._obtener_unico_hijo(indice)

            if padre is None:
                self.raiz = hijo
            else:
                self._conectar_padre(padre, indice, hijo)

            self.vector[indice] = None

        # Caso 3: el nodo tiene dos hijos.
        else:
            sucesor = self._buscar_sucesor(indice)
            valor_sucesor = self.vector[sucesor].elemento

            self.vector[indice].elemento = valor_sucesor

            self._eliminar_sucesor(sucesor)

        return True

    def _buscar_padre(self, indice_buscado):
        """Busca el índice del padre de un nodo."""
        if self.raiz is None or self.raiz == indice_buscado:
            return None

        actual = self.raiz

        while actual is not None:
            nodo_actual = self.vector[actual]

            if nodo_actual.hijo_izquierdo == indice_buscado:
                return actual

            if nodo_actual.hijo_derecho == indice_buscado:
                return actual

            if self.vector[indice_buscado].elemento < nodo_actual.elemento:
                actual = nodo_actual.hijo_izquierdo
            else:
                actual = nodo_actual.hijo_derecho

        return None

    def _es_hoja(self, indice):
        """Determina si un nodo no tiene hijos."""
        nodo = self.vector[indice]

        return (
            nodo.hijo_izquierdo is None
            and nodo.hijo_derecho is None
        )

    def _tiene_un_hijo(self, indice):
        """Determina si un nodo tiene exactamente un hijo."""
        nodo = self.vector[indice]

        tiene_izquierdo = nodo.hijo_izquierdo is not None
        tiene_derecho = nodo.hijo_derecho is not None

        return tiene_izquierdo != tiene_derecho

    def _obtener_unico_hijo(self, indice):
        """Retorna el único hijo de un nodo."""
        nodo = self.vector[indice]

        if nodo.hijo_izquierdo is not None:
            return nodo.hijo_izquierdo

        return nodo.hijo_derecho

    def _desconectar_padre(self, padre, indice):
        """Desconecta un nodo hoja de su padre."""
        if padre is None:
            self.raiz = None
            return

        nodo_padre = self.vector[padre]

        if nodo_padre.hijo_izquierdo == indice:
            nodo_padre.hijo_izquierdo = None
        else:
            nodo_padre.hijo_derecho = None

    def _conectar_padre(self, padre, indice, hijo):
        """Conecta el padre con el hijo del nodo eliminado."""
        nodo_padre = self.vector[padre]

        if nodo_padre.hijo_izquierdo == indice:
            nodo_padre.hijo_izquierdo = hijo
        else:
            nodo_padre.hijo_derecho = hijo

    def _buscar_sucesor(self, indice):
        """
        Busca el sucesor inorden de un nodo.

        El sucesor es el menor elemento del subárbol derecho.
        """
        nodo = self.vector[indice]
        actual = nodo.hijo_derecho

        while self.vector[actual].hijo_izquierdo is not None:
            actual = self.vector[actual].hijo_izquierdo

        return actual

    def _eliminar_sucesor(self, sucesor):
        """
        Elimina físicamente el nodo sucesor.

        El sucesor puede tener como máximo un hijo derecho.
        """
        padre = self._buscar_padre(sucesor)
        nodo_sucesor = self.vector[sucesor]

        hijo = nodo_sucesor.hijo_derecho

        if padre is None:
            self.raiz = hijo

        else:
            nodo_padre = self.vector[padre]

            if nodo_padre.hijo_izquierdo == sucesor:
                nodo_padre.hijo_izquierdo = hijo
            else:
                nodo_padre.hijo_derecho = hijo

        self.vector[sucesor] = None

    def inorden(self):
        """Realiza el recorrido inorden del árbol."""
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)

        return resultado

    def _inorden_recursivo(self, indice, resultado):
        """Función auxiliar para realizar el recorrido inorden."""
        if indice is None:
            return

        nodo = self.vector[indice]

        self._inorden_recursivo(nodo.hijo_izquierdo, resultado)

        resultado.append(nodo.elemento)

        self._inorden_recursivo(nodo.hijo_derecho, resultado)

    def mostrar_vector(self):
        """Muestra el contenido interno del vector."""
        for indice, nodo in enumerate(self.vector):
            if nodo is not None:
                print(
                    f"[{indice}] "
                    f"Elemento: {nodo.elemento}, "
                    f"Izq: {nodo.hijo_izquierdo}, "
                    f"Der: {nodo.hijo_derecho}"
                )

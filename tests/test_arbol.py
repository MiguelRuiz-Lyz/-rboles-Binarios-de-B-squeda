import unittest

from src.arbol_binario_busqueda import ArbolBinarioBusqueda

NOMBRES = ["Miguel", "Carlos", "Pedro", "Ana", "Luis", "Rosa", "Zoe"]


def crear_arbol(capacidad=50):
    arbol = ArbolBinarioBusqueda(capacidad)
    for nombre in NOMBRES:
        arbol.insertar(nombre)
    return arbol


class TestArbolBinarioBusqueda(unittest.TestCase):

    def test_arbol_nuevo_esta_vacio(self):
        self.assertTrue(ArbolBinarioBusqueda().vacio())

    def test_insertar_y_inorden_ordenado(self):
        arbol = crear_arbol()
        self.assertFalse(arbol.vacio())
        self.assertEqual(arbol.inorden(), sorted(NOMBRES))

    def test_no_permite_duplicados(self):
        arbol = crear_arbol()
        self.assertFalse(arbol.insertar("Ana"))
        self.assertEqual(len(arbol.inorden()), len(NOMBRES))

    def test_capacidad_llena(self):
        arbol = ArbolBinarioBusqueda(capacidad=3)
        self.assertTrue(arbol.insertar("B"))
        self.assertTrue(arbol.insertar("A"))
        self.assertTrue(arbol.insertar("C"))
        self.assertFalse(arbol.insertar("D"))

    def test_buscar(self):
        arbol = crear_arbol()
        self.assertIsNotNone(arbol.buscar("Carlos"))
        self.assertIsNone(arbol.buscar("Inexistente"))

    def test_eliminar_hoja(self):
        arbol = crear_arbol()
        self.assertTrue(arbol.eliminar("Ana"))
        self.assertEqual(arbol.inorden(), sorted(set(NOMBRES) - {"Ana"}))

    def test_eliminar_nodo_con_un_hijo(self):
        arbol = crear_arbol()
        arbol.eliminar("Ana")
        self.assertTrue(arbol.eliminar("Carlos"))
        self.assertEqual(
            arbol.inorden(), sorted(set(NOMBRES) - {"Ana", "Carlos"})
        )

    def test_eliminar_raiz_con_dos_hijos(self):
        arbol = crear_arbol()
        self.assertTrue(arbol.eliminar("Miguel"))
        self.assertEqual(arbol.inorden(), sorted(set(NOMBRES) - {"Miguel"}))
        self.assertIsNone(arbol.buscar("Miguel"))

    def test_eliminar_inexistente(self):
        self.assertFalse(crear_arbol().eliminar("Inexistente"))

    def test_eliminar_todo_deja_arbol_vacio(self):
        arbol = crear_arbol()
        for nombre in NOMBRES:
            self.assertTrue(arbol.eliminar(nombre))
        self.assertTrue(arbol.vacio())
        self.assertEqual(arbol.inorden(), [])

    def test_reutiliza_espacios_liberados(self):
        arbol = ArbolBinarioBusqueda(capacidad=3)
        for n in ["B", "A", "C"]:
            arbol.insertar(n)
        arbol.eliminar("A")
        self.assertTrue(arbol.insertar("A"))

    def test_crear_reinicia_el_arbol(self):
        arbol = crear_arbol()
        arbol.crear()
        self.assertTrue(arbol.vacio())


if __name__ == "__main__":
    unittest.main()

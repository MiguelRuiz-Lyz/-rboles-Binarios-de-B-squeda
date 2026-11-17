# Título :  Programa principal - Prueba del ABB con nombres
# Autor  :  Miguel Ruiz Loayza
# Fecha  :  19/08/2026
# ====================================================
from src.arbol_binario_busqueda import ArbolBinarioBusqueda


def main():
    """Prueba las operaciones principales del ABB."""

    arbol = ArbolBinarioBusqueda()

    for nombre in ["Miguel", "Carlos", "Pedro", "Ana", "Luis", "Rosa", "Zoe"]:
        arbol.insertar(nombre)

    print("¿El árbol está vacío?")
    print(arbol.vacio())

    print("\nRecorrido inorden:")
    print(arbol.inorden())

    print("\nContenido del vector:")
    arbol.mostrar_vector()

    print("\n¿Existe Carlos? (índice en el vector)")
    print(arbol.buscar("Carlos"))

    print("\nEliminando Ana (hoja)...")
    arbol.eliminar("Ana")
    print("Inorden después de eliminar Ana:")
    print(arbol.inorden())

    print("\nEliminando Carlos (un hijo)...")
    arbol.eliminar("Carlos")
    print("Inorden después de eliminar Carlos:")
    print(arbol.inorden())

    print("\nEliminando Miguel (raíz con dos hijos)...")
    arbol.eliminar("Miguel")
    print("Inorden después de eliminar Miguel:")
    print(arbol.inorden())

    print("\nContenido final del vector:")
    arbol.mostrar_vector()


if __name__ == "__main__":
    main()

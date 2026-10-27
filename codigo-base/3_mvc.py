"""Modelo-Vista-Controlador: catálogo de la biblioteca."""


# ===================== MODELO =====================
class Catalogo:                        # datos + avisa cuando cambia
    def __init__(self):
        self.libros = {"Clean Architecture": True, "Refactoring": True,
                       "Design Patterns": True}
        self.vistas = []

    def prestar(self, titulo):
        self.libros[titulo] = False
        for vista in self.vistas:
            vista.mostrar(self)


# ====================== VISTA ======================
class VistaLista:                      # solo muestra
    def mostrar(self, catalogo):
        for titulo, libre in catalogo.libros.items():
            estado = "disponible" if libre else "prestado"
            print(f"  {titulo}: {estado}")


class VistaResumen:                    # segunda vista agregada por el reto
    def mostrar(self, catalogo):
        libres = sum(catalogo.libros.values())
        total = len(catalogo.libros)
        print(f"Disponibles: {libres} de {total}")


# =================== CONTROLADOR ===================
class Controlador:                     # recibe la orden del usuario
    def __init__(self, catalogo):
        self.catalogo = catalogo

    def orden(self, texto):
        print(f"> {texto}")
        if texto.startswith("prestar "):
            self.catalogo.prestar(texto[len("prestar "):])


catalogo = Catalogo()
catalogo.vistas.append(VistaLista())
catalogo.vistas.append(VistaResumen())
controlador = Controlador(catalogo)
controlador.orden("prestar Refactoring")

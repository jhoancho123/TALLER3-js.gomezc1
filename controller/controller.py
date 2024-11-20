# controller.py
from models import Boa_Constrictor, Hurón
from views import Vista

class Controlador:
    def __init__(self):
        self.vista = Vista()

    def mostrar_sonido(self, animal):
        """Llama al método hacer_sonido del animal y lo muestra en la vista"""
        sonido = animal.hacer_sonido()
        self.vista.mostrar_sonido(sonido)

    def mostrar_flete(self, animal):
        """Llama al método calcular_flete del animal y lo muestra en la vista"""
        flete = animal.calcular_flete()
        self.vista.mostrar_flete(flete)

    def alimentar_boa(self, boa: Boa_Constrictor, cantidad: int):
        """Alimenta a la boa con una cantidad de ratones"""
        for _ in range(cantidad):
            boa.agregar_ratón()
        self.vista.mostrar_ratones_comidos(boa.ratones_comidos)

# Instanciar el controlador para gestionar la interacción
controlador = Controlador()

# Crear animales
boa = Boa_Constrictor(pais_origen="Brasil", impuestos=10.0, peso=5.0)
huron = Hurón(pais_origen="Argentina", impuestos=5.0, peso=2.5)

# Usar el controlador para mostrar los datos
controlador.mostrar_sonido(boa)        # Salida: El sonido del animal es: ¡Tsss!
controlador.mostrar_flete(boa)         # Salida: El costo de importación es: $50.00
controlador.alimentar_boa(boa, 3)      # Salida: La boa ha comido 3 ratones.
controlador.mostrar_sonido(huron)      # Salida: El sonido del animal es: ¡Eek Eek!
controlador.mostrar_flete(huron)       # Salida: El costo de importación es: $12.50
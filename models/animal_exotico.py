class Guarderia:
    def __init__(self):
        # Creamos 2 boas y 2 hurones en la guardería
        self.boas = [Boa_Constrictor(pais_origen="Brasil", impuestos=10.0, peso=5.0),
                     Boa_Constrictor(pais_origen="Perú", impuestos=12.0, peso=6.0)]
        self.hurones = [Hurón(pais_origen="Argentina", impuestos=5.0, peso=2.5),
                        Hurón(pais_origen="Chile", impuestos=6.0, peso=2.0)]

    def alimentar_boa(self, boa):
        """Alimenta a la boa recibida, maneja los casos de excepción y éxito."""
        try:
            # Verificamos si la boa recibida es None
            if boa is None:
                raise ValueError("Esta Boa no existe!")
            
            # Intentamos alimentar a la boa
            boa.agregar_ratón()
            print("Éxito")

        except ValueError as e:
            # Si la boa ha comido 10 ratones, lanzamos un error de demasiados ratones
            if str(e) == "Demasiados Ratones!":
                print("La boa está llena")
            # Si el argumento es None, lanzamos el error correspondiente
            elif str(e) == "Esta Boa no existe!":
                print(e)
            # Para cualquier otro error de agregar ratón
            else:
                print(f"Error inesperado: {e}")

class Animal_Exotico:
    def __init__(self, pais_origen: str, impuestos: float, peso: float):
        self.pais_origen = pais_origen
        self.impuestos = impuestos
        self.peso = peso

    def calcular_flete(self) -> float:
        """Calcula el flete, es decir, el costo de importación del animal"""
        return self.impuestos * self.peso

    def hacer_sonido(self):
        """Método que debe ser implementado en la clase hija"""
        raise NotImplementedError("El método hacer_sonido debe ser implementado en la clase hija")


class Boa_Constrictor(Animal_Exotico):
    def __init__(self, pais_origen: str, impuestos: float, peso: float):
        super().__init__(pais_origen, impuestos, peso)
        self.ratones_comidos = 0

    def hacer_sonido(self):
        """Sonido característico de la Boa"""
        return "¡Tsss!"

    def agregar_ratón(self):
        """Método para agregar un ratón a la cuenta de ratones comidos.
        Si la boa ya ha comido 10 ratones, lanza un ValueError."""
        if self.ratones_comidos >= 20:
            raise ValueError("Demasiados Ratones!")
        self.ratones_comidos += 1


class Hurón(Animal_Exotico):
    def __init__(self, pais_origen: str, impuestos: float, peso: float):
        super().__init__(pais_origen, impuestos, peso)

    def hacer_sonido(self):
        """Sonido característico del Hurón"""
        return "¡Eek Eek!"
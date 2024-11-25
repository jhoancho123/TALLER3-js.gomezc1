class Vista:
    def mostrar_sonido(self, sonido: str):
        """Muestra el sonido hecho por el animal"""
        print(f"El sonido del animal es: {sonido}")

    def mostrar_flete(self, flete: float):
        """Muestra el costo de importación del animal"""
        print(f"El costo de importación es: ${flete:.2f}")

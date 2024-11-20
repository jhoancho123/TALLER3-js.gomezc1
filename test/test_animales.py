import unittest
from models import Boa_Constrictor, Hurón
from views import Vista
from controller import Controlador

class TestControlador(unittest.TestCase):
    def setUp(self):
        """Método que se ejecuta antes de cada prueba"""
        self.controlador = Controlador()
        self.boa = Boa_Constrictor(pais_origen="Brasil", impuestos=10.0, peso=5.0)
        self.huron = Hurón(pais_origen="Argentina", impuestos=5.0, peso=2.5)

    def test_huron_hacer_sonido(self):
        """Prueba del sonido del hurón"""
        self.assertEqual(self.huron.hacer_sonido(), "¡Eek Eek!")

    def test_boa_hacer_sonido(self):
        """Prueba del sonido de la boa"""
        self.assertEqual(self.boa.hacer_sonido(), "¡Tsss!")

    def test_huron_calcular_flete(self):
        """Prueba del cálculo de flete para el hurón"""
        self.assertEqual(self.huron.calcular_flete(), 12.5)

    def test_boa_calcular_flete(self):
        """Prueba del cálculo de flete para la boa"""
        self.assertEqual(self.boa.calcular_flete(), 50.0)

    def test_boa_agregar_raton(self):
        """Prueba de alimentar a la boa"""
        self.assertEqual(self.boa.ratones_comidos, 0)
        self.boa.agregar_ratón()
        self.assertEqual(self.boa.ratones_comidos, 1)
        self.boa.agregar_ratón()
        self.assertEqual(self.boa.ratones_comidos, 2)

    def test_mostrar_sonido(self):
        """Prueba que el controlador llama correctamente a la vista para mostrar el sonido"""
        with self.assertLogs('controller', level='INFO') as log:
            self.controlador.mostrar_sonido(self.boa)
            self.assertIn("El sonido del animal es: ¡Tsss!", log.output)

    def test_mostrar_flete(self):
        """Prueba que el controlador llama correctamente a la vista para mostrar el flete"""
        with self.assertLogs('controller', level='INFO') as log:
            self.controlador.mostrar_flete(self.huron)
            self.assertIn("El costo de importación es: $12.50", log.output)

    def test_alimentar_boa(self):
        """Prueba que el controlador llama correctamente a la vista para alimentar a la boa"""
        with self.assertLogs('controller', level='INFO') as log:
            self.controlador.alimentar_boa(self.boa, 3)
            self.assertIn("La boa ha comido 3 ratones.", log.output)

if __name__ == '__main__':
    unittest.main()
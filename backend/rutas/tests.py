import math
from django.test import SimpleTestCase

from .utils import (
    analizar_cercania_ruta,
    calcular_distancia,
    encontrar_indice_mas_cercano,
)


class HaversineTests(SimpleTestCase):
    def test_distancia_mismo_punto_es_cero(self):
        punto = {'lat': -16.3989, 'lng': -71.5370}
        self.assertAlmostEqual(calcular_distancia(punto, punto), 0.0, places=9)

    def test_distancia_un_grado_de_latitud(self):
        p1 = {'lat': 0.0, 'lng': 0.0}
        p2 = {'lat': 1.0, 'lng': 0.0}
        self.assertAlmostEqual(calcular_distancia(p1, p2), 111194.93, delta=0.5)

    def test_distancia_plaza_armas_terminal_terrestre(self):
        origen = {'lat': -16.3989, 'lng': -71.5370}
        destino = {'lat': -16.4298, 'lng': -71.5192}
        self.assertAlmostEqual(calcular_distancia(origen, destino), 3925.59, delta=0.5)

    def test_distancia_es_simetrica(self):
        origen = {'lat': -16.3989, 'lng': -71.5370}
        destino = {'lat': -16.4298, 'lng': -71.5192}
        self.assertAlmostEqual(
            calcular_distancia(origen, destino),
            calcular_distancia(destino, origen),
            places=9,
        )

    def test_distancia_punto_cercano(self):
        origen = {'lat': -16.3989, 'lng': -71.5370}
        cercano = {'lat': -16.3939, 'lng': -71.5370}
        self.assertAlmostEqual(calcular_distancia(origen, cercano), 555.97, delta=0.5)

    def test_formula_asin_equivalente_a_atan2(self):
        def haversine_asin(p1, p2):
            r = 6371000.0
            lat1 = math.radians(p1['lat'])
            lon1 = math.radians(p1['lng'])
            lat2 = math.radians(p2['lat'])
            lon2 = math.radians(p2['lng'])
            dlat = lat2 - lat1
            dlon = lon2 - lon1
            a = (
                math.sin(dlat / 2.0) ** 2
                + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2.0) ** 2
            )
            return 2.0 * r * math.asin(math.sqrt(min(1.0, a)))

        pares = [
            ({'lat': -16.3989, 'lng': -71.5370}, {'lat': -16.4298, 'lng': -71.5192}),
            ({'lat': 0.0, 'lng': 0.0}, {'lat': 1.0, 'lng': 0.0}),
            ({'lat': -16.3989, 'lng': -71.5370}, {'lat': -16.3939, 'lng': -71.5370}),
        ]
        for p1, p2 in pares:
            self.assertAlmostEqual(
                calcular_distancia(p1, p2),
                haversine_asin(p1, p2),
                delta=1e-6,
            )


class CercaniaTests(SimpleTestCase):
    def test_analizar_cercania_ruta_devuelve_punto_mas_cercano(self):
        referencia = {'lat': -16.3989, 'lng': -71.5370}
        ruta = [
            [-16.4298, -71.5192],
            [-16.4150, -71.5280],
            [-16.3989, -71.5370],
        ]
        resultado = analizar_cercania_ruta(referencia, ruta)
        self.assertEqual(resultado['indice'], 2)
        self.assertEqual(resultado['coord'], [-16.3989, -71.5370])
        self.assertAlmostEqual(resultado['distancia'], 0.0, places=9)

    def test_analizar_cercania_ruta_elige_el_menor(self):
        referencia = {'lat': -16.3989, 'lng': -71.5370}
        ruta = [
            [-16.4039, -71.5370],
            [-16.3989, -71.5370],
        ]
        resultado = analizar_cercania_ruta(referencia, ruta)
        self.assertEqual(resultado['indice'], 1)
        self.assertAlmostEqual(resultado['distancia'], 0.0, places=9)

    def test_encontrar_indice_mas_cercano(self):
        referencia = {'lat': -16.3989, 'lng': -71.5370}
        ruta = [
            [-16.4298, -71.5192],
            [-16.3989, -71.5370],
            [-16.4150, -71.5280],
        ]
        self.assertEqual(encontrar_indice_mas_cercano(referencia, ruta), 1)

    def test_distancia_de_transbordo_supera_cien_metros(self):
        p1 = {'lat': -16.3989, 'lng': -71.5370}
        p2 = {'lat': -16.3979, 'lng': -71.5370}
        self.assertGreater(calcular_distancia(p1, p2), 100.0)

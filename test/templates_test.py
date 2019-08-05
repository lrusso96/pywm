from pywmit.templates.cite import CitaWeb, CitaPubblicazione, CitaLibro
import unittest


class TestTemplateClass(unittest.TestCase):
    def test_cita_web(self):
        cita_web = CitaWeb()
        self.assertEqual(cita_web.name, "cita web")

    def test_cita_libro(self):
        cita_libro = CitaLibro()
        self.assertEqual(cita_libro.name, "cita libro")

    def test_cita_pubblicazione(self):
        cita_pubblicazione = CitaPubblicazione()
        self.assertEqual(cita_pubblicazione.name, "cita pubblicazione")


if __name__ == '__main__':
    unittest.main()

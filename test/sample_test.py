"""from pywmit.templates.cite import CitaWeb, CitaPubblicazione, CitaLibro
from pywmit.parser import parse
import unittest


class TestSampleMethods(unittest.TestCase):
    def test_simple(self):
        wikicode = parse("Placca iberica")
        templates = wikicode.filter_templates()
        cita_web = CitaWeb()
        self.assertEqual(cita_web.name, 'cita web')
        cita_pubblicazione = CitaPubblicazione()
        cita_libro = CitaLibro()
        for t in templates:
            a = t.params
            if t.name.matches('cita web'):
                cita_web.check_params(a)
            elif t.name.matches('cita pubblicazione'):
                cita_pubblicazione.check_params(a)
            elif t.name.matches('cita libro'):
                cita_libro.check_params(a)
        print(wikicode)


if __name__ == '__main__':
    unittest.main()
"""
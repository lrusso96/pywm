from pywmit.parser import parse
from pywmit.templates.cite import CitaWeb, CitaLibro, CitaPubblicazione


def check(page):
    wikicode = parse(page)
    templates = wikicode.filter_templates()
    cita_web = CitaWeb()
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
import argparse
from utils import parse
from cite import CitaWeb, CitaLibro, CitaPubblicazione


def check(page):
    wikicode = parse(page)
    templates = wikicode.filter_templates()
    cita_web = CitaWeb()
    cita_pubblicazione = CitaPubblicazione()
    cita_libro = CitaLibro()
    for t in templates:
        if t.name.matches('cita web'):
            cita_web.check_params(t)
        elif t.name.matches('cita pubblicazione'):
            cita_pubblicazione.check_params(t)
        elif t.name.matches('cita libro'):
            cita_libro.check_params(t)


def setup_parser():
    # set the main parser
    parser = argparse.ArgumentParser(description='Template checker')
    parser.add_argument("page")
    # create the parser
    return parser.parse_args()


if __name__ == '__main__':
    args = setup_parser()
    check(args.page)

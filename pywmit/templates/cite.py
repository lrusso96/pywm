from pywmit.templates.base import Template, Param

# fixme: handle "nome" and "cognome" fields
# todo: add "cita news"


class CitaLibro(Template):
    def __init__(self):
        super().__init__('cita libro')
        self.params = set()
        self.params.add(Param('titolo', kind=Param.Kind.REQUIRED))
        self.params.add(Param('autore', kind=Param.Kind.SUGGESTED, has_many=True))
        self.params.add(Param('wkautore', has_many=True))
        self.params.add(Param('curatore'))
        self.params.add(Param('traduttore'))
        self.params.add(Param('illustratore'))
        self.params.add(Param('altri'))
        self.params.add(Param('url'))
        self.params.add(Param('via'))
        self.params.add(Param('editore', kind=Param.Kind.SUGGESTED))
        self.params.add(Param('città', Param.Kind.SUGGESTED))
        self.params.add(Param('anno', Param.Kind.SUGGESTED))
        self.params.add(Param('data', Param.Kind.SUGGESTED))
        self.params.add(Param('lingua'))
        self.params.add(Param('annooriginale'))
        self.params.add(Param('volume'))
        self.params.add(Param('opera'))
        self.params.add(Param('edizione'))
        self.params.add(Param('capitolo'))
        self.params.add(Param('url_capitolo'))
        self.params.add(Param('p'))
        self.params.add(Param('pp'))
        self.params.add(Param('posizione'))
        self.params.add(Param('isbn'))
        self.params.add(Param('lccn'))
        self.params.add(Param('doi'))
        self.params.add(Param('oclc'))
        self.params.add(Param('id'))
        self.params.add(Param('cid'))
        self.params.add(Param('citazione'))
        self.params.add(Param('accesso'))
        self.params.add(Param('urlarchivio'))
        self.params.add(Param('dataarchivio'))
        self.params.add(Param('urlmorto'))


# fixme: add 'data' field (not in official docs!)
class CitaPubblicazione(Template):
    def __init__(self):
        super().__init__('cita pubblicazione')
        self.params = set()
        self.params.add(Param('titolo', kind=Param.Kind.REQUIRED))
        self.params.add(Param('autore', kind=Param.Kind.SUGGESTED, has_many=True))
        self.params.add(Param('curatore', kind=Param.Kind.SUGGESTED))
        self.params.add(Param('wkautore', has_many=True))
        self.params.add(Param('rivista', kind=Param.Kind.SUGGESTED))
        self.params.add(Param('volume', kind=Param.Kind.SUGGESTED))
        self.params.add(Param('numero', kind=Param.Kind.SUGGESTED))
        self.params.add(Param('editore'))
        self.params.add(Param('città'))
        self.params.add(Param('data'))
        self.params.add(Param('anno'))
        self.params.add(Param('mese'))
        self.params.add(Param('p'))
        self.params.add(Param('pp'))
        self.params.add(Param('lingua'))
        self.params.add(Param('issn'))
        self.params.add(Param('doi'))
        self.params.add(Param('pmid'))
        self.params.add(Param('id'))
        self.params.add(Param('cid'))
        self.params.add(Param('url'))
        self.params.add(Param('formato'))
        self.params.add(Param('accesso'))
        self.params.add(Param('abstract'))
        self.params.add(Param('urlarchivio'))
        self.params.add(Param('dataarchivio'))
        self.params.add(Param('urlmorto'))
        # fixme: accepted but not (yet) in official docs!
        self.params.add(Param('isbn'))
        self.params.add(Param('bibcode'))
        self.params.add(Param('jstor'))


class CitaWeb(Template):
    def __init__(self):
        super().__init__('cita web')
        self.params = set()
        self.params.add(Param('url', kind=Param.Kind.REQUIRED))
        self.params.add(Param('titolo', kind=Param.Kind.REQUIRED))
        self.params.add(Param('autore', has_many=True))
        self.params.add(Param('sito', kind=Param.Kind.SUGGESTED))
        self.params.add(Param('data', kind=Param.Kind.SUGGESTED))
        self.params.add(Param('accesso', kind=Param.Kind.SUGGESTED))
        self.params.add(Param('wkautore', has_many=True))
        self.params.add(Param('editore'))
        self.params.add(Param('lingua'))
        self.params.add(Param('formato'))
        self.params.add(Param('p'))
        self.params.add(Param('pp'))
        self.params.add(Param('cid'))
        self.params.add(Param('citazione'))
        self.params.add(Param('urlarchivio'))
        self.params.add(Param('dataarchivio'))
        self.params.add(Param('urlmorto'))

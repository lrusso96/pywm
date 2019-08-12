import logging
from typing import Set
from enum import Enum


def setup_logger():
    log_format = '%(levelname)s (%(name)s): %(message)s'
    _logger = logging.getLogger('pywm')
    file_handler = logging.StreamHandler()
    formatter = logging.Formatter(log_format)
    file_handler.setFormatter(formatter)
    _logger.addHandler(file_handler)
    return _logger


logger = setup_logger()


class Param:
    class Kind(Enum):
        OPTIONAL = 1
        SUGGESTED = 2
        REQUIRED = 3

    def __init__(self, title: str, kind=Kind.OPTIONAL, has_many=False):
        self.kind = kind
        self.title = title
        self.has_many = has_many

    def is_required(self) -> bool:
        return self.kind == Param.Kind.REQUIRED

    def is_suggested(self) -> bool:
        return self.kind == Param.Kind.SUGGESTED

    def matches(self, title: str) -> bool:
        if self.title == title.strip():
            return True
        elif self.has_many and title.startswith(self.title):
            return title[len(self.title):].isdigit()
        else:
            return False


class Template:
    params: Set[Param]

    def __init__(self, name: str):
        self.name = name
        self.params = set()

    def check_params(self, attrs: list):
        miss_required = set(x.title for x in set(self.params) if x.is_required())
        miss_suggested = set(x.title for x in set(self.params) if x.is_suggested())
        suspected = set()
        for att in attrs:
            for par in self.params:
                s = str(att.name)
                if par.matches(s):
                    miss_required.discard(par.title)
                    miss_suggested.discard(par.title)
                    suspected.discard(s)
                    break
                else:
                    suspected.add(s)
        for m in miss_required:
            logger.warning('missing required parameter in %s: %s', self.name, m)
        for m in suspected:
            logger.warning('invalid parameter in %s: %s', self.name, m)
        for m in miss_suggested:
            logger.info('missing suggested parameter in %s: %s', self.name, m)

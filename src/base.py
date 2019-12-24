from typing import Set
from enum import Enum
from utils import *


class Param:
    class Kind(Enum):
        OPTIONAL = 1
        SUGGESTED = 2
        REQUIRED = 3

    def __init__(self, title: str, kind=Kind.OPTIONAL, has_many=False):
        self.kind = kind
        self.title = title
        self.has_many = has_many

    def is_required(self):
        return self.kind == Param.Kind.REQUIRED

    def is_suggested(self):
        return self.kind == Param.Kind.SUGGESTED

    def matches(self, title: str):
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

    def check_params(self, template):
        attrs = template.params
        miss_required = set(x.title for x in set(
            self.params) if x.is_required())
        miss_suggested = set(x.title for x in set(
            self.params) if x.is_suggested())
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

        if(len(miss_required) > 0 or len(suspected) > 0 or len(miss_suggested) > 0):
            for p in ["titolo", "url", 1]:
                try:
                    id = template.get(p).value
                    break
                except ValueError:
                    id = "-"
                    pass

            print_init()
            print_normal(f'\n== {self.name} ==')
            print_ok(f'id: {id}\n')

        for m in miss_required:
            print_error(f'missing required parameter: {m}')
        for m in suspected:
            print_debug(f'invalid parameter: {m}')
        for m in miss_suggested:
            print_accent(f'missing suggested parameter: {m}')

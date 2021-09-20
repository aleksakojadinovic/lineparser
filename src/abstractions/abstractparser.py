"""
An abstract class representing a parser
"""
from typing import List, Dict


class StoreFetcher:
    def __init__(self, psystem, key):
        self.psystem = psystem
        self.key = key


    def get(self):
        return self.psystem.get_data(self.key)

    def __call__(self, *args, **kwargs):
        return self.get()

class ParsedUnit:
    def __init__(self, data, storage_key):
        self.data = data
        self.storage_key = storage_key


# TODO: allow separator (here or in specific parsers? or create an abstract class SequenceParser? idk)
class AbstractParser:
    def __init__(self, **kwargs):
        self.single_lined = False
        if 'scope' not in kwargs or kwargs['scope'] is None or kwargs['scope'] == 1:
            kwargs['scope'] = 1
            self.single_lined = True

        self.data = dict(kwargs)
        self.storage_key = None

    def parse_(self, in_data) -> ParsedUnit:
        for key in self.data:
            entry = self.data[key]
            if isinstance(entry, StoreFetcher):
                self.data[key] = entry.get()

        pdata = self.parse(in_data, self.data)
        return ParsedUnit(pdata, self.storage_key)

    def parse(self, in_data, meta):
        raise NotImplementedError

    def into(self, key):
        self.storage_key = key
        return self

    def __gt__(self, other):
        return self.into(other)



class ParseSystem:
    def __init__(self):
        self.units: List[AbstractParser] = []
        self.storage_keys = []
        self.saved_data = dict()


    def parse_input(self, **kwargs):
        if 'file' in kwargs:
            lines = kwargs['file'].read().splitlines()
        elif 'filepath' in kwargs:
            lines = open(kwargs['filepath'], 'r').read().splitlines()
        elif 'lines' in kwargs:
            lines = kwargs['lines']
        elif 'str' in kwargs:
            # TODO: Won't work on windows, fetch newline from sys/env or wherever
            lines = kwargs['str'].split("\n")
        else:
            raise ValueError(f'No input found.')

        # TODO: Temporary, to avoid warning. Partial parsing will be allowed.
        if not self.units:
            raise ValueError(f'No parsing units found.')

        lines_start = 0
        for i, unit in enumerate(self.units):
            unit_scope = unit.data['scope']
            if isinstance(unit_scope, StoreFetcher):
                unit_scope = unit_scope.get()
            unit_lines = lines[lines_start:lines_start + unit_scope]
            lines_start += unit_scope
            if unit.single_lined:
                unit_lines = unit_lines[0]
            punit: ParsedUnit = unit.parse_(unit_lines)
            if punit.storage_key is not None:
                if isinstance(punit.storage_key, str):
                    self[punit.storage_key] = punit.data
                else:
                    for single_key, single_val in zip(punit.storage_key, punit.data):
                        self[single_key] = single_val




        # for i, (line, unit) in enumerate(zip(lines, self.units)):
        #     punit: ParsedUnit = unit.parse_(line)
        #     if punit.storage_key is not None:
        #         if isinstance(punit.storage_key, str):
        #             self[punit.storage_key] = punit.data
        #         else:
        #             # Assume iterable of strings and data iterable of something
        #             for single_key, single_val in zip(punit.storage_key, punit.data):
        #                 self[single_key] = single_val





    def __call__(self, **kwargs):
        return self.parse_input(**kwargs)

    def get_data(self, key):
        return self.saved_data[key]


    def set_data(self, key, value):
        self.saved_data[key] = value

    def __setitem__(self, key, value):
        self.set_data(key, value)

    def add_unit(self, p: AbstractParser):
        self.units.append(p)
        return self

    def __iadd__(self, other):
        self.add_unit(other)
        return self

    def fetch(self, key):
        return StoreFetcher(self, key)

    def __getitem__(self, item):
        return self.fetch(item)















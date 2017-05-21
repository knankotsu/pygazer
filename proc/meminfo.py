#-*- coding: utf-8 -*-
import re

# My modules
import utils
import template

class MemValue(object):
    def __init__(self, value, unit):
        self.value = utils.parse_value(value)
        self.unit = unit

class MemInfos(template.Template):
    def __init__(self):
        super().__init__("/proc/meminfo")
        self.scan()

    def scan(self):
        for line in self._fd.readlines():
            if len(line) <= 1:
                continue
            name, value = line.split(':')

            name = re.sub(r'\((.+)\)', r'_\1', name).lower()
            value = value.lstrip().rstrip()
            try:
                value, unit = value.split(" ")
                value = MemValue(value, unit)
            except:
                pass

            setattr(self, name, value)
        self.close()

if __name__ == '__main__':
    minfo = MemInfos()
    print(vars(minfo))
    from IPython import embed; embed()

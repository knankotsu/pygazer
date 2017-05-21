#-*- coding: utf-8 -*-
import pprint


# My modules
import template
import utils

class CpuInfos(template.Template):
    def __init__(self):
        super().__init__("/proc/cpuinfo")
        self.scan()

    def scan(self):
        for line in self._fd.readlines():
            if len(line) <= 1: #空行は無視
                continue

            name, value = tuple(line.split(':'))

            name = name.rstrip().replace(" ", "_")
            value = value.lstrip().rstrip()

            setattr(self, name, value)
        self.close()

if __name__ == '__main__':
    cinfo = CpuInfos()
    print(vars(cinfo))
    from IPython import embed; embed()



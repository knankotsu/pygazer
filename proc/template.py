#-*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class Template(metaclass=ABCMeta):
    def __init__(self, path):
        self._fd = open(path, "r")

    @abstractmethod
    def scan(self):
        """
        procfs上のファイルを解析する
        :return:
        """
        pass

    def close(self):
        self._fd.close()

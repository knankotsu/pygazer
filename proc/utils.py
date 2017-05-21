#-*- coding: utf-8 -*-

def parse_value(value):
    try:
        return int(value)
    except ValueError:
        try:
            return int(value, 16)
        except:
            try:
                return float(value)
            except:
                return value
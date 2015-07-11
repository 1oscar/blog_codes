#!/usr/bin/env python
#coding=utf8

#python 2.7.8

class Singleton(type):
    _instances = {}

    def __call__(class_, *args, **kw):
        if  class_ not in class_._instances:
            class_._instances[class_] = super(Singleton, class_).__call__(*args, **kw)
        return class_._instances[class_]
    

class KaiFei(object):
        __metaclass__ = Singleton



kai = KaiFei()
fei = KaiFei()

print id(kai), id(fei)
print kai, fei

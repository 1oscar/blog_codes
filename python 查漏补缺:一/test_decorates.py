#!/usr/bin/env python
#coding=utf8

# _ 防止与关键字冲突
def Singleton(class_):
    instances = {}

    def get_instance(*args, **kw):
        if class_ not in instances:
            instances[class_] = class_(*args, **kw)
        return instances[class_]
    
    return get_instance


@Singleton
class kaifei(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

kai = kaifei('kai')
fei = kaifei('fei')

print id(kai), id(fei)
print kai, fei

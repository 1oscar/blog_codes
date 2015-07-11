#!/usr/bin/env python
#coding=utf-8


class Singleton(object):

    def __new__(class_, *args, **kw):
        if not hasattr(class_, '_instance'):
            class_._instance = super(Singleton, class_).__new__(class_, *args, **kw)
        
        return class_._instance


class Kaifei(Singleton):
    
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    

if __name__ == '__main__':
    kai = Kaifei('kai')
    fei = Kaifei('fei')
    print id(kai), id(fei)
    print kai, fei


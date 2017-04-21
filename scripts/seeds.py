# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from faker import Factory

def run():
    fakes = Factory.create('zh_CN')

    for x in xrange(1,100):
    	print fakes.name(), fakes.phone()


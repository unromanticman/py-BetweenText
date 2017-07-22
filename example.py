#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# python 2.7.11

from BetweenText import BetweenText

text =  BetweenText.get('<body>get this text</body>','<body>','</body>')
print text

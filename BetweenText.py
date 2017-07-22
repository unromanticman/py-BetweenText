#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# python 2.7.11


class BetweenText:

    @staticmethod
    def get(text,st,ed):
		text = text.split(st)[1]
		text = text.split(ed)[0]
		return text



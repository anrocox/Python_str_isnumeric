#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 8, 2014

@author: anroco

How to determine if characters of a python str are numerics?

¿Como determinar si los caracteres de un str python son numericos?
'''

#create a str
s = '123¾Ⅹ'
print(s)

#the isnumeric() method verify if all characters in the string are numeric
#characters. Return True or False.
#
#Include all characters that have the Unicode numeric property with the value
#Numeric_Type=Digit, Numeric_Type=Decimal or Numeric_Type=Numeric
print(s.isnumeric())

#create a str
s = '1.234'
print(s)

#return False because '.' isn't a numeric character
print(s.isnumeric())

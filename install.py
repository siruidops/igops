#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os,sys

print
logo = """
 ___           _        _ _
|_ _|_ __  ___| |_ __ _| | |
 | || '_ \/ __| __/ _` | | |
 | || | | \__ \ || (_| | | |
|___|_| |_|___/\__\__,_|_|_|
"""
print logo
print
raw_input('[*] Please press enter to install[] ')
s = os.system('pip install -r requirements.txt')
print
print " -!- Installed -!-"
print "   Run With: './igops.py'"
print

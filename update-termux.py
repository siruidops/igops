#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib
import sys
import os

red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 
tur="\033[0;36m"
yellow="\033[1;33m"
end="\033[1;37m"

url = 'https://github.com/siruidops/igops'

logo = yellow+"""
 _   _           _       _
| | | |_ __   __| | __ _| |_ ___
| | | | '_ \ / _` |/ _` | __/ _ \
| |_| | |_) | (_| | (_| | ||  __/
 \___/| .__/ \__,_|\__,_|\__\___|
      |_|
"""+end

def update():
	print
	print logo
	print
	try:
		u = urllib.urlopen(url)
	except Exception as error:
		print green+'  [-] ',error,end
		print
		sys.exit()
	v = open('version.txt','r').read()
	if v == u.read():
		print brown+"  [!] Not new version found"+end
		print
		sys.exit()
	else:
		print green+"  [*] New version found"
		print
		print tur+"      Name   :"+pur+" igops"+end
		print tur+"      Version:"+pur+" "+u.read()+end
		print
		try:
			conf = raw_input('Press Enter To Update ...')
		except:
			print
			sys.exit()
		os.chdir('..')
		os.mkdir('igops-'+u.read())
		os.chdir('igops-'+u.read())
		git = os.system('git clone https://github.com/siruidops/igops.git')
		os.chdir('igops')
		os.system('python2 install.py')
		print
		print green+" ------ Updated ------"+end
		print "  Name   : igops"
		print "  Version: "+u.read()
		print "  Path   : ../igops-"+u.read()+"/igops/"
		print

if __name__ == '__main__':
	update()
else:
	pass





#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Tested on Linux ( Kali Linux , Debian )

##               In The Name Of God                  ##
#                                                     #
# Subject  : Robots Analyze                           #
# Time     : 2018-02-05 20:48                         #
# Developer: Sir uidops                               #
# Email    : Sir.u1d0p5@gmail.com                     #
# Telegram : https://t.me/Sir_uidops                  #
# Github   : https://github.com/siruidops/              #
#
##         Copy Right For Me (Sir Uidops)            ##

# for errors in this script and help 
#    please send a message for me
#
# Email    : Sir.u1d0p5@gmail.com
# Telegram : https://t.me/Sir_uidops
#

red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 
tur="\033[0;36m"
yellow="\033[1;33m"
end="\033[1;37m"

info = {'dev'   :'sir uidops',
		'email' :'sir.u1d0p5@gmail.com',
		'github':'https://github.com/siruidops/igops/'
}

queryIndex = ['robots.txt',
'search/',
'admin/',
'login/',
'sitemap.xml',
'sitemap2.xml',
'config.php',
'wp-login.php',
'log.txt',
'update.php',
'INSTALL.pgsql.txt',
'user/login/',
'INSTALL.txt',
'profiles/',
'scripts/',
'LICENSE.txt',
'CHANGELOG.txt',
'themes/',
'inculdes/',
'misc/',
'user/logout/',
'user/register/',
'cron.php',
'filter/tips/',
'comment/reply/',
'xmlrpc.php',
'modules/',
'install.php',
'MAINTAINERS.txt',
'user/password/',
'node/add/',
'INSTALL.sqlite.txt',
'UPGRADE.txt',
'INSTALL.mysql.txt']

try:
	import sys
	import os
	from socket import *
	import builtwith
	import urllib
	import urlparse
	import time
	import dns.resolver
	import whois
	import re
	import getopt
	import subprocess
	import google
	import html5lib
	from bs4 import BeautifulSoup
except ImportError:
	print
	print red+" [-] Please install reuquiremenets.txt"+end
	print green+"     pip install -r requiremenets.txt"+end
	print
	sys.exit()

def scan(target):
	try:
		rtio = gethostbyname(target)
	except:
		print
		print red+" [-] Please connect to a network internet"+end
		print
		sys.exit()
	#netlocation = urlparse.urlparse(target).netloc
	url   = "http://%s/"%(target)
	print
	print yellow+" Url: ",url,end
	print yellow+" IP : ",gethostbyname(target),end
	print
	print yellow+" [!] Analyze Robots.txt ..."+end
	print
	for i in queryIndex:
		robotsURL = "%s%s"%(url,i)
		robots = urllib.urlopen(robotsURL)
		if robots.code == 200:
			print green+"    [+] 200: "+robotsURL+end
		else:
			print red+"    [-] ",robots.code,': '+robotsURL+end
		splitRobots = robots.read().split('\n')
		for i in splitRobots:
			try:
				commit = urllib.urlopen(i)
				if commit.code == 200:
					print "    [+] 200: %s"%(robotsURL)
			except:
				pass
	print
	print yellow+" [!] Analyze SiteMap.xml"+end
	print
	sitemapURL = "%ssitemap.xml"%(url)
	sitemapURL2 = "%ssitemap2.xml"%(url)
	sitemap = urllib.urlopen(sitemapURL)
	sitemap2 = urllib.urlopen(sitemapURL2)
	print brown+"    [!] %d: %s"%(sitemap.code, sitemapURL)
	print brown+"    [!] %d: %s"%(sitemap2.code, sitemapURL2)
	print end
	print
	print yellow+" [!] Simple Port Scan"+end
	print
	print pur+'  PORT    '+tur+'STATE    '+green+'Service'+end
	enport = [7,19,20,21,22,23,25,42,43,49,53,67,68,69,70,79,80,88,102,110,113,119,123,135,137,139,143,161,162,177,179,201,264,318,381,383,389,411,412,443,445,464,465,497,500,563,587,593,636,902,989,990,993,995,1025,1194,1241,2082,2083,3306,3074,3389,4664,5050,5500,5800,5900,8000,8080,8200,9988,5190]
	print green
	for port in enport:
		try:
			s = socket(AF_INET, SOCK_STREAM)
			res = s.connect_ex((target, port))
			s.close()
		except Exception as error:
			print
			print red+'  '+str(error)+end
			continue
		if res == 0:
			try:
				service = getservbyport(port, 'tcp')
			except:
				service = 'Unknow'
			if len(str(port)) == 4:
				print pur+'  '+str(port)+'    '+tur+'Open'+'     '+green+str(service)+end
			elif len(str(port)) == 3:
				print pur+'  '+str(port)+'     '+tur+'Open'+'     '+green+str(service)+end
			elif len(str(port)) == 2:
				print pur+'   '+str(port)+'     '+tur+'Open'+'     '+green+str(service)+end
			elif len(str(port)) == 1:
				print pur+'     '+str(port)+'    '+tur+'Open'+'     '+green+str(service)+end
			elif len(str(port)) == 5:
				print pur+'  '+str(port)+'   '+tur+'Open'+'     '+green+str(service)+end
			else:
				pass
		else:
			pass
	print end
	print yellow+" [!] Analyze Banner of Port"+end
	banners = urllib.urlopen(url)
	print green
	for i,j in banners.headers.items():
		print "    %s : %s"%(i,j)
	print end
	print
	print yellow+" [!] Analyze Technology"+end
	print green
	b = builtwith.parse(url)
	for i,j in b.iteritems():
		k = ', '.join(j)
		print '    ',i,': ',k
	print end
	print yellow+" [!] Analyze IP Reverse"
	print
	sb = gethostbyaddr(gethostbyname(target))
	for i in sb:
		if type(i) == list:
			data = '\n    '.join(i)
			print green+"    "+data,end
		else:
			print green+"    "+i,end
	print
	print yellow+" [!] Analyze DNS 'A' Recorde"+end
	print 
	answersA = dns.resolver.query(target, 'A')
	for i in answersA.response.answer:
		for j in i.items:
			print green+"    ",j.to_text()
	print
	print yellow+" [!] Analyze DNS 'MX' Recorde"+end
	print
	answersMX = dns.resolver.query(target, 'MX')
	for i in answersMX.response.answer:
		for j in i.items:
			print green+"    ",j.to_text()
	print
	print yellow+" [!] Analyze DNS 'NS' Recorde"+end
	print
	answersNS = dns.resolver.query(target, 'NS')
	for i in answersNS.response.answer:
		for j in i.items:
			print green+"    ",j.to_text()
	print
	print yellow+" [!] Whois Scan"+end
	print green
	wh = whois.whois(target)
	for i,j in wh.iteritems():
		print "    ",i,' : ',j
	print end
	print yellow+" [!] Analyze Email"+end
	print
	html = urllib.urlopen(url).read()
	i = re.findall('[\w]+@[\w.]+', html)
	for j in i:
			print "    ",j
	print
	print yellow+" [!] Analyze urls"+end
	print
	url = "https://%s/"%(target)
	u = urllib.urlopen(url)
	s = BeautifulSoup(u.read(), 'html.parser')
	all = s.find_all('a')
	print green
	for i in all:
		print '    ',i['href']
	all = s.find_all('img')
	print green
	for i in all:
		print '    ',i['src']
	print end
	print yellow+" [!] Analyze Google Index of Target"+end
	print
	try:
		g = google.search('site:%s'%(target))
		for i in g:
			print green+"    "+i+end
	except:
		pass
	print
	print green+" [+] Scan Finished !"+end
	print
logo = yellow+"""
     _/_/_/_/_/
         _/
         _/      _/_/_/_/       _/_/_/  _/_/_/ _/_/_/
         _/      _/    _/      _/   _/ _/  _/   _/
         _/      _/_/_/_/     _/   _/ _/_/_/     _/
     _/_/_/_/_/        _/     _/_/_/ _/      _/_/_/
                       _/           _/ \033[0;31mversion 1.0\033[1;33m
                 _/_/_/_/          _/
"""

def banner():
	print
	print logo
	print
	print tur+"Developer"+end+': '+pur+info['dev']+end
	print tur+"E-mail"+end+'   : '+pur+info['email']+end
	print tur+"Github"+end+'   : '+pur+info['github']+end
	print
	print yellow+"\tUsage: ./igops.py [\033[0;32mOptions\033[1;33m]"+end
	print
	print green+"Options:"+end
	print 
	print tur+"    [-t Target]    "+end+': '+pur+"Target Adress to scan e.g: google.com or 163.234.56.77"+end
	print tur+"    [-r]           "+end+': '+pur+"Show README.md File"+end
	print tur+"    [-h]           "+end+': '+pur+"Show Help Banner"+end
	print
	print green+"e.g.:"+end
	print
	print pur+"    ./igops.py "+tur+"-t "+green+"google.com"+end
	print pur+"    ./igops.py "+tur+"-h "+end
	print

def application():
	argv = sys.argv[1:]
	argvv = len(sys.argv)
	
	if argvv == 1:
		banner()
		sys.exit()
	elif argvv > 3:
		banner()
		print
		print red+"\t[-] Invalid Options"+end
		print
		sys.exit()
	else:
		pass
	
	try:
		opts, args = getopt.getopt(argv, '-t:-r-h')
	except getopt.GetoptError:
		banner()
		print
		print red+"\t[-] Invalid Options"+end
		print
		sys.exit()
	
	for opt,arg in opts:
		if opt == '-t':
			print
			print logo
			print
			scan(arg)
		elif opt == '-h':
			banner()
			sys.exit()
		else:
			banner()
			print
			print red+'\t[-] Invalid Options'+end
			print
			sys.exit()





if __name__ == '__main__':
	application()
else:
	pass


# -*- Copy Right For Sir Uidops :/ -*-





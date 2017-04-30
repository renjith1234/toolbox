#!/usr/bin/python
import urllib2
import sys

if len(sys.argv) < 2:
  print "[*] HONEYPOTS CHECKER"
  print "[*] Usage : "+((sys.argv[0]).split)(".")[1]+" <ip addr>"
  sys.exit()

print "[*] HONEYPOTS CHECKER"
print "[*] Get wordlist from http://pastebin.com/raw/dgt5fk69" 
content = urllib2.urlopen("http://pastebin.com/raw/dgt5fk69").read()

ips = content.split();
for x in ips:
  if sys.argv[1] == x:
    print "[+] Its an honypot dude"
    sys.exit()
  
print "[*] Your safe"


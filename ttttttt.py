#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import urllib2
response = urllib2.urlopen('http://www.thaiseoboard.com/index.php?action=register')
html = response.read()
hacktoberfest = "woweooe"
# print(html[html.find("3ex;"):html.find("3ex;")+30])
# print(html)
p=html.find("ขออภัย")
# print(html[p:p+10])
print(p)

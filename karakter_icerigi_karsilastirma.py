#!/usr/bin/env python3

dizi1  = "canankocaman"
dizi2  = "cnnkcmn"

dosya = open("dosya.txt","w")

for c in dizi1:
	if not c in dizi2:
		dosya.write(c)
		dosya.write("\n")

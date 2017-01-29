import os
import sys

print("""
					+----------------------------+
					|        lstudio v1.0        |
					+----------------------------+

	\033[1;32m [+] Author: Labreche Abdelatif \033[1;m
 	\033[1;32m [+] lstudio: Helps you to install all linux supported multimedia programs \033[1;m

 +---------------------+---------------+-----------------+-------------+--------------+--------------+
 |        Audio        |      Video    |       Image     |      3D     | Engineering  |   Animation  |
 +---------------------+---------------+-----------------+-------------+--------------+--------------+
 | 1) vlc Media Player | 3) Lightworks | 5) Gimp         | 8) Blender  | 10) Openscad | 11) Natron   |
 | 2) Audacity         | 4) Openshot   | 6) Raw Therapee | 9) Openscad |              |              |
 |                     |               | 7) Inkscape     |             |              |              |
 +---------------------+---------------+-----------------+-------------+--------------+--------------+
 0) Exit
""")
while True:
	cmd = input("\033[1;34mlstudio > \033[1;m")

	if(cmd == 1):
		os.system("sudo apt-get install vlc")
	elif(cmd == 2):
		os.system("sudo apt-get install audacity")
	elif(cmd == 3):
		os.system("sudo apt-get install gdebi")
 		os.system("wget ftp.us.debian.org/debian/pool/main/t/tiff3/libtiff4_3.9.6-11_amd64.deb")
 		os.system("wget http://www.lwks.com/dmpub/lwks-12.0-amd64.deb")
 		os.system("sudo gdebi libtiff4_3.9.6-11_amd64.deb")
  		os.system("sudo gdebi lwks-12.0-amd64.deb")
  	elif(cmd == 4):
  		os.system("sudo apt-get install openshot")
  	elif(cmd == 5):
  		os.system("sudo apt-get install gimp")
  	elif(cmd == 6):
  		os.system("sudo apt-get install rawtherapee")
  	elif(cmd == 7):
  		os.system("sudo apt-get install inkscape")
  	elif(cmd == 8):
  		os.system("sudo apt-get install blender")
  	elif(cmd == 9):
  		os.system("sudo apt-get install openscad")
  	elif(cmd == 10):
  		os.system("sudo apt-get install openscad")
  	elif(cmd == 11):
  		os.system("sudo apt-get install gdebi")
  		os.system("sudo apt-get install libegl1-mesa")
  		os.system("wget http://packages.deepin.com/deepin/pool/main/n/natron/natron_2.0.1_i386.deb")
  		os.system("sudo gdebi natron_2.0.1_i386.deb")
  	elif(cmd == 0):
  		sys.exit()





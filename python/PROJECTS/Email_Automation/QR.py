'''

import random
player1 = input("Enter any one of the below: Rock,Paper,Scissors").lower()
'''

#you should include above game in VirtualAssistant either as a module or function --> it should play game
#QRCode Creation -->pip install PyQRCode

import pyqrcode
import png

link = "www.linkedin.com/in/ramana-komati-4292332b7"
#now we create QRCode for above link
qr = pyqrcode.create(link)
#print(qr)
#pip install pypng
qr.png("myqr.png",scale = 10)

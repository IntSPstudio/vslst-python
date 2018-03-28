#|==============================================================|#
# Made by IntSPstudio
# Project Visual Street
#
# Twitter: @IntSPstudio
#|==============================================================|#

#IMPORT
import random
#SETTINGS
treeContent ="@"
treeFrame ="#"
backgroundContent ="+"
treeDecorations ="%"
treeWidth =20
def addLine(width,optio,content):
	a = int(treeWidth - width /2)
	b = ""
	point =""
	for i in range(0, a):
		b = b + backgroundContent
	for i in range(0, width):
		c = random.randrange(0, 5)
		if content == 1:
			d = treeContent
		elif content == 2:
			d = treeFrame
		else:
			d = treeContent
		if optio == 1:
			if c == 0:
				point = point + treeDecorations
			else:
				point = point + d
		else:
			point = point + d
	point = b + point + b
	return point
if __name__ == "__main__":
	ip = 0
	for i in range(0, 15):
		print(addLine(ip,1,1))
		ip +=2
	for i in range(0,4):
		print(addLine(6,0,2))
	print(addLine(0,0,0))
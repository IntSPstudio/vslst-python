#|==============================================================|#
# Made by IntSPstudio
# Project Visual Street
#
# Twitter: @IntSPstudio
#|==============================================================|#

#SETTINGS
fileName ="sample"
fileSeparator =";"
#READ FILE
def readFile(name):
	file = name +".csv"
	file = open(file, "r")
	fileContent = file.read().splitlines()
	file.close()
	return fileContent
#ARRAY HEIGHT
def getArrayWidth(array):
	arrayMaxWidth =0
	arrayHeight = len(array)
	for yp in range(0, arrayHeight):
		arrayWidth = len(content[yp])
		pointWidth =0
		pointCheck =0
		for xp in range(0, arrayWidth):
			point = str(content[yp][xp])
			
			if point == fileSeparator:
				pointCheck =0
			else:
				if pointCheck == 0:
					pointWidth +=1
					pointCheck =1
		if pointWidth > arrayMaxWidth:
			arrayMaxWidth = pointWidth
	return arrayMaxWidth
#START
if __name__ == "__main__":
	#CONTENT
	content = readFile(fileName)
	contentHeight = len(content)
	#LIMITS
	arrayHeight = len(content)
	arrayWidth = getArrayWidth(content)
	#LIST COMPREHENSION
	arrayContent = [["" for xp in range(arrayWidth)] for yp in range(1)]
	#ADDING CONTENT TO LIST
	arrayYP =0
	for yp in range(0, contentHeight):
		contentWidth = len(content[yp])
		contentCheck =0
		wcl =""
		arrayXP =-1
		for xp in range(0, contentWidth):
			point = str(content[yp][xp])
			if point == fileSeparator:
				wcl =""
				contentCheck =0
			else:
				if contentCheck == 0:
					arrayXP +=1
					contentCheck =1
				wcl = wcl + point
				arrayYP = yp
				print(wcl)
				#arrayContent[arrayYP][arrayXP] = wcl
	print(arrayContent)
	print(content)
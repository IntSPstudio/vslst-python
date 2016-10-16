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
		arrayWidth = len(array[yp])
		pointWidth =0
		pointCheck =0
		for xp in range(0, arrayWidth):
			point = str(array[yp][xp])
			
			if point == fileSeparator:
				pointCheck =0
			else:
				if pointCheck == 0:
					pointWidth +=1
					pointCheck =1
		if pointWidth > arrayMaxWidth:
			arrayMaxWidth = pointWidth
	return arrayMaxWidth
#MAKE ARRAY
def makeContentArray():
	#CONTENT
	contentFile = readFile(fileName)
	contentHeight = len(contentFile)
	#LIMITS
	arrayHeight = len(contentFile)
	arrayWidth = getArrayWidth(contentFile)
	#LIST COMPREHENSION
	arrayContent = [["" for xp in range(arrayWidth)] for yp in range(arrayHeight)]
	#ADDING CONTENT TO LIST
	arrayYP =0
	for yp in range(0, contentHeight):
		contentWidth = len(contentFile[yp])
		contentCheck =0
		wcl =""
		arrayXP =-1
		for xp in range(0, contentWidth):
			point = str(contentFile[yp][xp])
			if point == fileSeparator:
				wcl =""
				contentCheck =0
			else:
				if contentCheck == 0:
					arrayXP +=1
					contentCheck =1
				wcl = wcl + point
				arrayYP = yp
				#print(wcl)
				arrayContent[arrayYP][arrayXP] = wcl
	return arrayContent
#START
if __name__ == "__main__":
	#CSV TO 2D ARRAY
	arrayContent = makeContentArray()
	print(arrayContent)

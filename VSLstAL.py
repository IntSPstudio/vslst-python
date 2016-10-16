#|==============================================================|#
# Made by IntSPstudio
# Project Visual Street
#
# Twitter: @IntSPstudio
#|==============================================================|#
#SETTINGS
fileNameIn ="sample"
fileNameOut ="result"
fileSeparator =";"
#READ FILE
def readFile(name):
	file = name +".csv"
	file = open(file, "r")
	fileContent = file.read().splitlines()
	file.close()
	return fileContent
#WRITE FILE
def writeFile(array):
	arrayMaxWidth =0
	arrayHeight = len(array)
	arrayLine =""
	fileName = fileNameOut +".csv"
	f = open(fileName,"w")
	for yp in range(0, arrayHeight):
		arrayWidth = len(array[yp])
		for xp in range(0, arrayWidth):
			point = str(array[yp][xp])
			if arrayLine !="":
				arrayLine = arrayLine + fileSeparator + point
			else:
				arrayLine = point
		if yp < arrayHeight -1:
			arrayLine = arrayLine +"\n"
		f.write(arrayLine)
		arrayLine =""
	f.close()
#ARRAY HEIGHT (CSV STYLE)
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
def makeContentArray(contentFileName):
	#CONTENT
	contentFile = readFile(contentFileName)
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
def printContentArraySimple(array):
	arrayMaxWidth =0
	arrayHeight = len(array)
	arrayPrintMap =""
	arraySeparatorV ="\n"
	arraySeparatorH =" "
	for yp in range(0, arrayHeight):
		arrayWidth = len(array[yp])
		for xp in range(0, arrayWidth):
			point = str(array[yp][xp])
			if point !="":
				if xp == 0:
					arrayPrintMap = arrayPrintMap + point
				else:
					arrayPrintMap = arrayPrintMap + arraySeparatorH + point
		if yp < arrayHeight -1:
			arrayPrintMap = arrayPrintMap + arraySeparatorV
	return arrayPrintMap
#START
if __name__ == "__main__":
	#CSV TO 2D ARRAY
	fileContent = makeContentArray(fileNameIn)
	fileHeight = len(fileContent)
	fileWidth = arrayWidth = len(fileContent[0])
	print(fileHeight, "x", fileWidth)
	print(printContentArraySimple(fileContent))

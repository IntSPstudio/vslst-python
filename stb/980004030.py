#|==============================================================|#
# Made by IntSPstudio
# Project Visual Street
# ID: 980004030
# Twitter: @IntSPstudio
#|==============================================================|#

#IMPORT
import it8c
#MAIN
if __name__ == "__main__":
	fileNameI ="collectionlist.csv"
	#CHECK FILE
	if it8c.fileTextExists(fileNameI) == 1:
		#READ FILE
		rawFileContent = it8c.csvReadFile(fileNameI,";")
		rawFileContentHeight = len(rawFileContent)
		rawFileContentWidth = len(rawFileContent[0])
		#EXTRACT COLUMNS
		for i in range(0,rawFileContentWidth):
			cacheLine = it8c.dataExtractArrayColumn(rawFileContent,i)
			#TITLE
			pointa = cacheLine[0]
			#FILE NAME
			pointb = pointa +"_summary.csv"
			#GET CONTENT NOT TITLE
			columnContent = it8c.dataCreateList(rawFileContentHeight -1,"-") 
			for i in range(1, rawFileContentHeight):
				j = i -1
				columnContent[j] = cacheLine[i]
			#SUMMARY
			pointc = it8c.dataCheckListObjects(columnContent)
			#SAVE SUMMARY
			it8c.csvWriteFile(pointc,pointb,";",0) 
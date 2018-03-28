#|==============================================================|#
# Made by IntSPstudio
# Project Visual Street
#
# Twitter: @IntSPstudio
#|==============================================================|#
#IMPORT IT8c
import it8c
#MAIN
if __name__ == "__main__":
	fileName = "sample.csv"
	if (it8c.fileTextExists(fileName) == 1):
		fileContent = it8c.csvReadFile(fileName,";")
		print(it8c.csvArraySize(fileContent))
		print(it8c.csvSimplePrint(fileContent))
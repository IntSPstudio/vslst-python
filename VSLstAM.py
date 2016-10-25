#|==============================================================|#
# Made by IntSPstudio
# Project Visual Street
#
# Twitter: @IntSPstudio
#|==============================================================|#
#IMPORT IT8c library
import it8c
#MAIN
if __name__ == "__main__":
	fileContent = it8c.csvReadFile("sample.csv")
	print(it8c.csvArraySize(fileContent))
	print(it8c.csvSimplePrint(fileContent))
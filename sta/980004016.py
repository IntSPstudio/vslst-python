#|==============================================================|#
# Made by IntSPstudio
# Project Visual Street
# ID: 980004016
# Twitter: @IntSPstudio
#|==============================================================|#

#IMPORT
import it8c
import platform
#MAIN
if __name__ == "__main__":
	#ARRAY
	platformContent = it8c.dataCreateArray(10,2,"")
	#IMPORT DATA
	platformContent[0][0] ="COMPUTER"
	platformContent[1][0] ="Name"
	platformContent[1][1] = platform.node()
	platformContent[2][0] ="Information"
	platformContent[2][1] = platform.platform()
	platformContent[3][0] ="Operating system"
	platformContent[3][1] = platform.system()
	platformContent[4][0] ="CPU architecture"
	platformContent[4][1] = platform.machine()
	platformContent[5][0] ="CPU information"
	platformContent[5][1] = platform.processor()
	platformContent[6][0] ="PYTHON"
	platformContent[7][0] ="Version"
	platformContent[7][1] = platform.python_version()
	platformContent[8][0] ="Build number"
	platformContent[8][1] = platform.python_build()[0]
	platformContent[9][0] ="Build date"
	platformContent[9][1] = platform.python_build()[1]
	#PRINT ARRAY CONTENT
	print(it8c.vslTerminalLine(0,""))
	print(it8c.dataSmrPrintArray(platformContent," ","",0))
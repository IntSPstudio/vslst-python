#|==============================================================|#
# Made by IntSPstudio
# Project Visual Street
#
# Twitter: @IntSPstudio
#|==============================================================|#

#IMPORT
import it8c
#AVARAGE CALCULATOR
def calculateAvarage(listContent):
	listLength = len(listContent)
	listNumberAvg =0
	if listLength > 0:
		for i in range(0, listLength):
			pointa = listContent[i]
			checka = it8c.checkIfItIsNumber(userRawInput)
			if checka == 1:
				listNumberAvg += int(pointa)
		return listNumberAvg / listLength
	return 0
#MAIN
if __name__ == "__main__":
	continuity =1
	userNumberList =[]
	userNumberAvarage =0
	while continuity == 1:
		userRawInput = input("Add number: ")
		if userRawInput !="exit":
			checka = it8c.checkIfItIsNumber(userRawInput)
			if checka == 1:
				userNumInput = int(userRawInput)
				userNumberList.extend([userNumInput])
				userNumberAvarage = calculateAvarage(userNumberList)
		else:
			continuity =0
		print("Avarage: "+ str(userNumberAvarage))
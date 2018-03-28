#|==============================================================|#
# Made by IntSPstudio
# Project Visual Street
#
# Twitter: @IntSPstudio
#|==============================================================|#

#POSSIBLE CHARACTERS
poscha = [1,2,3,4,5]
#LENGTH
poschaLength = len(poscha)

for a in range(0, poschaLength):
	for b in range(0, poschaLength):
		for c in range(0, poschaLength):
			output = str(poscha[a]) + str(poscha[b]) + str(poscha[c])
			print(output)
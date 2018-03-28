#|==============================================================|#
# Made by IntSPstudio
# Project Visual Street
#
# Twitter: @IntSPstudio
#|==============================================================|#

#IMPORT
import datetime
#MAIN
if __name__ == "__main__":
	clDateA = datetime.datetime.now()
	clYear = clDateA.year
	clMonth = clDateA.month
	clDay = clDateA.day
	clHour = clDateA.hour
	clMinute = clDateA.minute
	clSecond = clDateA.second
	clDateB = "{:04d}-{:02d}.{:02} {:02}:{:02}:{:02}".format(clYear,clMonth,clDay,clHour,clMinute,clSecond)
	print(clDateB)
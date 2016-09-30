#|==============================================================|#
# Made by IntSPstudio
# Project Visual Street
#
# Twitter: @IntSPstudio
#|==============================================================|#

#IMPORT
import sys
import hashlib
#USER INPUT
input = sys.argv[1]
#START
if __name__ == "__main__":
	hasht = hashlib.sha1()
	hasht.update(input.encode('utf-8'))
	output = hasht.hexdigest()
	print(output)

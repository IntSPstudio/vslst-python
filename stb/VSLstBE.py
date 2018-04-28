#|==============================================================|#
# Made by IntSPstudio
# Project Visual Street
#
# Twitter: @IntSPstudio
#|==============================================================|#

#LIBRARIES
from tkinter import Tk, Frame, LEFT, BOTH
#SETTINGS
#MAIN
root = Tk()
rootWidth =854 #X
rootHeight =480 #Y
rootSize = str(rootWidth) +"x"+ str(rootHeight)
root.geometry(rootSize)
root.title("VSLstBE")
#FRAMES
frame1Width = int(rootWidth /3)
frame1Height = rootHeight
frame1Color = "#181818"
frame2Width = rootWidth - frame1Width
frame2Height = rootHeight
frame2Color = "#202020"
#START
if __name__ == "__main__":
  f1 = Frame(root, width = frame1Width, height = frame1Height, bg = frame1Color, relief="flat")
  f1.pack(fill=BOTH, expand=0, side=LEFT)
  f2 = Frame(root, width = frame2Width, height = frame2Height, bg = frame2Color, relief="flat")
  f2.pack(fill=BOTH, expand=1, side=LEFT)
  root.mainloop()
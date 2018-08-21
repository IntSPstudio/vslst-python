#|==============================================================|#
# Made by IntSPstudio
# Project Visual Street
#
# Twitter: @IntSPstudio
#|==============================================================|#

#LIBRARIES
import urllib.request, json 
#SETTINGS
findKeyA = "data-original" #KEY
findKeyB = '"{' #START
findKeyC = '}"' #STOP
findKeyD = ":"
findKeyE = ","
#LOOP
if __name__ == "__main__":
    #GIVE LICENSE
    ap = "https://www.biltema.fi/auton-varaosahaku/" #URL (Change by country)
    userLp = input("License plate: ") #ABC-123
    if userLp !="":
        cp = ap + userLp #URL
        #GET
        with urllib.request.urlopen(cp) as url:
            cacheContent = url.read().decode()
            cacheContent = cacheContent.replace(" ", "")
            cacheContent = cacheContent.replace("&quot;","")
            #CHECK POINTS
            ap = cacheContent.find(findKeyA)
            bp = cacheContent.find(findKeyB,ap) +2
            cp = cacheContent.find(findKeyC,bp)
            #LOOP
            if ap > 0:
                if bp > 0:
                    if cp > 0:
                        #TA
                        arrayContent ={}
                        mode =1
                        dp =""
                        fp =""
                        gp =""
                        #TB
                        for i in range(bp,cp):
                            ep = cacheContent[i]
                            #TC
                            if ep == findKeyD:
                                fp = dp
                                dp =""
                            elif ep == findKeyE:
                                gp = dp
                                dp =""
                                #RULE CHECK
                                fp = str("").join(i for i in fp if i.isalnum())
                                gp = str("").join(i for i in gp if i.isalnum())
                                #OPTIONS
                                if gp == "true":
                                    arrayContent[fp] = True
                                elif gp == "null":
                                    arrayContent[fp] = None
                                elif gp == "":
                                    arrayContent[fp] = None
                                else:
                                    arrayContent[fp] = gp
                            else:
                                dp = dp + str(ep)
                        #SAVE RESULTS (PRINT OR SAVE)
                        print(json.dumps(arrayContent, indent=2, sort_keys=True))
                        """
                        aUrl = str("").join(i for i in userLp if i.isalnum()) +"_results.json"
                        aFile = open(aUrl, "w")
                        json.dump(arrayContent, aFile)
                        aFile.close()
                        """
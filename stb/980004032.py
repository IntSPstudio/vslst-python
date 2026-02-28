#|==============================================================|#
# Made by IntSPstudio
# Project Visual Street
# ID: 980004032
#|==============================================================|#
#LIBRARIES
import urllib.request, json
#LOOP
if __name__ == "__main__":
    #GIVE LICENSE
    url_start = "https://www.biltema.fi/auton-varaosahaku/" #URL (Change by country)
    user_input = input("License plate: ") #ABC-123
    result_title = str(user_input)
    if user_input !="":
        url_get = url_start + user_input #URL
        result =""
        #TRY TO GET THE DATA
        try:
            with urllib.request.urlopen(url_get) as url:
                user_content = url.read().decode()
                #CHECK POINTS
                url_start_point = user_content.find("extraVehicleInformation")
                url_end_point =0
                #END POINT CHECK
                for i in range(url_start_point +3,len(user_content)):
                    url_test_point = user_content[i-2] + user_content[i-1] + user_content[i]
                    if url_test_point == "}},":
                        url_end_point =i
                #READ CONTENT
                for i in range(url_start_point, url_end_point):
                    result = result + user_content[i]
                #CLEANING TEXT
                result = result.replace('extraVehicleInformation":','')
                result_dict = json.loads(result)
                #PRINING TO SCREEN
                pretty_json = json.dumps(result_dict, indent=4, ensure_ascii=False)
                print(pretty_json)
                #SAVE IT TO FILE
                file_name = result_title +".json"
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write(json.dumps(result_dict, ensure_ascii=False, indent=2))
        except:
            print("An exception occurred")
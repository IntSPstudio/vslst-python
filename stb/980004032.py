#|==============================================================|#
# Made by IntSPstudio
# Project Visual Street
# ID: 980004032
#|==============================================================|#

#LIBRARIES
import urllib.request, json, re
#SETTINGS
url_key_segment = "extraVehicleInformation" #KEY
url_key_blocka ="["
url_key_blockb ="]"
url_start_bracket_point =0
url_end_bracket_point =1
#LOOP
if __name__ == "__main__":
    #GIVE LICENSE
    url_start = "https://www.biltema.fi/auton-varaosahaku/" #URL (Change by country)
    user_input = input("License plate: ") #ABC-123
    if user_input !="":
        url_get = url_start + user_input #URL
        result =""
        #GET
        with urllib.request.urlopen(url_get) as url:
            user_content = url.read().decode()
            #CHECK POINTS
            url_start_point = user_content.find(url_key_segment)
            #GET
            print(url_start_point)
            for i in range(url_start_point,len(user_content)):
                url_test_point = user_content[i]
                if url_end_bracket_point == 1:
                    if url_test_point == url_key_blocka:
                         url_start_bracket_point =1
                    if url_test_point == url_key_blockb:   
                        url_end_bracket_point =0
                    if url_start_bracket_point == 1:
                        result = result + user_content[i]
            #PARSING
            pairs = re.findall(r'"title":"(.*?)","value":"(.*?)"', result)
            result_dict = {title: value for title, value in pairs}
            result_title = user_input
            #PRINT
            for i in result_dict:
                print (i, "=", result_dict[i])
            #SAVE
            file_name = result_title +".json"
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(json.dumps(result_dict, ensure_ascii=False, indent=2))
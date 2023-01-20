import requests
from get_header_data import   get_token
from get_new_token import get_new_token
import urllib3
urllib3.disable_warnings()

from settings import *

def get_event_id(query_string,email):
  
    get_event_url = "https://ticketingweb.passo.com.tr/api/passoweb/allevents"
    get_event_headers = {
    "Access-Control-Request-Headers":
	"authorization,content-type,currentculture","Accept":"Accept: application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Authorization": "Bearer " + get_token(email),"Connection": "close","Content-Type": "application/json;charset=utf-8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}

    get_event_json = {"CityId": None, "endDate": "", "from": 0, "genreId": None, "HastagId": None, "query": query_string, "size": 20, "startDate": "", "SubGenreIdList": []}
    event_response = requests.post(get_event_url, headers=get_event_headers, json=get_event_json, verify=False)
    if event_response.status_code == 200:
        event_data = event_response.json()
    
        event_valueList = event_data["valueList"]
        if len(event_valueList)>0:
                    
                        event_id = event_valueList[0]["id"]
                        seo_url=event_valueList[0]["seoUrl"]
                        return [event_id,seo_url]
        else:
            print("No available event!Try other events.")
            return  "no_event"          


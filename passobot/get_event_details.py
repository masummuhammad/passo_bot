import requests

import urllib3
urllib3.disable_warnings()


from settings import *

def get_event_details(event_id: str,seo_url) -> list:
    event_details_url = f"https://ticketingweb.passo.com.tr/api/passoweb/geteventdetails/{seo_url}/{event_id}/618"
    event_details_headers = {
    "Accept":"Accept: application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Connection": "close","Content-Type": "application/json;charset=utf-8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
    event_details_response = requests.get(event_details_url, headers=event_details_headers, verify=False)
    
    if event_details_response.status_code == 200:
        event_details = event_details_response.json()
        
        event_categories_details = event_details["value"]["categories"]
        event_validationIntegrations_details = event_details["value"]["validationIntegrations"]
        #for item in event_validationIntegrations_details:
            # print(item['parameter1DisplayName'])
        
        return [event_categories_details, event_validationIntegrations_details]



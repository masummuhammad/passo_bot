import requests
from get_header_data import  *
from get_new_token import get_new_token
import urllib3
from settings import *
urllib3.disable_warnings()


def priority_validation_rule(EventId, ValidationIntegrationID, param1,email,password):
    priority_validation_rule_url = "https://ticketingweb.passo.com.tr/api/passoweb/priorityvalidationrule"
    priority_validation_rule_headers = {
    "Access-Control-Request-Headers":
	"authorization,content-type,currentculture","Accept":"Accept: application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Authorization": "Bearer " + get_token(email),"Connection": "close","Content-Type": "application/json;charset=utf-8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
    priority_validation_rule_json = {"ValidationIntegrationID":int(ValidationIntegrationID),"EventId":int(EventId),"param1":str(param1)}
    priority_validation_rule_res = requests.post(priority_validation_rule_url, headers=priority_validation_rule_headers, json=priority_validation_rule_json, verify=False)
    
    if priority_validation_rule_res.status_code == 401:
        
        get_new_token(email,password)
        priority_validation_rule_headers = {
        "Access-Control-Request-Headers":
        "authorization,content-type,currentculture","Accept":"Accept: application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Authorization": "Bearer " + get_token(email),"Connection": "close","Content-Type": "application/json;charset=utf-8",
         "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
        priority_validation_rule_json={"ValidationIntegrationID":int(ValidationIntegrationID),"EventId":int(EventId),"param1":str(param1)  }
        priority_validation_rule_res = requests.post(priority_validation_rule_url, headers=priority_validation_rule_headers, json=priority_validation_rule_json, verify=False)
        
        if priority_validation_rule_res.status_code == 200:
            
            print(f"priority validation rule result: {priority_validation_rule_res.json()}")
            return
    if priority_validation_rule_res.status_code == 200:
        
        print(f"priority validation rule result: {priority_validation_rule_res.json()}")
        return



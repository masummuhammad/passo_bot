from get_header_data import get_refresh_token_id
import requests

import urllib3

urllib3.disable_warnings()
from initdb import connection


def get_new_token(email,password):
    get_new_token_url = "https://ticketingweb.passo.com.tr/api/passoweb/login"
    get_new_token_headers = {
    "Access-Control-Request-Headers":
	"authorization,content-type,currentculture","Accept":"Accept: application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Connection": "close","Content-Type": "application/json;charset=utf-8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
    data={"username":email,"password":password,"rememberMe":"true"}
    
    token_res = requests.post(get_new_token_url, headers=get_new_token_headers,json=data, verify=False)
    
    if token_res.status_code==200:
        token_res_data=token_res.json()
        
        refresh_token_id=token_res_data['value']['refresh_token']
        access_token=token_res_data['value']['access_token']
        try:
                cursor=connection.cursor()
                cursor.execute("update header_data set refresh_token ='%s' where email ='%s';"%(refresh_token_id,email))
                connection.commit()
                cursor.execute("update header_data set token = '%s'  where email = '%s';"%(access_token,email))
                connection.commit()
        except Exception as e:
            print(e)

        return access_token

def check_token_validity(email) -> str:
    
    
    refresh_token_url = "https://ticketingweb.passo.com.tr/api/passoweb/refreshtoken/%s" % get_refresh_token_id(email)
    refresh_token_headers={"Access-Control-Request-Headers":
	"authorization,content-type,currentculture","Accept":"Accept: application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Connection": "close","Content-Type": "application/json;charset=utf-8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
    refresh_token_res = requests.post(refresh_token_url, headers=refresh_token_headers, verify=False)
    
    if refresh_token_res.status_code == 200:
        return 'valid'
    if refresh_token_res.status_code == 401:
        return 'invalid'





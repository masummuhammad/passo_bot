import time

import requests
from requests import ConnectTimeout, HTTPError, ReadTimeout, Timeout

from get_header_data import   get_token
from get_new_token import get_new_token
from settings import sleep_before_getting_available_block_list
import urllib3
urllib3.disable_warnings()


def get_available_block_list(event_id, seat_category_id,email,password):
    loop = True
    token = get_token(email)
    n = 0
    while loop:
        available_block_list_url = "https://ticketingweb.passo.com.tr/api/passoweb/getavailableblocklist?seatCategoryId=%s&serieId=null&eventId=%s" % (seat_category_id, event_id)
       

        available_block_list_headers = {
        "Access-Control-Request-Headers":
	    "authorization,content-type,currentculture","Accept":"Accept: application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Authorization": "Bearer " + token,"Connection": "close","Content-Type": "application/json;charset=utf-8",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
        try:
            time.sleep(sleep_before_getting_available_block_list)
            available_block_list_res = requests.get(available_block_list_url, headers=available_block_list_headers, verify=False)
        except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError):
            continue
        if available_block_list_res.status_code == 401:
            get_new_token(email,password)
            # print(f"old token:{token}")
            token = get_token(email)
            # print(f"new token:{token}")
            continue

        try:
            available_block_list_data = available_block_list_res.json()
            valueList = available_block_list_data['valueList']
            
            if len(valueList) == 0:
                n += 1
                print(f"Retry no: {n}, block found: {available_block_list_data}")
                continue
            
            return valueList
        except Exception as e:
            print(e)


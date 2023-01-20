import json
import time

import requests
from get_header_data import get_token
from get_new_token import get_new_token
import urllib3
from requests import ConnectTimeout, HTTPError, ReadTimeout, Timeout


from get_user_basket_info import get_user_basket_booking
from settings import sleep_before_adding_best_ticket_to_basket,phone_number
urllib3.disable_warnings()




def add_best_seats_to_basket(block_name_, block_id, event_id, seat_category_id, seat_category_variant_id, max_number_of_ticket_in_basket_allowed, found_ticket_total_number,email,password):
    
    token = get_token(email)
    
    loop2=True
    
    try_count=0
    
    while loop2:
        try_count+=1
        if try_count==3:
            return 'try_next_block'
        add_best_seats_to_basket_url = "https://ticketingweb.passo.com.tr/api/passoweb/addbestseatstobasket"
        add_best_seats_to_basket_json = {"blockId":block_id,"seatCategoryTicketTypeId":100,"seatCategoryId":seat_category_id,"sidebyside":False,"discountIntegrationId":None,"variantCount":[{"seatCategoryVariantId":seat_category_variant_id,"count":1}],"eventId":event_id}

        add_best_seats_to_basket_headers = {
        "Access-Control-Request-Headers":
        "authorization,content-type,currentculture","Accept":"Accept: application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Authorization": "Bearer " + token,"Connection": "close","Content-Type": "application/json;charset=utf-8",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}

        try:
            time.sleep(sleep_before_adding_best_ticket_to_basket)
            print(f"Trying block: {block_name_}")
               
            res_sub_category = requests.post(add_best_seats_to_basket_url, headers=add_best_seats_to_basket_headers, json=add_best_seats_to_basket_json, verify=False, timeout=2.0)
        except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError):
            continue
        
        if res_sub_category.status_code==401:
            token=get_new_token(email,password)
            continue
        data=res_sub_category.json()
        
        if data['isError']:
            
            if try_count >= 2:
                return 'try_next_block'
            else:
                continue
        elif data['resultCode']==5275:
            return 'max_ticket_in_basket'

        result = data['valueList']

        basket_id = result[0]['basket']['basketId']
        if basket_id:
            user_basket_info_ = get_user_basket_booking(email)
            if user_basket_info_=='empty_basket':
                print("Basktet is empty!")
                continue
            
            found_ticket_total_number = len(user_basket_info_)
            print(f"Ticket found total: {found_ticket_total_number}")
            webhook = "https://hooks.slack.com/services/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"
            ticket_info_for_slack: str = ""
            for item in user_basket_info_:
                for item_ in item:
                    item_ = f"{item_}: {item[item_]}\n"
                    ticket_info_for_slack += item_
                ticket_info_for_slack = ticket_info_for_slack + "\n\n"
            payload = {"text": f"Hi, {len(user_basket_info_)} new ticket has been added to basket. \nemail: {email}\npassword: {password}\nphone number: {phone_number}\n\n{ticket_info_for_slack}"}
            print(f"Hi, {len(user_basket_info_)} new ticket has been added to basket.\nemail: {email}\npassword: {password}\nphone number: {phone_number}\n\n{ticket_info_for_slack}")
            requests.post(webhook, json.dumps(payload), verify=False)

            if max_number_of_ticket_in_basket_allowed <= found_ticket_total_number: 
                return found_ticket_total_number
            else:
                continue

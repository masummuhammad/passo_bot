import requests
from get_header_data import *
from get_new_token import get_new_token
import urllib3
urllib3.disable_warnings()


def get_user_basket_booking(email):
    user_info_list = []
    user_basket_booking_url = "https://ticketingweb.passo.com.tr/api/passoweb/getuserbasketbooking"
    if_modified_since = "Mon, 17 Oct 2022 21:45:34 GMT"
    user_basket_booking_headers = {
    "Access-Control-Request-Headers":
    "authorization,content-type,currentculture","Accept":"Accept: application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Authorization": "Bearer " + get_token(email),"Connection": "close","Content-Type": "application/json;charset=utf-8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
    
    user_basket_booking_res = requests.get(user_basket_booking_url, headers=user_basket_booking_headers, verify=False)
    
    if user_basket_booking_res.status_code == 200:
        user_basket_booking_data = user_basket_booking_res.json()
        
        user_basket_booking_data = user_basket_booking_data['value']["basketBookingProducts"]
        if not user_basket_booking_data:
            print("There is no ticket in the basket")
            return "empty_basket"
        for item in user_basket_booking_data:
            user_info = {
                "rowId": item["rowId"],
                "Category_Name": item["seatCategory_Name"],
                "block_Name": item["block_Name"],
                "tribune_Name": item["tribune_Name"],
                "RowName": item["refSeatInfo_RowName"],
                "SeatName": item["refSeatInfo_SeatName"],
                "Date": item["startDate"],
            }
            user_info_list.append(user_info)
        return user_info_list

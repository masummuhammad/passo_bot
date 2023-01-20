import requests
from get_header_data import get_token
import urllib3

urllib3.disable_warnings()

def clear_basket(email):
    burp0_url = "https://ticketingweb.passo.com.tr/api/passoweb/removeallseatfrombookingbasket"
    burp0_headers = {
    "Access-Control-Request-Headers":
    "authorization,content-type,currentculture","Accept":"Accept: application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Authorization": "Bearer " + get_token(email),"Connection": "close","Content-Type": "application/json;charset=utf-8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}

    remove_all_seat_from_booking_basket = requests.post(burp0_url, headers=burp0_headers, verify=False)
    
    

    # print(remove_all_seat_from_booking_basket.json())
           
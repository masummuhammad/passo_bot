import requests
from get_header_data import    get_token
from get_new_token import get_new_token, check_token_validity
import urllib3
urllib3.disable_warnings()


def get_variants(event_id, seatcategoryid,email):
    get_variants_url = f"https://ticketingweb.passo.com.tr/api/passoweb/getvariants?eventId={event_id}&serieId=&tickettype=101&campaignId=null&validationintegrationid=null&seatcategoryid={seatcategoryid}"
    get_variants_headers = {
    "Access-Control-Request-Headers":
	"authorization,content-type,currentculture","Accept":"Accept: application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Authorization": "Bearer " + get_token(email),"Connection": "close","Content-Type": "application/json;charset=utf-8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
    get_variants_res = requests.get(get_variants_url, headers=get_variants_headers, verify=False)
    if get_variants_res.status_code == 200:
        get_variants_data = get_variants_res.json()
        variants_id=get_variants_data["value"]["variants"][0]["id"]
        return variants_id


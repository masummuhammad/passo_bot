import pymysql
import requests
import urllib3

from get_new_token import get_new_token

urllib3.disable_warnings()
token = ""
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='as598249',
                             database='passo_ticket',
                             charset='utf8mb4',
                             autocommit=True,
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    try:
        sql = "SELECT `token` FROM `token`;"
        cursor.execute(sql)
        token = cursor.fetchone()
    except Exception as e:
        print(e)


loop = True
index = 0

while loop:
    index += 1
    # category13 = "5007437"
    category = "5007438"
    event_id = "3972331"
    category_url = "https://ticketingweb.passo.com.tr/api/passoweb/getavailableblocklist?seatCategoryId=%s&serieId=null&eventId=%s" % (category, event_id)
    category_headers = {
    "Access-Control-Request-Headers":
    "authorization,content-type,currentculture","Accept":"Accept: application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Authorization": "Bearer " + token,"Connection": "close","Content-Type": "application/json;charset=utf-8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
    category_res = requests.get(category_url, headers=category_headers)
    if category_res.status_code == 401:
        token = get_new_token()
    data = category_res.json()

    print(f"{index} : {data}")
    try:
        valueList = data['valueList']
        # print(len(valueList))
        if len(valueList) == 0:
            continue
        value = valueList[len(valueList)-1]
        totalCount = value['totalCount']
        categoriesCount = value['categoriesCount']
        id_ = value['id']
        name = value['name']
        # id_ = "60338"

        sub_category_url = "https://ticketingweb.passo.com.tr/api/passoweb/addbestseatstobasket"
        sub_category_headers = {
        "Access-Control-Request-Headers":
        "authorization,content-type,currentculture","Accept":"Accept: application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Authorization": "Bearer " + token,"Connection": "close","Content-Type": "application/json;charset=utf-8",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
        sub_category_json = {"BlockId": id_, "EventId": even_id, "SeatCategoryId": category, "SeatCategoryTicketTypeId": 100, "SideBySide": True, "variantCount": [{"count": 1, "SeatCategoryVariantId": 2599240}]}

        loop2 = True
        m = 0
        while loop2:
            m += 1
            print(f"Try number: {m}")
            res_sub_category = requests.post(sub_category_url, headers=sub_category_headers, json=sub_category_json)
            data = res_sub_category.json()
            result = data['valueList']
            basket_id = result[0]['basket']['basketId']
            if basket_id:
                print(f"Ticket found: {basket_id}")
                loop = False
                break

    except IndexError:
        pass
    except KeyError:
        pass
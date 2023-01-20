import asyncio
import time
from get_header_data import  get_token
from installment import get_installment

import requests
from bs4 import BeautifulSoup
from threading import Timer
from make_payments import make_payment
from time_out_wait import main__, main__2
from get_new_token import get_new_token, check_token_validity


def tanimla(row_ids, event_id,email,password,name,cardnumber,cardexpiredatemonth,cardexpiredateyear,cardcvv2):
    token = get_token(email)
    cookies = {
        'BIGipServerVip_Prod_IksirSanalPos_https.app~Vip_Prod_IksirSanalPos_https_pool': '',
        'TS01a1807a': '',
        'TS01885cf1': '',
        'cookie': '',
        'aspNetCore_antiforgery': '',
        'rxVisitor': '',
        'dtLatC': '',
        'dtPC': '',
        'dtSa': '',
        'dtCookie': '',
        'rxvt': '',
        'TS01be67d8': '',
        'TS01859013': '016c47325c4a1117d02dffde3eaed031405b81893b2aa6a87e927d4ddb819761cd34e96629c986b6b58098c0a8ab3dbef47489a32c',
        'TS22476f14027': '08c779538dab2000339bedba8b1cbfd2ee55f41fbd8efd679b9ad5271b4273544789acbd6a73e948083af747f2113000ab99d84b4351f0fb860b54bad18e8d65abfcbd5bf70d8b7c8d55d48bfb1f53802948e3f52496381b06059a1b34b50327'
    }
    #######################################
    burp0_url = "https://iksirext.nkolayislem.com.tr:443/favicon.ico"
    burp0_cookies = {"cookie": "", "TS01be67d8": "0168200b61fb691d63f2b90054db3a70b8b6453d6a030e8409530ade2e7d9f3502c39ce6c41fda431c4425ea2fd8c34eae90386b83"}
    burp0_headers = {"User-Agent": "Passo;Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F) CTV", "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8", "X-Requested-With": "com.aktifbank.passo",
                     "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "no-cors", "Sec-Fetch-Dest": "image", "Referer": "https://iksirext.nkolayislem.com.tr/VPosApi/Pf/Ok/PfVpos/7AFD1367-5320-4DFB-ADFA-1268BD4BD1DF/SALES",
                     "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
    favicon = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies, verify=False)
    favicon_cookie = favicon.cookies.get_dict()
    for key in favicon_cookie:
        cookies[key] = favicon_cookie[key]
    #########################################

    assign_contact_to_seat_web_headers = {
        "Access-Control-Request-Headers":
        "authorization,content-type,currentculture","Accept":"Accept: application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Authorization": "Bearer " + token,"Connection": "close","Content-Type": "application/json;charset=utf-8",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}

    n = 0
    CountryCode = ''
    NationalID = ''
    for row in row_ids:
        n += 1
        if n == 1:
            # CountryCode = CountryCode1
            CountryCode = input(f"Enter Country Code for ticket no:{n}>>")
            NationalID = input(f"Enter National Id or Passport number for ticket no:{n}>>")
        elif n == 2:
            CountryCode = input(f"Enter Country Code for ticket no:{n}>>")
            NationalID = input(f"Enter National Id or Passport number for ticket no:{n}>>")
        elif n == 3:
            CountryCode = input(f"Enter Country Code for ticket no:{n}>>")
            NationalID = input(f"Enter National Id or Passport number for ticket no:{n}>>")
        elif n == 4:
            CountryCode = input(f"Enter Country Code for ticket no:{n}>>")
            NationalID = input(f"Enter National Id or Passport number for ticket no:{n}>>")
        elif n == 5:
            CountryCode = input(f"Enter Country Code for ticket no:{n}>>")
            NationalID = input(f"Enter National Id or Passport number for ticket no:{n}>>")
        assign_contact_to_seat_web_json_data = {
            'CountryCode': CountryCode,
            'NationalID': NationalID,
            'RowId': row,
            'FirstName': '',
            'LastName': '',
            'HesCode': '',
        }

        assign_contact_to_seat_web = requests.post('https://ticketingweb.passo.com.tr/api/passoweb/assigncontacttoseatweb', headers=assign_contact_to_seat_web_headers, json=assign_contact_to_seat_web_json_data, verify=False)
        if assign_contact_to_seat_web.status_code == 401:
            get_new_token(email,password)
            token = get_token(email)
            assign_contact_to_seat_web_headers = {
            "Access-Control-Request-Headers":
            "authorization,content-type,currentculture","Accept":"Accept: application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Authorization": "Bearer " + token,"Connection": "close","Content-Type": "application/json;charset=utf-8",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
            assign_contact_to_seat_web = requests.post('https://ticketingweb.passo.com.tr/api/passoweb/assigncontacttoseatweb', headers=assign_contact_to_seat_web_headers, json=assign_contact_to_seat_web_json_data, verify=False)





        assign_contact_to_seat_web_data = assign_contact_to_seat_web.json()
       
        try:
            id_ = assign_contact_to_seat_web_data['value']['id']
            print(f"*******Defining successful for id: {id_} *********")
        except KeyError:
            print("Defining failed!!!!!!!")
            return 'error'

        assign_contact_to_seat_web_cookie = assign_contact_to_seat_web.cookies.get_dict()
        for key in assign_contact_to_seat_web_cookie:
            cookies[key] = assign_contact_to_seat_web_cookie[key]
#now    ##################################################################
    before_pay_n_kolay_virtual_pos_headers = {
        "Access-Control-Request-Headers":
        "authorization,content-type,currentculture","Accept":"Accept: application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Authorization": "Bearer " + token,"Connection": "close","Content-Type": "application/json;charset=utf-8",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}


    json_data = {
    "cardInfo":None,"installment":None,
    'serieId': event_id,
    }

    before_pay_n_kolay_virtual_pos = requests.post('https://ticketingweb.passo.com.tr/api/passoweb/beforepaynkolayvirtualpos', headers=before_pay_n_kolay_virtual_pos_headers, json=json_data, verify=False)
    before_pay_n_kolay_virtual_pos_data = before_pay_n_kolay_virtual_pos.json()
    
    if before_pay_n_kolay_virtual_pos_data["isError"]:
        return 'error'
    before_pay_n_kolay_virtual_pos_data_amount = before_pay_n_kolay_virtual_pos_data["value"]['amount']  # float type
    before_pay_n_kolay_virtual_pos_data_sx = before_pay_n_kolay_virtual_pos_data["value"]['sx']
    before_pay_n_kolay_virtual_pos_data_clientReferenceCode = before_pay_n_kolay_virtual_pos_data["value"]['clientReferenceCode']
    before_pay_n_kolay_virtual_pos_data_productId = before_pay_n_kolay_virtual_pos_data["value"]['productId']
    before_pay_n_kolay_virtual_pos_data_second = before_pay_n_kolay_virtual_pos_data["value"]['second']
    before_pay_n_kolay_virtual_pos_cookie = before_pay_n_kolay_virtual_pos.cookies.get_dict()
    for key in before_pay_n_kolay_virtual_pos_cookie:
        cookies[key] = before_pay_n_kolay_virtual_pos_cookie[key]
#now
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'null',
        'User-Agent': 'Passo;Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F) CTV',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'X-Requested-With': 'com.aktifbank.passo',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': f'TS01a1807a={cookies["TS01a1807a"]}; BIGipServerVip_Prod_IksirSanalPos_https.app~Vip_Prod_IksirSanalPos_https_pool={cookies["BIGipServerVip_Prod_IksirSanalPos_https.app~Vip_Prod_IksirSanalPos_https_pool"]};cookie={cookies["cookie"]}; TS01885cf1={cookies["TS01885cf1"]}',
    }

    data = {
        'sx': before_pay_n_kolay_virtual_pos_data_sx,
        'amount': before_pay_n_kolay_virtual_pos_data_amount,
        'productId': before_pay_n_kolay_virtual_pos_data_productId,
        'clientRefCode': before_pay_n_kolay_virtual_pos_data_clientReferenceCode,
        'successUrl': 'https://www.passo.com.tr/successnkolay',
        'failUrl': 'https://www.passo.com.tr/failnkolay',
        'second': int(before_pay_n_kolay_virtual_pos_data_second),
        'cardCampaign': '0',
        'bin': '',
    }

    pay_n_kolay_vpos = requests.post('https://paynkolay.nkolayislem.com.tr/Vpos', headers=headers, data=data, verify=False)

    pay_n_kolay_vpos_cookies = pay_n_kolay_vpos.cookies.get_dict()
    
    for key in pay_n_kolay_vpos_cookies:
        if "Antiforgery" in key:
            cookies["aspNetCore_antiforgery"] = pay_n_kolay_vpos_cookies[key]
            continue
        cookies[key] = pay_n_kolay_vpos_cookies[key]

    
    S = BeautifulSoup(pay_n_kolay_vpos.text, 'lxml')

    ci = S.find(id='ci').get('value')
    su = S.find(id='su').get('value')
    fu = S.find(id='fu').get('value')
    pid = S.find(id='pid').get('value')
    cref = S.find(id='cref').get('value')
    amorj = S.find(id='amorj').get('value')
    secorj = S.find(id='secorj').get('value')
    secrem = S.find(id='secrem').get('value')
    binen = S.find(id='binen').get('value')
    campen = S.find(id='campen').get('value')
    namSur = S.find(id='namSur').get('value')
    usethreed = S.find(id='usethreed').get('value')
    hashData = S.find(id='hashData').get('value')
    agentCode = S.find(id='agentCode').get('value')
    detail = S.find(id='detail').get('value')
    transactionType = S.find(id='transactionType').get('value')
    sx = S.find(id='sx').get('value')
    TransactionTrxId = S.find(id='TransactionTrxId').get('value')
    __RequestVerificationToken = S.find(name='RequestVerificationToken')
    
    #######################################
    installment_data = get_installment(cookies, sx, amorj, pid)
    
    tsx1 = installment_data[0]
    tsx3 = installment_data[1]
    tsx5 = installment_data[2]
    ########################################
    l_ = asyncio.get_event_loop()
    answer = l_.run_until_complete(main__(l_, 540))
    l_.close()
    print(f"answer from first promot: {answer}")
    if answer == 'yes' or answer == 'Yes':
        print(f'[{answer}] Proceeding to pay...')
        payment_status = make_payment(name,cardnumber,cardexpiredatemonth,cardexpiredateyear,cardcvv2,cookies, ci, su, fu, pid, cref, amorj, secorj, secrem, binen, campen, namSur, usethreed, hashData, agentCode, detail, transactionType,sx, TransactionTrxId,__RequestVerificationToken, tsx1, tsx3, tsx5)
        if payment_status == 'done':
            return 'done'
        return 'error'
    elif answer == 'no':
        return 'error'
    else:
        print('Extending time...')
        valid = check_token_validity()
        print(f'Token status before extending time: {valid}')
        if valid == 'invalid':
            get_new_token()
        elif valid == 'new_otp_required':
            return
        before_pay_n_kolay_virtual_pos_headers = {
        "Access-Control-Request-Headers":
        "authorization,content-type,currentculture","Accept":"Accept: application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Authorization": "Bearer " + get_token(email),"Connection": "close","Content-Type": "application/json;charset=utf-8",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
        before_pay_n_kolay_virtual_pos = requests.post('https://ticketingweb.passo.com.tr/api/passoweb/beforepaynkolayvirtualpos', headers=before_pay_n_kolay_virtual_pos_headers, json=json_data, verify=False)
        before_pay_n_kolay_virtual_pos_data = before_pay_n_kolay_virtual_pos.json()
        if before_pay_n_kolay_virtual_pos_data["isError"]:
            print('Error! in before pay n kolay virtual pos')
            return 'error'
        before_pay_n_kolay_virtual_pos_data_amount = before_pay_n_kolay_virtual_pos_data["value"]['amount']  # float type
        before_pay_n_kolay_virtual_pos_data_sx = before_pay_n_kolay_virtual_pos_data["value"]['sx']
        before_pay_n_kolay_virtual_pos_data_clientReferenceCode = before_pay_n_kolay_virtual_pos_data["value"]['clientReferenceCode']
        before_pay_n_kolay_virtual_pos_data_productId = before_pay_n_kolay_virtual_pos_data["value"]['productId']
        before_pay_n_kolay_virtual_pos_data_second = before_pay_n_kolay_virtual_pos_data["value"]['second']
        before_pay_n_kolay_virtual_pos_cookie = before_pay_n_kolay_virtual_pos.cookies.get_dict()
        for key in before_pay_n_kolay_virtual_pos_cookie:
            cookies[key] = before_pay_n_kolay_virtual_pos_cookie[key]
        data = {
            'sx': before_pay_n_kolay_virtual_pos_data_sx,
            'amount': before_pay_n_kolay_virtual_pos_data_amount,
            'productId': before_pay_n_kolay_virtual_pos_data_productId,
            'clientRefCode': before_pay_n_kolay_virtual_pos_data_clientReferenceCode,
            'successUrl': 'https://www.passo.com.tr/successnkolay',
            'failUrl': 'https://www.passo.com.tr/failnkolay',
            'second': int(before_pay_n_kolay_virtual_pos_data_second),
            'cardCampaign': '0',
            'bin': '',
        }
        pay_n_kolay_vpos = requests.post('https://paynkolay.nkolayislem.com.tr/Vpos', headers=headers, data=data, verify=False)
        pay_n_kolay_vpos_cookies = pay_n_kolay_vpos.cookies.get_dict()
        for key in pay_n_kolay_vpos_cookies:
            if "Antiforgery" in key:
                cookies["aspNetCore_antiforgery"] = pay_n_kolay_vpos_cookies[key]
                continue
            cookies[key] = pay_n_kolay_vpos_cookies[key]
        S = BeautifulSoup(pay_n_kolay_vpos.text, 'lxml')

        ci = S.find(id='ci').get('value')
        su = S.find(id='su').get('value')
        fu = S.find(id='fu').get('value')
        pid = S.find(id='pid').get('value')
        cref = S.find(id='cref').get('value')
        amorj = S.find(id='amorj').get('value')
        secorj = S.find(id='secorj').get('value')
        secrem = S.find(id='secrem').get('value')
        binen = S.find(id='binen').get('value')
        campen = S.find(id='campen').get('value')
        namSur = S.find(id='namSur').get('value')
        usethreed = S.find(id='usethreed').get('value')
        hashData = S.find(id='hashData').get('value')
        agentCode = S.find(id='agentCode').get('value')
        detail = S.find(id='detail').get('value')
        transactionType = S.find(id='transactionType').get('value')
        sx = S.find(id='sx').get('value')
        TransactionTrxId = S.find(id='TransactionTrxId').get('value')
        __RequestVerificationToken = S.find(name='RequestVerificationToken')

        l_new = asyncio.get_event_loop()
        answer2 = l_new.run_until_complete(main__2(l_new, 240))
        l_new.close()
        if answer2 == 'yes' or answer2 == 'Yes':
            print(f'[{answer2}]>> Trying to pay...')
            payment_status = make_payment(cookies, ci, su, fu, pid, cref, amorj, secorj, secrem, binen, campen, namSur, usethreed, hashData, agentCode, detail, transactionType, sx, TransactionTrxId, __RequestVerificationToken)
            if payment_status == 'done':
                return 'done'
            return 'error'
        else:
            return 'error'
    #####################################################################################

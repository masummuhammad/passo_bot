import time


import requests
from bs4 import BeautifulSoup
from threading import Timer


def make_payment(name,cardnumber,cardexpiredatemonth,cardexpiredateyear,cardcvv2,cookies, ci, su, fu, pid, cref, amorj, secorj, secrem, binen, campen, namSur, usethreed, hashData, agentCode, detail, transactionType,sx, TransactionTrxId,__RequestVerificationToken, tsx1, tsx3, tsx5):

    if manual_card_input:
        name_local = input("Enter Name>>")
        cardnumber_local = input("Enter Card Number>>")
        cardexpiredatemonth_local = input("Enter Card expire date month>>")
        cardexpiredateyear_local = input("Enter Card expire year ex. 2026>>")
        cardcvv2_local = input("Enter Card cvv2>>")
    else:
        name_local = name
        cardnumber_local = cardnumber
        cardexpiredatemonth_local = cardexpiredatemonth
        cardexpiredateyear_local = cardexpiredateyear
        cardcvv2_local = cardcvv2

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://paynkolay.nkolayislem.com.tr',
        'User-Agent': 'Passo;Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F) CTV',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'X-Requested-With': 'com.aktifbank.passo',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://paynkolay.nkolayislem.com.tr/Vpos',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': f'.AspNetCore.Antiforgery.P5e449hmYiQ={cookies["aspNetCore_antiforgery"]}; TS01a1807a={cookies["TS01a1807a"]}; BIGipServerVip_Prod_IksirSanalPos_https.app~Vip_Prod_IksirSanalPos_https_pool={cookies["BIGipServerVip_Prod_IksirSanalPos_https.app~Vip_Prod_IksirSanalPos_https_pool"]}; cookie={cookies["cookie"]}; TS01885cf1={cookies["TS01885cf1"]}',
    }
    data = {
        'viewPages': 'new',
        'ci': ci,
        'su': su,
        'fu': fu,
        'pid': pid,
        'cref': cref,
        'amorj': amorj,
        'secorj': secorj,
        'secrem': secrem,
        'binen': binen,
        'campen': campen,
        'namSur': namSur,
        'usethreed': usethreed,
        'hashData': hashData,
        'agentCode': agentCode,
        'detail': detail,
        'environment': 'ORTAKODEME',
        'language': 'tr',
        'transactionType': transactionType,
        'paymentRouter': 'NONE',
        'payByLinkOid': '',
        'getUrlAddress': 'https://www.passo.com.tr/failnkolay',
        'sx': sx,
        'currencyCode': '949',
        'TransactionTrxId': TransactionTrxId,
        'CardStorageRegister': 'false',
        'customerKey': '',
        'createUser': '',
        'name': name_local,
        'number': f"{cardnumber_local[0]}{cardnumber_local[1]}{cardnumber_local[2]}{cardnumber_local[3]} {cardnumber_local[4]}{cardnumber_local[5]}{cardnumber_local[6]}{cardnumber_local[7]} {cardnumber_local[8]}{cardnumber_local[9]}{cardnumber_local[10]}{cardnumber_local[11]} {cardnumber_local[12]}{cardnumber_local[13]}{cardnumber_local[14]}{cardnumber_local[15]}",
        'ay': cardexpiredatemonth_local,
        'yil': cardexpiredateyear_local,
        'cvv': cardcvv2_local,
        'tno': '1',
        'tsx1': tsx1,
        'tsx3': tsx3,
        'tsx5': tsx5,
        '__RequestVerificationToken': __RequestVerificationToken,
    }

    payment_perform = requests.post('https://paynkolay.nkolayislem.com.tr/Vpos/Payment/Perform', headers=headers, data=data, verify=False)
    payment_perform_data = payment_perform.text
    S = BeautifulSoup(payment_perform_data, 'lxml')
    terminalmerchantid = S.find('input', {'name': 'terminalmerchantid'}).get('value')
    txnamount = S.find('input', {'name': 'txnamount'}).get('value')
    orderid = S.find('input', {'name': 'orderid'}).get('value')
    terminalid = S.find('input', {'name': 'terminalid'}).get('value')
    successurl = S.find('input', {'name': 'successurl'}).get('value')
    errorurl = S.find('input', {'name': 'errorurl'}).get('value')
    customeremailaddress = S.find('input', {'name': 'customeremailaddress'}).get('value')
    customeripaddress = S.find('input', {'name': 'customeripaddress'}).get('value')
    secure3dhash = S.find('input', {'name': 'secure3dhash'}).get('value')
    strCompanyName = S.find('input', {'name': 'strCompanyName'}).get('value')
    strtimestamp = S.find('input', {'name': 'strtimestamp'}).get('value')
    payment_perform_cookies = payment_perform.cookies.get_dict()
    for key in payment_perform_cookies:
        cookies[key] = payment_perform_cookies[key]
    ########################################################################################################################
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://paynkolay.nkolayislem.com.tr',
        'User-Agent': 'Passo;Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F) CTV',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'X-Requested-With': 'com.aktifbank.passo',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://paynkolay.nkolayislem.com.tr/',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': f"rxVisitor={cookies['rxVisitor']}; dtLatC={cookies['dtLatC']}; dtPC={cookies['dtPC']}; dtSa={cookies['dtSa']}; dtCookie={cookies['dtCookie']}; rxvt={cookies['rxvt']}",
    }
    data = {
        'mode': 'PROD',
        'secure3dsecuritylevel': '3d',
        'apiversion': 'v0.01',
        'terminalprovuserid': 'PROVAUT',
        'terminaluserid': 'PROVAUT',
        'terminalmerchantid': terminalmerchantid,
        'txntype': 'sales',
        'txnamount': txnamount,
        'txncurrencycode': '949',
        'txninstallmentcount': '1',
        'orderid': orderid,
        'terminalid': terminalid,
        'successurl': successurl,
        'errorurl': errorurl,
        'customeremailaddress': customeremailaddress,
        'customeripaddress': customeripaddress,
        'secure3dhash': secure3dhash,
        'strCompanyName': strCompanyName,
        'strlang': 'tr',
        'strRefreshTime': '10',
        'strtimestamp': strtimestamp,
        'cardnumber': cardnumber_local,
        'cardexpiredatemonth': cardexpiredatemonth_local,
        'cardexpiredateyear': f"{cardexpiredateyear_local[2]}{cardexpiredateyear_local[3]}",
        'cardcvv2': cardcvv2_local,
    }
    response_gt3dengine = requests.post('https://sanalposprov.garanti.com.tr/servlet/gt3dengine', headers=headers, data=data, verify=False)
    gt3dengine_data = response_gt3dengine.text
    S = BeautifulSoup(gt3dengine_data, 'lxml')
    goreq = S.find('input', {'name': 'goreq'}).get('value')
    response_gt3dengine_cookies = response_gt3dengine.cookies.get_dict()
    for key in response_gt3dengine_cookies:
        cookies[key] = response_gt3dengine_cookies[key]
    ################################################################
    headers = {
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'origin': 'https://sanalposprov.garanti.com.tr',
        'user-agent': 'Passo;Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F) CTV',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'x-requested-with': 'com.aktifbank.passo',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'referer': 'https://sanalposprov.garanti.com.tr/',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': f'dtCookie={cookies["dtCookie"]}'
    }
    data = {
        'goreq': goreq,
    }
    troy_approve = requests.post('https://goguvenliodeme.bkm.com.tr/troy/approve', headers=headers, data=data, verify=False)
    troy_approve_data = troy_approve.text
    S = BeautifulSoup(troy_approve_data, 'lxml')
    goredreq = S.find('input', {'name': 'goredreq'}).get('value')
    troy_approve_cookies = troy_approve.cookies.get_dict()
    for key in troy_approve_cookies:
        cookies[key] = troy_approve_cookies[key]
    ########################################################
    TDSecureTroy_url = "https://acs.yapikredi.com.tr:443/TDSecureTroy/"
    TDSecureTroy_cookies = {"JSESSIONID": "", "__zzatihs-w-yapi3ds-prod": "", "cfidsihs-w-yapi3ds-prod": ""}
    TDSecureTroy_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "https://goguvenliodeme.bkm.com.tr", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Passo;Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F) CTV", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "X-Requested-With": "com.aktifbank.passo", "Sec-Fetch-Site": "cross-site", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Dest": "document", "Referer": "https://goguvenliodeme.bkm.com.tr/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
    TDSecureTroy_data = {"goredreq": goredreq}
    TDSecureTroy = requests.post(TDSecureTroy_url, headers=TDSecureTroy_headers, cookies=TDSecureTroy_cookies, data=TDSecureTroy_data, verify=False)
    TDSecureTroy_cookies = TDSecureTroy.cookies.get_dict()
    for key in TDSecureTroy_cookies:
        cookies[key] = TDSecureTroy_cookies[key]
    ############################################################################################
    sendPush_url = "https://acs.yapikredi.com.tr/TDSecureTroy/rest/3d/sendPush"
    sendPush_cookies = {"JSESSIONID": cookies['JSESSIONID'], "__zzatihs-w-yapi3ds-prod": "", "cfidsihs-w-yapi3ds-prod": ""}
    sendPush_headers = {"Cache-Control": "max-age=0",
                            "Upgrade-Insecure-Requests": "1",
                            "Origin": "https://goguvenliodeme.bkm.com.tr",
                            "Content-Type": "application/x-www-form-urlencoded",
                            "User-Agent": "Passo;Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F) CTV",
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                            "X-Requested-With": "com.aktifbank.passo",
                            "Sec-Fetch-Site": "cross-site",
                            "Sec-Fetch-Mode": "navigate",
                            "Sec-Fetch-Dest": "document",
                            "Referer": "https://goguvenliodeme.bkm.com.tr",
                            "Accept-Encoding": "gzip, deflate",
                            "Accept-Language": "en-US,en;q=0.9",
                            "Connection": "keep-alive"}

    sendPush = requests.post(sendPush_url, headers=sendPush_headers, cookies=sendPush_cookies, verify=False)
    sendPush_cookies = sendPush.cookies.get_dict()
    for key in sendPush_cookies:
        cookies[key] = sendPush_cookies[key]
    ###########################################################################################
    isTransactionCompleted_url = "https://acs.yapikredi.com.tr:443/TDSecureTroy/rest/3d/isTransactionCompleted"
    isTransactionCompleted_cookies = {"JSESSIONID": cookies['JSESSIONID'], "cfidsihs-w-yapi3ds-prod": "", "__zzatihs-w-yapi3ds-prod": ""}
    isTransactionCompleted_headers = {"Accept": "application/json, text/plain, */*", "User-Agent": "Passo;Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F) CTV", "Content-Type": "application/json;charset=utf-8", "Origin": "https://acs.yapikredi.com.tr", "X-Requested-With": "com.aktifbank.passo", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://acs.yapikredi.com.tr/TDSecureTroy/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
    isTransactionCompleted = requests.post(isTransactionCompleted_url, headers=isTransactionCompleted_headers, cookies=isTransactionCompleted_cookies, verify=False)
    print(isTransactionCompleted.json())
    x = 0
    goredres = ''
    while x < 100:
        x += 1
        isTransactionCompleted = requests.post(isTransactionCompleted_url, headers=isTransactionCompleted_headers, cookies=isTransactionCompleted_cookies, verify=False)
        isTransactionCompleted_json = isTransactionCompleted.json()
        # print(isTransactionCompleted_json)
        try:
            if isTransactionCompleted_json["status"] == 2:
                print('payment not approved yet')
                continue
            if isTransactionCompleted_json["status"] == 1:
                goredres = isTransactionCompleted_json["result"]["returnForm"]["goredres"]
                print('Payment approved, now trying to make purchase')
                if goredres:
                    break
            if isTransactionCompleted_json["status"] == 4:
                print('Payment approval time out!')
                return '3d_payment_time_out_error'
        except Exception as e:
            print(e)

    url_commit = "https://goguvenliodeme.bkm.com.tr/troy/redirection/commit"
    commit_header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'connection': 'keep-alive',
    'content-length': '941',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': f'dtCookie={cookies["dtCookie"]}',
    'host': 'goguvenliodeme.bkm.com.tr',
    'origin': 'https://acs.yapikredi.com.tr',
    'referer': 'https://acs.yapikredi.com.tr/',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Passo;Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F) CTV',
    'x-requested-with': 'com.aktifbank.passo'
    }
    req_body = {'goredres': goredres}
    commit_res = requests.post(url_commit, headers=commit_header, data=req_body, verify=False)
    print(commit_res.status_code)
    commit_data = commit_res.text
    S = BeautifulSoup(commit_data, 'lxml')
    commit_gores = S.find('input', {'name': 'gores'}).get('value')

    url_troygateway = "https://sanalposprov.garanti.com.tr/servlet/troygateway"
    troygateway_header = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'connection': 'keep-alive',
        'content-length': '814',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': f'rxVisitor={cookies["rxVisitor"]}; dtLatC={cookies["dtLatC"]}; dtPC={cookies["dtPC"]}; dtSa={cookies["dtSa"]}; rxvt={cookies["rxvt"]}; dtCookie={cookies["dtCookie"]}',
        'host': 'sanalposprov.garanti.com.tr',
        'origin': 'https://goguvenliodeme.bkm.com.tr',
        'referer': 'https://goguvenliodeme.bkm.com.tr/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Passo;Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F) CTV',
        'x-requested-with': 'com.aktifbank.passo'
    }
    data_troygateway = {'gores': commit_gores}
    response_troygateway = requests.post(url_troygateway, headers=troygateway_header, data=data_troygateway, verify=False)
    print(response_troygateway.status_code)
    try:
        troygateway_data = response_troygateway.text
        S = BeautifulSoup(troygateway_data, 'lxml')
        xid = S.find('input', {'name': 'xid'}).get('value')
        mdstatus = S.find('input', {'name': 'mdstatus'}).get('value')
        mderrormessage = S.find('input', {'name': 'mderrormessage'}).get('value')
        txnstatus = S.find('input', {'name': 'txnstatus'}).get('value')
        eci = ''
        cavv = S.find('input', {'name': 'cavv'}).get('value')
        paressyntaxok = S.find('input', {'name': 'paressyntaxok'}).get('value')
        paresverified = S.find('input', {'name': 'paresverified'}).get('value')
        version = S.find('input', {'name': 'version'}).get('value')
        ireqcode = S.find('input', {'name': 'ireqcode'}).get('value')
        ireqdetail = S.find('input', {'name': 'ireqdetail'}).get('value')
        vendorcode = S.find('input', {'name': 'vendorcode'}).get('value')
        cavvalgorithm = S.find('input', {'name': 'cavvalgorithm'}).get('value')
        md = S.find('input', {'name': 'md'}).get('value')
        terminalid = S.find('input', {'name': 'terminalid'}).get('value')
        oid = S.find('input', {'name': 'oid'}).get('value')
        authcode = S.find('input', {'name': 'authcode'}).get('value')
        response = S.find('input', {'name': 'response'}).get('value')
        errmsg = S.find('input', {'name': 'errmsg'}).get('value')
        hostmsg = S.find('input', {'name': 'hostmsg'}).get('value')
        procreturncode = S.find('input', {'name': 'procreturncode'}).get('value')
        transid = S.find('input', {'name': 'transid'}).get('value')
        hostrefnum = S.find('input', {'name': 'hostrefnum'}).get('value')
        rnd = S.find('input', {'name': 'rnd'}).get('value')
        hash = S.find('input', {'name': 'hash'}).get('value')
        hashparams = S.find('input', {'name': 'hashparams'}).get('value')
        hashparamsval = S.find('input', {'name': 'hashparamsval'}).get('value')
        clientid = S.find('input', {'name': 'clientid'}).get('value')
        MaskedPan = S.find('input', {'name': 'MaskedPan'}).get('value')
        strRefreshTime = '10'
        txncurrencycode = S.find('input', {'name': 'txncurrencycode'}).get('value')
        errorurl = S.find('input', {'name': 'errorurl'}).get('value')
        txninstallmentcount = S.find('input', {'name': 'txninstallmentcount'}).get('value')
        customeremailaddress = S.find('input', {'name': 'customeremailaddress'}).get('value')
        successurl = S.find('input', {'name': 'successurl'}).get('value')
        terminalmerchantid = S.find('input', {'name': 'terminalmerchantid'}).get('value')
        strCompanyName = S.find('input', {'name': 'strCompanyName'}).get('value')
        terminalprovuserid = S.find('input', {'name': 'terminalprovuserid'}).get('value')
        terminalid = S.find('input', {'name': 'terminalid'}).get('value')
        txnamount = S.find('input', {'name': 'txnamount'}).get('value')
        mode = S.find('input', {'name': 'mode'}).get('value')
        secure3dsecuritylevel = S.find('input', {'name': 'secure3dsecuritylevel'}).get('value')
        orderid = S.find('input', {'name': 'orderid'}).get('value')
        customeripaddress = S.find('input', {'name': 'customeripaddress'}).get('value')
        strtimestamp = S.find('input', {'name': 'strtimestamp'}).get('value')
        strlang = S.find('input', {'name': 'strlang'}).get('value')
        secure3dhash = S.find('input', {'name': 'secure3dhash'}).get('value')
        txntype = S.find('input', {'name': 'txntype'}).get('value')
        apiversion = S.find('input', {'name': 'apiversion'}).get('value')

        url_VPosApi = f"https://iksirext.nkolayislem.com.tr:443{successurl.split('.tr')[1]}"
        VPosApi_header = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'connection': 'keep-alive',
            # 'content-length': '1874',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': f'cookie={cookies["cookie"]}; TS01be67d8={cookies["TS01be67d8"]};',
            'host': 'iksirext.nkolayislem.com.tr',
            'origin': 'https://sanalposprov.garanti.com.tr',
            'referer': 'https://sanalposprov.garanti.com.tr/',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Passo;Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F) CTV',
            'x-requested-with': 'com.aktifbank.passo'
        }
        VPosApi_data = {
            'xid': xid,
            'mdstatus': mdstatus,
            'mderrormessage': mderrormessage,
            'txnstatus': txnstatus,
            'eci': '',
            'cavv': cavv,
            'paressyntaxok': paressyntaxok,
            'paresverified': paresverified,
            'version': version,
            'ireqcode': ireqcode,
            'ireqdetail': ireqdetail,
            'vendorcode': vendorcode,
            'cavvalgorithm': cavvalgorithm,
            'md': md,
            'terminalid': terminalid,
            'oid': oid,
            'authcode': authcode,
            'response': response,
            'errmsg': errmsg,
            'hostmsg': hostmsg,
            'procreturncode': procreturncode,
            'transid': transid,
            'hostrefnum': hostrefnum,
            'rnd': rnd,
            'hash': hash,
            'hashparams': hashparams,
            'hashparamsval': hashparamsval,
            'clientid': clientid,
            'MaskedPan': MaskedPan,
            'strRefreshTime': '10',
            'txncurrencycode': txncurrencycode,
            'errorurl': errorurl,
            'txninstallmentcount': txninstallmentcount,
            'customeremailaddress': customeremailaddress,
            'successurl': successurl,
            'terminalmerchantid': terminalmerchantid,
            'strCompanyName': strCompanyName,
            'terminalprovuserid': terminalprovuserid,
            'txnamount': txnamount,
            'mode': mode,
            'secure3dsecuritylevel': secure3dsecuritylevel,
            'orderid': orderid,
            'customeripaddress': customeripaddress,
            'strtimestamp': strtimestamp,
            'strlang': strlang,
            'secure3dhash': secure3dhash,
            'txntype': txntype,
            'apiversion': apiversion
        }

        VPosApi_response = requests.post(url_VPosApi, headers=VPosApi_header, data=VPosApi_data, verify=False)
        print(VPosApi_response.status_code)
        VPosApi_cookies = VPosApi_response.cookies.get_dict()
        for key in VPosApi_cookies:
            cookies[key] = VPosApi_cookies[key]
        VPosApi_data = VPosApi_response.text
        S = BeautifulSoup(VPosApi_data, 'lxml')
        # xid = S.find('input', {'name': 'xid'}).get('value')
        RESPONSE_CODE = S.find('input', {'name': 'RESPONSE_CODE'}).get('value')
        RESPONSE_DATA = S.find('input', {'name': 'RESPONSE_DATA'}).get('value')
        REFERENCE_CODE = S.find('input', {'name': 'REFERENCE_CODE'}).get('value')
        USE_3D = S.find('input', {'name': 'USE_3D'}).get('value')
        MERCHANT_NO = S.find('input', {'name': 'MERCHANT_NO'}).get('value')
        AUTH_CODE = S.find('input', {'name': 'AUTH_CODE'}).get('value')
        CLIENT_REFERENCE_CODE = S.find('input', {'name': 'CLIENT_REFERENCE_CODE'}).get('value')
        TIMESTAMP = S.find('input', {'name': 'TIMESTAMP'}).get('value')
        TRANSACTION_AMOUNT = S.find('input', {'name': 'TRANSACTION_AMOUNT'}).get('value')
        AUTHORIZATION_AMOUNT = S.find('input', {'name': 'AUTHORIZATION_AMOUNT'}).get('value')
        COMMISION = S.find('input', {'name': 'COMMISION'}).get('value')
        COMMISION_RATE = S.find('input', {'name': 'COMMISION_RATE'}).get('value')
        INSTALLMENT = S.find('input', {'name': 'INSTALLMENT'}).get('value')
        RND = S.find('input', {'name': 'RND'}).get('value')
        hashData = S.find('input', {'name': 'hashData'}).get('value')

        url_mobilesuccessnkolay = "https://www.passo.com.tr/successnkolay"
        header_mobilesuccessnkolay = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'connection': 'keep-alive',
            'content-length': '1874',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': f"TS01859013={cookies['TS01859013']}; TS22476f14027={cookies['TS22476f14027']};",
            'host': 'iksirext.nkolayislem.com.tr',
            'origin': 'https://sanalposprov.garanti.com.tr',
            'referer': 'https://sanalposprov.garanti.com.tr/',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Passo;Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F) CTV',
            'x-requested-with': 'com.aktifbank.passo'
        }
        data_mobilesuccessnkolay = {
            'RESPONSE_CODE': RESPONSE_CODE,
            'RESPONSE_DATA': RESPONSE_DATA,
            'REFERENCE_CODE': REFERENCE_CODE,
            'USE_3D': USE_3D,
            'MERCHANT_NO': MERCHANT_NO,
            'AUTH_CODE': AUTH_CODE,
            'CLIENT_REFERENCE_CODE': CLIENT_REFERENCE_CODE,
            'TIMESTAMP': TIMESTAMP,
            'TRANSACTION_AMOUNT': TRANSACTION_AMOUNT,
            'AUTHORIZATION_AMOUNT': AUTHORIZATION_AMOUNT,
            'COMMISION': COMMISION,
            'COMMISION_RATE': COMMISION_RATE,
            'INSTALLMENT': INSTALLMENT,
            'RND': RND,
            'hashData': hashData
        }
        mobilesuccessnkolay = requests.post(url_mobilesuccessnkolay, headers=header_mobilesuccessnkolay, data=data_mobilesuccessnkolay, verify=False)
        print(mobilesuccessnkolay.status_code)
        print(mobilesuccessnkolay.text)
        print('finished')
        return 'done'
    except Exception as e:
        print(e)
        return 'error'

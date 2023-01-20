import requests
from bs4 import BeautifulSoup


def get_installment(cookies, sx, amorj, pid):
    installments_cookies = {
            'BIGipServerVip_Prod_IksirSanalPos_https.app~Vip_Prod_IksirSanalPos_https_pool': cookies["BIGipServerVip_Prod_IksirSanalPos_https.app~Vip_Prod_IksirSanalPos_https_pool"],
            'cookie': cookies["cookie"],
            'TS01885cf1': cookies["TS01885cf1"],
        }
    installments_headers = {
        'Host': 'paynkolay.nkolayislem.com.tr',
        'Connection': 'keep-alive',
        'Accept': 'text/html, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Passo;Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTT Build/LVY48F) CTV',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://paynkolay.nkolayislem.com.tr',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://paynkolay.nkolayislem.com.tr/Vpos',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    installments_data = {
        'sx': sx,
        'amorj': amorj,
        'cardnumber': '5400 6270 2389 5415',
        'pid': pid,
        'usethreed': '',
        'getUrlAddress': '',
        'iscardvalid': 'true',
        'transactionId': '',
        'currencyCode': '949',
        'instalments': '0',
        'language': 'tr',
        'foreignPaymenAllow': 'false',
        'viewPage': 'new',
    }
    installments_response = requests.post('https://paynkolay.nkolayislem.com.tr/VPos/Payment/Installments', cookies=installments_cookies, headers=installments_headers, data=installments_data, verify=False)
    installments_html = BeautifulSoup(installments_response.text, 'lxml')
    tsx1 = installments_html.find('input', {'name': 'tsx1'}).get('value')
    tsx3 = installments_html.find('input', {'name': 'tsx3'}).get('value')
    tsx5 = installments_html.find('input', {'name': 'tsx5'}).get('value')
    return [tsx1, tsx3, tsx5]

import requests, json

from refresh import refresh_lst


def binance_io(coin):
    lst = []
    headers = {
        'authority': 'www.binance.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
        'cache-control': 'max-age=0',
        'cookie': 'BNC-Location=; __BNC_USER_DEVICE_ID__={"685cf930488f50c55b2ffc5da440d9c4":{"date":1662202820956,"value":"1662202819699HMFOUIft3fCcPfRGNjz"}}; fiat-prefer-currency=RUB; bnc-uuid=f62a4ee1-472d-42ee-8aa7-ac3eb852c2f9; source=referral; campaign=www.binance.com; se_gd=1cbGgUVpbRbB1FWNbDAZgZZCQDQcTBSVFod5bU0NFNSUgUFNXVAR1; se_gsd=fAAnXDRgNgAjNxIBJQM2UwAHEApWBQoGUFtBUl1RVVNUJFNS1; logined=y; BNC_FV_KEY=333cc5d3b3eca717b4e7cae75fe414d4d42e4d14; monitor-uuid=31adc5be-246f-4a90-a61b-7db9c83dc7b1; userPreferredCurrency=RUB_USD; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2235311803%22%2C%22first_id%22%3A%221831baa0cb8181-0c2fe6277897248-26021c51-3686400-1831baa0cb9c5e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTgzMWJhYTBjYjgxODEtMGMyZmU2Mjc3ODk3MjQ4LTI2MDIxYzUxLTM2ODY0MDAtMTgzMWJhYTBjYjljNWUiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIzNTMxMTgwMyJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2235311803%22%7D%2C%22%24device_id%22%3A%221831baa0cb8181-0c2fe6277897248-26021c51-3686400-1831baa0cb9c5e%22%7D; BNC_FV_KEY_EXPIRE=1662899563014; lang=ru; se_sd=QsMGVVgoTAaUBAJBSF1dgZZUxAhtREYVlIXBRVUVFNcVABVNXVED1; gtId=21cc238a-d993-49c6-b973-ed10e5e5e71b; cr00=4409F439FE09A1D52E21134E141CB8CF; d1og=web.35311803.3258028A534F6ADAB6EB36A92EBC6BAF; r2o1=web.35311803.23D9BE0B8EB1CADEC44045D15B81E4E7; f30l=web.35311803.9167D6F2B95EA7796DE42312EDDADBAD; p20t=web.35311803.447E1C7B9A861336BF1F984BDA6F3ED2; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Sep+11+2022+11%3A33%3A10+GMT%2B0500+(%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.34.0&isIABGlobal=false&hosts=&consentId=960224e3-9e30-4d9f-b720-d463cb86bf9b&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }

    params = (
        ('coin', f'{coin.upper()}'),
        ('lang', 'ru'),
    )

    response = requests.get('https://www.binance.com/bapi/capital/v2/public/capital/config/getOne', headers=headers, params=params)

    res = json.loads(response.text)
    for i in res["data"]:
        if i['depositEnable'] == True and i['withdrawEnable'] == True:
            lst.append(i["name"].lower())
    return refresh_lst(lst)


if __name__ == '__main__':
    print(binance_io("GBP"))
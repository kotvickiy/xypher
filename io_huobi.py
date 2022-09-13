import requests, json

from refresh import refresh_lst



def huobi_io(coin):
    lst = []
    headers = {
        'authority': 'www.huobi.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
        'cache-control': 'max-age=0',
        'cookie': '_ga=GA1.1.324069324.1662615385; _ga_J76R0D6G87=GS1.1.1662615385.1.1.1662615515.60.0.0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2279A5C235A38174703B98D0F61200C4B89EF443C91062678E1A47989D98C53A0D%22%2C%22first_id%22%3A%221830758a0583c8-066db449e2a47c8-26021c51-3686400-1830758a059c8f%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24latest_utm_source%22%3A%22web_official_register_page%22%7D%2C%22%24device_id%22%3A%221830758a0583c8-066db449e2a47c8-26021c51-3686400-1830758a059c8f%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTgzMTY5MWE4OWYxYjAtMDVjYTkxZjFkMDE5ZDg4LTI2MDIxYzUxLTM2ODY0MDAtMTgzMTY5MWE4YTBjOTUiLCIkaWRlbnRpdHlfbG9naW5faWQiOiI3OUE1QzIzNUEzODE3NDcwM0I5OEQwRjYxMjAwQzRCODlFRjQ0M0M5MTA2MjY3OEUxQTQ3OTg5RDk4QzUzQTBEIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2279A5C235A38174703B98D0F61200C4B89EF443C91062678E1A47989D98C53A0D%22%7D%7D; _ha_session=1662830510923; HB_SSO=bmeoSGJqfmtMA7hYgRIH5PY2I0UkC6XArxgYtI7Z9eXWLIGU04cRf1zeNUSbWfbDvXBa6zHqaugdveL+EEFC38jw1yr662nZ1lziB6DNeJA6xK2vnrEUXti9oeUGw9F4DF+vmM95sd2wX2onBW5EAUQvVHSmg5RiL39n12RIX+3JPxB04zn0sniGNvTE6v9a5un7uzttnaMikafoOe3HAg==; HB-UC-TOKEN=bmeoSGJqfmtMA7hYgRIH5PY2I0UkC6XArxgYtI7Z9eXWLIGU04cRf1zeNUSbWfbDvXBa6zHqaugdveL+EEFC38jw1yr662nZ1lziB6DNeJA6xK2vnrEUXti9oeUGw9F4DF+vmM95sd2wX2onBW5EAUQvVHSmg5RiL39n12RIX+3JPxB04zn0sniGNvTE6v9a5un7uzttnaMikafoOe3HAg==; HB-PRO-TOKEN=IQ6B6UpA6ardcpNSN0ptzJDyaOQjUwvtFJ_M4-M1QUcY-uOP2m0-gvjE57ad1qDF; HB-OLD-TOKEN=IQ6B6UpA6ardcpNSN0ptzJDyaOQjUwvtFJ_M4-M1QUcY-uOP2m0-gvjE57ad1qDF; PHPSESSID=hftvmc5lopfc4c2qfp9fd9840f; token=IQ6B6UpA6ardcpNSN0ptzJDyaOQjUwvtFJ_M4-M1QUcY-uOP2m0-gvjE57ad1qDF; hb-otc-token=IQ6B6UpA6ardcpNSN0ptzJDyaOQjUwvtFJ_M4-M1QUcY-uOP2m0-gvjE57ad1qDF; hbsession=d5b573c3-9a4c-45b0-a94b-8cba68ed54d4',
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
        ('currency', f'{coin.lower()}'),
        ('r', '3xwm94'),
        ('x-b3-traceid', '87c5896fef8a3ce5ae87e48156aea726'),
    )

    response = requests.get('https://www.huobi.com/-/x/pro/v2/reference/currencies', headers=headers, params=params)

    res = json.loads(response.text)
    for i in res["data"][0]["chains"]:
        if i['depositStatus'] == "allowed" and i['withdrawStatus'] == "allowed":
            lst.append(i["displayName"].lower())
    return refresh_lst(lst)

if __name__ == "__main__":
    print(huobi_io("EGAME"))

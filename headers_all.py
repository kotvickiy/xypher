import requests, json

def get_json_xypher_all():
    headers = {
        'authority': 'xypher.io',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'XPHR=b2kqdktujlei44lgkbk7brihsrmfokda',
        'origin': 'https://xypher.io',
        'referer': 'https://xypher.io/Screener/Arbitrage',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = [
    ('ExchangesFrom[]', 'BNC'),
    ('ExchangesFrom[]', 'KCN'),
    ('ExchangesFrom[]', 'FTX'),
    ('ExchangesFrom[]', 'HBG'),
    ('ExchangesTo[]', 'BNC'),
    ('ExchangesTo[]', 'KCN'),
    ('ExchangesTo[]', 'FTX'),
    ('ExchangesTo[]', 'HBG'),
    ('Pairs[]', 'USDT'),
    ('Top100', 'false'),
    ]

    response = requests.post('https://xypher.io/Remote/API/MVP/GetPairs/Master', headers=headers, data=data)

    return json.loads(response.text)

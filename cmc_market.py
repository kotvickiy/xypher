import requests, json, csv


def symbol_coin(symbol):
    with open("./symbol_coin.csv", encoding="utf-8") as file:
        lst = [i.strip() for i in file.readlines()]
    for i in lst:
        if i.split(",")[0] == symbol:
            return i.split(",")[1]


def verify_cmc(coin, ex1, ex2):
    if coin == "EUR" or coin == "LTC3L" or coin == "LINK3S" or coin == "IOTA" or coin == "XRP3S" or coin == "XRP3L" or coin == "ETH3L" or coin == "BCH3L":
        return False
    try:
        headers = {
            'authority': 'api.coinmarketcap.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
            'cache-control': 'no-cache',
            'fvideo-id': '33dda3b79dce95f1913ba9abf34e0f5107fed3f8',
            'origin': 'https://coinmarketcap.com',
            'platform': 'web',
            'referer': 'https://coinmarketcap.com/',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'x-request-id': '8b5b6d8ba8384c929c24ec35621e2261',
        }
        params = (
            ('slug', f"{symbol_coin(coin)}"),
            ('start', '1'),
            ('quoteCurrencyId', '825'),
            ('limit', '100'),
            ('category', 'spot'),
            ('sort', 'cmc_rank_advanced'),
        )
        response = requests.get('https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest', headers=headers, params=params)
        flag = 0

        for i in json.loads(response.text)["data"]["marketPairs"]:
            if ex1 in i["exchangeName"].lower() and float(i["effectiveLiquidity"]) > 100:
                flag += 1
            if ex2 in i["exchangeName"].lower() and float(i["effectiveLiquidity"]) > 100:
                flag += 1

        if flag >= 2:
            # print(flag)
            return True
        else:
            # print(flag, coin, ex1, ex2, response.url)
            return False
    except KeyError:
        # print(coin, symbol_coin(coin))
        with open("error_coin.csv", "a", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow((coin, symbol_coin(coin)))
        return False

# verify_cmc("EGAME", "huobi", "kucoin")
# print(verify_cmc("EGAME", "huobi", "kucoin"))
# [7.55, 'EGAME', 'https://www.huobi.com/en-us/exchange/egame_usdt', '0.000328', 'https://www.kucoin.com/ru/trade/EGAME-USDT', '0.0003548']
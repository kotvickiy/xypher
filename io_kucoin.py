import requests, json

from refresh import refresh_lst



def kucoin_io(coin):
    lst = []
    headers = {
        'authority': 'www.kucoin.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
        'cache-control': 'max-age=0',
        'cookie': '_uetvid=bdcc5a30284611edaab545c43cba54ae; __cfruid=ee724a549a5530aa42b2249a7716a66fabcf5ecd-1662827880; SESSION=NjU3MzE4MjMtYWQ3OC00MTc5LWI2MWUtOWI5NTBkZDgyNzJj; version=62db8366269ee300011756ca; X-TRACE=byKYa2Y4zBhF5DWjwtCPTmhRdTDVU8FrtP40DAUMqGQ=; x-bullet-token=2neAiuYvAU5cbMXpmsXD5OJlewXCKryg8dSpDCgag8ZwbZpn3uIHi6siD_s132wYwoXOiOG0Q0Ek6Ttng-Zt7LOxXsy4xjbW4DNI0ZaZFPD5yWKtOCh28KqRyqznCVt1whuoNZhpWWE76TbqxpYZABmsFGVqGB1O.boHjUZCZEyn_Gv7FGwJ_zA==; __cf_bm=HJQlZkAlZECiLhLnMg.dS12EFduPs7uSkImLHqxl.bg-1662831783-0-AdoybBryQjPm+ucKdNIZ/gVvDZrXEY1z6vU6JXFenZxWxsSPgAtxU3kjhUcdIXSfzQfLBJZo9SUCjnbfQElyvoNydzs1rKf3pkcO/jQZg2cArYAJgZSB5c5qL4QkXDYq9g==; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22162055564%22%2C%22first_id%22%3A%22182ee18d530d2d-071c5fcc4ef12e4-26021d51-3686400-182ee18d531506%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22rf%22%7D%2C%22%24device_id%22%3A%22182ee18d530d2d-071c5fcc4ef12e4-26021d51-3686400-182ee18d531506%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTgzMDc0NDY2OGEzYy0wYmYxZTY5MzU5NjgyOC0yNjAyMWM1MS0zNjg2NDAwLTE4MzA3NDQ2NjhiMTAyOCIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjE2MjA1NTU2NCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22162055564%22%7D%7D; AWSALB=ddSfpguQ2s8FN2Dklm0ECRUFq2b95cEXEyiAPvoG0bm+GxGECSDF+JjXk9IK/r0xrJAb81MFn4FN0+kZNfZOvwa82Sp8YS/UcGUPXMjE5/T8qiQQFA5JMemxsbo7; AWSALBCORS=ddSfpguQ2s8FN2Dklm0ECRUFq2b95cEXEyiAPvoG0bm+GxGECSDF+JjXk9IK/r0xrJAb81MFn4FN0+kZNfZOvwa82Sp8YS/UcGUPXMjE5/T8qiQQFA5JMemxsbo7',
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
        ('currency', f'{coin.upper()}'),
        ('c', 'cce4e564998c40b189b82daa425c98cc'),
        ('lang', 'ru_RU'),
    )

    response = requests.get('https://www.kucoin.com/_api/currency/currency/chain-info', headers=headers, params=params)

    res = json.loads(response.text)
    for i in res["data"]:
        if i['isDepositEnabled'] == "true" and i['isWithdrawEnabled'] == "true":
            if i.get('preDepositTipEnabled'):
                continue
            else:
                lst.append(i['chainName'].lower())
    return refresh_lst(lst)


if __name__ == '__main__':
    print(kucoin_io("xmr"))

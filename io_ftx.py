import requests, json

from refresh import refresh_lst



def ftx_io(coin):
    headers = {
        'authority': 'ftx.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJ1c2VyfHZsYWRrb3R2aWNraXlAbWFpbC5ydSIsImlzcyI6ImZ0eC5jb20iLCJuYmYiOjE2NjI5MDM1NDAsImV4cCI6MTY2MzE2MjgwMCwiYXVkIjoiaHR0cHM6Ly9mdGV4Y2hhbmdlLmNvbS9hcGkvIiwiaWF0IjoxNjYyOTAzNjAwLCJtZmEiOnRydWUsIm9ubHlBbGxvd1N1cHBvcnRPbmx5IjpmYWxzZSwicmVxdWlyZXNFbWFpbExpbmsiOmZhbHNlLCJ3aXRoZHJhd2Fsc0Rpc2FibGVkIjpmYWxzZSwiaW50ZXJuYWxUcmFuc2ZlcnNEaXNhYmxlZCI6ZmFsc2UsInBlcnNpc3ROZXh0VG9rZW4iOmZhbHNlLCJyZWFkT25seSI6bnVsbCwic2hvcnRFeHBpcnkiOmZhbHNlfQ.g5h2w-5v-sINf1IdMB-fTJRU-yTYsPuKW9C4A_EeHCFynfFbL75Zie8lCcE4NREhktd6JcTSVD2EKJH4wTn27vyK-c-B-RUM-kz0O9YwQTFj_WDqzeMIMyv0rf5vLt1FyBxqzUBCjtLJfLKLferWJIfWRV773YyxXGCuWN9wGKb5glVFVksTE08OSDcEY7ojh89iFbs83zSJoBt94zm2GY3Alv-09qa-EbQRLuOHHN4vO1Z_3Pg71Hiwr-afAOt2fpskcODgrXhM75E4Hq4h_RDo42oB0-cJTnuB9ISdxTatzjDEE0aficjHbtEJXjeT98TEKeeLvl3J95sCoRqYXQ',
        'cache-control': 'max-age=0',
        'cookie': '__stripe_mid=5e4444fd-0871-4a7b-8129-29ab069ae883dd1de1; G_ENABLED_IDPS=google; __stripe_sid=269cfa43-23c0-4498-90a6-63eff2e7950d57752f',
        'ftx-client': 'web',
        'if-none-match': 'W/"0cb82313c1571a15d750505da5a0d03f"',
        'referer': 'https://ftx.com/wallet',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'x-app-v': 'v2.0',
        'x-sardine-session': '2d01a81a-5163-4dcc-a55d-dafeb7f75877',
    }

    response = requests.get('https://ftx.com/api/wallet/coins', headers=headers)
    res = json.loads(response.text)

    for i in res["result"]:
        if i["id"] == f"{coin.upper()}" and i["canDeposit"] == True and i["canWithdraw"] == True:
            return refresh_lst(i["methods"])


if __name__ == '__main__':
    print(ftx_io("trx"))
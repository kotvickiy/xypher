#!/usr/bin/env python3
# pip install requests gspread
import requests, time, gspread

from datetime import datetime

from headers_all import get_json_xypher_all
from cmc_market import verify_cmc
from network import verify_network
from config import TOKEN, CHAT_ID



def lst_coins(val):
    coins = []
    dict_exchanges = {
        "HBG": "https://www.huobi.com/en-us/exchange/",
        "BNC": "https://www.binance.com/en/trade/",
        "KCN": "https://www.kucoin.com/ru/trade/",
        "FTX": "https://ftx.com/trade/",
    }

    for i in val:
        min_A = [999999999, "", i["CoinName"], "_", "usdt"]
        max_B = [0, "", i["CoinName"], "_", "usdt"]
        for k, v in i.items():
            if k[-1] == "A":
                if v < min_A[0]:
                    min_A[0] = v
                    min_A[1] = dict_exchanges.get(k[0:3])
            if k[-1] == "B":
                if v > max_B[0]:
                    max_B[0] = v
                    max_B[1] = dict_exchanges.get(k[0:3])
        spread = round(100 - (min_A[0] * 100 / max_B[0]), 2)
        if spread > 50 or spread < 0.5:
            continue
        if min_A[1]:
            if "huobi" in min_A[1]:
                min_A[2] = i["CoinName"].lower()
            if "binance" in min_A[1]:
                min_A[4] = min_A[4].upper()
            if "kucoin" in min_A[1]:
                min_A[3] = "-"
                min_A[4] = min_A[4].upper()
            if "ftx" in min_A[1]:
                min_A[3] = "/"
                min_A[4] = min_A[4].upper()
        if max_B[1]:
            if "huobi" in max_B[1]:
                max_B[2] = i["CoinName"].lower()
            if "binance" in max_B[1]:
                max_B[4] = max_B[4].upper()
            if "kucoin" in max_B[1]:
                max_B[3] = "-"
                max_B[4] = max_B[4].upper()
            if "ftx" in max_B[1]:
                max_B[3] = "/"
                max_B[4] = max_B[4].upper()
        spread_coin_exchange = [spread, i["CoinName"], f"{min_A[1]}{min_A[2]}{min_A[3]}{min_A[4]}", f"{min_A[0]}", f"{max_B[1]}{max_B[2]}{max_B[3]}{max_B[4]}", f"{max_B[0]}"]
        # print(spread_coin_exchange)
        # print(spread_coin_exchange[1], spread_coin_exchange[2].replace("https://", "").replace("www.", "").split(".")[0], spread_coin_exchange[4].replace("https://", "").replace("www.", "").split(".")[0])
        if verify_cmc(spread_coin_exchange[1], spread_coin_exchange[2].replace("https://", "").replace("www.", "").split(".")[0], spread_coin_exchange[4].replace("https://", "").replace("www.", "").split(".")[0]):
            print(spread_coin_exchange)
            vn = verify_network(spread_coin_exchange[1], spread_coin_exchange[2].replace("https://", "").replace("www.", "").split(".")[0], spread_coin_exchange[4].replace("https://", "").replace("www.", "").split(".")[0])
            print("=====================> ", vn)
            if vn:
                spread_coin_exchange.append(vn)
                if spread_coin_exchange[0] > 2:
                    print(spread_coin_exchange)
                    msg = str(str(spread_coin_exchange[0]) + ' ' + spread_coin_exchange[1] + '\n'\
                            + spread_coin_exchange[3] + ' ' + spread_coin_exchange[2] + '\n'\
                            + spread_coin_exchange[5] + ' ' + spread_coin_exchange[4] + '\n'\
                            + spread_coin_exchange[6] + '\n'
                    )
                    requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage', params=dict(chat_id=CHAT_ID,text=msg, disable_web_page_preview=True))
                coins.append(spread_coin_exchange)
    coins.sort(key=lambda x: x[0], reverse=True)
    return coins


def filling_table(lc, start_num, end_num):
    extend = [[" ", " ", " ", " ", " ", " ", " "]] * (10 - len(lc))
    lc.extend(extend)
    gc = gspread.service_account(filename='./sacc.json')
    sh = gc.open("Test")
    worksheet = sh.sheet1
    worksheet.update(f"B{start_num}:H{end_num}", [[lc[0][0], lc[0][1], lc[0][2], lc[0][3], lc[0][4], lc[0][5], lc[0][6]],
                                                  [lc[1][0], lc[1][1], lc[1][2], lc[1][3], lc[1][4], lc[1][5], lc[1][6]],
                                                  [lc[2][0], lc[2][1], lc[2][2], lc[2][3], lc[2][4], lc[2][5], lc[2][6]],
                                                  [lc[3][0], lc[3][1], lc[3][2], lc[3][3], lc[3][4], lc[3][5], lc[3][6]],
                                                  [lc[4][0], lc[4][1], lc[4][2], lc[4][3], lc[4][4], lc[4][5], lc[4][6]],
                                                  [lc[5][0], lc[5][1], lc[5][2], lc[5][3], lc[5][4], lc[5][5], lc[5][6]],
                                                  [lc[6][0], lc[6][1], lc[6][2], lc[6][3], lc[6][4], lc[6][5], lc[6][6]],
                                                  [lc[7][0], lc[7][1], lc[7][2], lc[7][3], lc[7][4], lc[7][5], lc[7][6]],
                                                  [lc[8][0], lc[8][1], lc[8][2], lc[8][3], lc[8][4], lc[8][5], lc[8][6]],
                                                  [lc[9][0], lc[9][1], lc[9][2], lc[9][3], lc[9][4], lc[9][5], lc[9][6]]])
    

def main():
    start = datetime.now()
    sh = gspread.service_account(filename='./sacc.json').open("Test")
    worksheet = sh.sheet1
    worksheet.format("D1", {"backgroundColor": { "red": 1.0, "green": 0.8, "blue": 0.8}})
    worksheet.update("D1", "О б н о в л е н и е ...")
    l_c_all = lst_coins(get_json_xypher_all())[:10]
    filling_table(l_c_all, 4, 13)
    worksheet.format("D1", {"backgroundColor": { "red": 0.8, "green": 1.0, "blue": 0.8}})
    worksheet.update("D1", f"Обновлено в: {datetime.now().strftime('%H:%M:%S')}")
    print(f"[ + ] {datetime.now().strftime('%d-%m-%Y %H:%M:%S')} {datetime.now() - start}")


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(ex)

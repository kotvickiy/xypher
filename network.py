from io_binance import binance_io
from io_ftx import ftx_io
from io_huobi import huobi_io
from io_kucoin import kucoin_io



def change_ex(ex, coin):
    if ex == "binance":
        return binance_io(coin)
    elif ex == "ftx":
        return ftx_io(coin)
    elif ex == "huobi":
        return huobi_io(coin)
    elif ex == "kucoin":
        return kucoin_io(coin)


def verify_network(coin, ex1, ex2):
    res = ''
    lst = []
    one = change_ex(ex1, coin)
    two = change_ex(ex2, coin)
    for i in one:
        if i in two:
            if i == "erc20":
                continue
            lst.append(i)
    if lst:
        for i in lst:
            res += f"{i} "
        return res[:-1]


if __name__ == '__main__':
    print(verify_network("EGAME", "huobi", "kucoin"))

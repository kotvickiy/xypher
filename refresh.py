def refresh_lst(lst):
    for index, value in enumerate(lst):
        if value == "trx":
            lst[index] = "trc20"
        elif value == "tron (trc20)":
            lst[index] = "trc20"
        elif value == "tron":
            lst[index] = "trc20"
        elif value == "bnb beacon chain (bep2)":
            lst[index] = "bep2"
        elif value == "bnb smart chain (bep20)":
            lst[index] = "bep20"
        elif value == "ethereum (erc20)":
            lst[index] = "erc20"
        elif value == "erc20eth":
            lst[index] = "erc20"
        elif value == "new bitshares":
            lst[index] = "nbs"
        elif value == "decred":
            lst[index] = "dcr"
        elif value == "walton":
            lst[index] = "wtc"
        elif value == "irisnet":
            lst[index] = "iris"
    return lst



if __name__ == '__main__':
    print(refresh_lst(['heco', 'trx', 'bnb smart chain (bep20)', 'tron (trc20)', 'bnb beacon chain (bep2)']))

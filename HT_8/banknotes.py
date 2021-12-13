
import json
from pathlib import Path




change_dict = {}
def rec_change(M, coins_list):
    change_dict[0] = 0
    s = 0
    coins = []

    for i in coins_list:
        for x in i:
            coins.append(int(x))
    for money in range(1, M + 1):
        num_of_coins = float('inf')

        for coin in coins:
            if money >= coin :
                if change_dict[money - coin] + 1 < num_of_coins:
                    num_of_coins = change_dict[money - coin] + 1
                    s = coin

        change_dict[money] = num_of_coins


    return change_dict[M], s

def method(M, coins):
    nums, path = rec_change(M, coins)
    del_bankn = [path]


    while M - path > 0:
        if path == 0:
            raise ValueError("У банка недостатньо коштів для видачі")
        M -= path
        nums, path = rec_change(M, coins)
        del_bankn.append(path)
    del_banknonte(del_bankn)

    return del_bankn

def del_banknonte(nominal):
    print(nominal)
    with open(outpath / "bank_money.json", "r+") as file:
        data_collector = json.load(file)
        for i in data_collector:
            for x in i:
                for y in nominal:
                    if int(x) == y :
                        i[x] -= 1


        file.seek(0,0)
        json.dump(data_collector,file,indent=4)


outpath = Path.cwd()


def start_banknotes(cash):

    with open(outpath / "bank_money.json", "r+") as file:
        data_collector = json.load(file)
        print(data_collector)

        what_we_have = []
        for i in data_collector:
            for x in i:
                if i[x] > 0 and int(x) < cash:
                    what_we_have.append(i)
                    # coins.append(int(x))
        print(what_we_have)


    print(method(cash, what_we_have))

    return True















import json
from pathlib import Path
import sqlite3

ans = []
k = 0
outpath = Path.cwd()

def dict_factory(cursor, row):

    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

con = sqlite3.connect("bank_money")
con.row_factory = dict_factory
cur = con.cursor()

a = cur.execute("SELECT * FROM bank_mon")
print(a)
data2 = cur.fetchall()
data = data2[0]





print(data)

def select_banknotes(money_withdraw):
    print(data)


    A = [int(i) for i in data if data[i] > 0 and int(i) <= money_withdraw]
    print(A)

    k = money_withdraw
    K = money_withdraw
    INF = 10 * 10
    F = [INF] * (K + 1)
    F[0] = 0

    for k in range(1, K + 1):
        for i in range(len(A)):
            if k - A[i] >= 0 and F[k - A[i]] < F[k]:
                F[k] = F[k - A[i]]

        F[k] += 1
    exit = False

    max = sum(int(i) * data[i] for i in data if int(i) < money_withdraw)
    print(max)
    while k != 0 and exit == False:
        for i in range(len(A)):
            if k - A[i] >= 0 and F[k] == F[k - A[i]] + 1:
                if data[str(A[i])] > 0:
                    ans.append(A[i])
                    k -= A[i]
                    data[str(A[i])] -= 1

        print(data)
        print(sum(int(i) * data[i] for i in data if int(i) < money_withdraw))
        check = []
        for i in A:
            if k % i == 0:
                check.append(False)
            else:
                check.append(True)
        print(check)
        if sum(int(i) * data[i] for i in data if int(i) < money_withdraw) < k or all(check) == True:
            con = sqlite3.connect(outpath / "bank_money")
            cur = con.cursor()
            cur.execute(f"""Update bank_money 10,20,50,100,200,500,1000 = {data['10']},{data['20']},
                            {data['50']},{data['100']},{data['200']},{data['500']}{data['1000']} WHERE row = 1""")
            con.commit()
            con.close()
            data.update(data2)
            print(data)
            raise ValueError(f'Банк не може видати таку саму, спробуйте іншу суму')


    print(k)
    print("= ", ans)

    print(data)






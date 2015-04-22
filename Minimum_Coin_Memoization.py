x = int(raw_input())
y = raw_input()
y = y.split(' ')
z = []
for i in range(len(y)):
    z.append(int(y[i]))

def mincoin(total = None, coins = None):
    if total in coins:
        return [total]
    elif max(coins) > total:
        return None
    else:
        min_len = None
        min_cfg = None

        for coin in coins:
            result = mincoin(total = total - coin, coins = coins)
            if result != None:
                if min_len == None or (1 + len(result)) < len(min_cfg):
                    min_cfg = [coin] + result
                    min_len = len(min_cfg)

        return min_cfg

print mincoin(x, z)

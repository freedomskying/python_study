import tushare as ts


# 获取Tushare Token
def getToken():
    with open('D:/tushare_token.txt', 'r') as f:
        token = f.readline()

    return token


if __name__ == '__main__':
    token = getToken()
    print(token)

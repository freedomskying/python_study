import cx_Oracle as oracle


def oraclesql(cursor):
    fp = open(r'/home/oracle/scripts/tablespace.sql')
    fp_sql = fp.read()
    cursor.execute(fp_sql)
    data = cursor.fetchall()
    return data


if __name__ == '__main__':
    ipaddr = "192.168.223.138"
    username = "system"
    password = "redhat"
    oracle_port = "1521"
    oracle_service = "oracle.test"
    try:
        db = oracle.connect(username + "/" + password + "@" + ipaddr + ":" + oracle_port + "/" + oracle_service)
        # 将异常捕捉，然后e就是抛异常的具体内容
    except Exception as e:
        print(e)
    else:
        cursor = db.cursor()
        data = oraclesql(cursor)
        for i in data:
            print(i)
        cursor.close()
        db.close()

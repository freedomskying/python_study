import cx_Oracle as oracle

import networkx as nx
import matplotlib.pyplot as plt


def oraclesql(cursor):
    # fp = open(r'/home/oracle/scripts/tablespace.sql')
    # fp_sql = fp.read()
    fp_sql = 'SELECT A.RECORD_ID, A.ASSOCIATE_ID FROM DW_DOWJ_ASSOCIATIONS_DTL A START WITH RECORD_ID = ''847594'' CONNECT BY NOCYCLE RECORD_ID = PRIOR ASSOCIATE_ID'
    cursor.execute(fp_sql)
    data = cursor.fetchall()
    return data


if __name__ == '__main__':
    ipaddr = "10.100.2.35"
    username = "wluser"
    password = "wluser"
    oracle_port = "1521"
    oracle_service = "ORCLPDB"

    dg = nx.DiGraph()

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

        print(list(set(list(data[0]) + list(data[1]))))
        print(list(data[1]))
        print(list(data[0]))
        print(data)
        dg.add_nodes_from(list(set(list(data[0]) + list(data[1]))))

        dg.add_edges_from(data)

        nx.draw(dg, with_labels=True, node_size=900, node_color='green')
        plt.show()

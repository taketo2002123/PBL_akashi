import MySQLdb
 
def db_sample():
    """ 接続サンプル """
 
    # 接続する 
    con = MySQLdb.connect(
            user='root',
            passwd='20020123aA',
            host='localhost',
            db='ファン',
            charset="utf8")
 
    # カーソルを取得する
    cur= con.cursor()
     
    # クエリを実行する
    sql =  '''
    CREATE TABLE fan(
       id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(50) NULL,
       password VARCHAR(300) NULL,
       gender ENUM('F','M')
    )'''
    cur.execute(sql)
 
    cur.execute("SHOW TABLES")
    print(cur.fetchall())

    cur.close()
    con.close()
 
if __name__ == "__main__":
    db_sample()
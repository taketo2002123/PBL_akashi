import MySQLdb
 
def db_sample():
    """ 接続サンプル """
 
    # 接続する 
    con = MySQLdb.connect(
            user='root',
            passwd='20020123aA',
            host='localhost',
            db='popular',
            charset="utf8")
 
    # カーソルを取得する
    cur= con.cursor()
     
    # クエリを実行する
    sql =  '''
    CREATE TABLE popular(
       id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(50) NULL,
       password VARCHAR(300) NULL,
       gender ENUM('F','M'),
       columm VARCHAR(50) NULL
    )'''
    cur.execute(sql)
 
    cur.execute("SHOW TABLES")
    print(cur.fetchall())

    cur.close()
    con.close()
 
if __name__ == "__main__":
    db_sample()
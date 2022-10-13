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
    cur.execute("""INSERT INTO student(first_name,last_name,birthday,gender)
        VALUES('akashi','taketo','20020123','F')
    """)
 
    cur.execute("SELECT * FROM student")
    for row in cur:
        print(row)

    # 保存を実行
    con.commit()
 
# 接続を閉じる
    con.close()
if __name__ == "__main__":
    db_sample()    
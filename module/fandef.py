import MySQLdb
from werkzeug.security import generate_password_hash as gph
from werkzeug.security import check_password_hash as cph
def db_sample(username,password,sexual,secret):
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
    cur.execute("""SELECT * FROM fan WHERE name=%s AND gender=%s
    """
    ,(username,sexual))
    data=[]
    cash=cur
    for row in cur:
        data.append(row)
    if len(data)!=0:
        return True 
    # クエリを実行する
    if len(secret)<4:
        return True

    cur.execute("""INSERT INTO fan(name,password,gender)
        VALUES(%s,%s,%s)
    """
    ,(username,password,sexual))
 
    

    # 保存を実行
    con.commit()
    return False
def db_select(username,password,sexual):
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
    cur.execute("""SELECT * FROM fan WHERE name=%s AND gender=%s
    """
    ,(username,sexual))
    flag=False
    cash=0
    for row in cur:
        print(row[2])
        flag=cph(row[2],password)
        cash=row
       

    # 保存を実行
    con.commit() 
# 接続を閉じる
    con.close()
    return flag,cash 


def fan_popular_db_select(username,sexual,columm):
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
    if username==None:
        if sexual==None:
            if columm==None:
                cur.execute("""SELECT * FROM popular 
                """)
            else:
                cur.execute("""SELECT * FROM popular WHERE  columm=%s
                """
                ,(columm,))
        else:
            if columm==None:
                cur.execute("""SELECT * FROM popular WHERE  gender=%s 
                """
                ,(sexual,))
            else:
                cur.execute("""SELECT * FROM popular WHERE gender=%s AND columm=%s
                """
                ,(sexual,columm))           
              


    # クエリを実行する
    else:
        if sexual==None:
            if columm==None:
                cur.execute("""SELECT * FROM popular WHERE name=%s
                """
                ,(username,))
            else:
                cur.execute("""SELECT * FROM popular WHERE name=%s AND columm=%s
                """
                ,(username,columm))
        else:
            if columm==None:
                cur.execute("""SELECT * FROM popular WHERE name=%s AND gender=%s 
                """
                ,(username,sexual))
            else:
                cur.execute("""SELECT * FROM popular WHERE name=%s AND gender=%s AND columm=%s
                """
                ,(username,sexual,columm))
    
    cash=cur 
    
       
    # 保存を実行
    con.commit() 
# 接続を閉じる
    con.close()
    return cash 
def columm_popular_db_select_comment(columm):
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
    if columm==None:
        cur.execute("""SELECT * FROM comment """)
    else :
        cur.execute("""SELECT * FROM comment WHERE columm=%s 
                """
                ,(columm,))   
    cash=cur 
    
       
    # 保存を実行
    con.commit() 
# 接続を閉じる
    con.close()
    return cash                      

def fan_popular_db_select_comment(username):
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
    print(username)
    
    cur.execute("""SELECT * FROM comment WHERE poster=%s 
                """
                ,(username,))
       
       
    
    cash=cur 
    
       
    # 保存を実行
    con.commit() 
# 接続を閉じる
    con.close()
    return cash   
def fan_db_upload(name,username,password,sexual,secret)  :
    # 接続する 
    con = MySQLdb.connect(
            user='root',
            passwd='20020123aA',
            host='localhost',
            db='ファン',
            charset="utf8")
 
    # カーソルを取得する
    cur= con.cursor()
    if len(secret)<4:
        return True
     
    # クエリを実行する
    cur.execute("""UPDATE  fan SET name=%s , password=%s , gender=%s   WHERE name=%s 
    """
    ,(username,password,sexual,name))
    con.commit()      
    return False
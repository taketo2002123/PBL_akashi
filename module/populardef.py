import MySQLdb
from werkzeug.security import generate_password_hash as gph
from werkzeug.security import check_password_hash as cph
def popular_db_sample(username,password,sexual,columm,secret):
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
    cur.execute("""SELECT * FROM popular WHERE name=%s AND gender=%s
    """
    ,(username,sexual))
    data=[]
    for row in cur:
        data.append(row)
    if len(data)!=0:
        return True   
    if len(secret)<4:
        return True     
    # クエリを実行する
    cur.execute("""INSERT INTO popular(name,password,gender,columm)
        VALUES(%s,%s,%s,%s)
    """
    ,(username,password,sexual,columm))
 
    

    # 保存を実行
    con.commit()
    return False
def popular_db_select(username,password,sexual):
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
    cur.execute("""SELECT * FROM popular WHERE name=%s AND gender=%s
    """
    ,(username,sexual))
 
    for row in cur:
        print(row[2])
        flag=cph(row[2],password)
        cash=row
    return flag,cash   
def popular_db_upload(name,username,password,sexual,columm)  :
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
    cur.execute("""UPDATE  popular SET name=%s , password=%s , gender=%s , columm=%s WHERE name=%s 
    """
    ,(username,password,sexual,columm,name))
    con.commit()

def popular_db_comment(name,columm,comment,file,title):
    con = MySQLdb.connect(
            user='root',
            passwd='20020123aA',
            host='localhost',
            db='popular',
            charset="utf8")
 
    # カーソルを取得する
    cur= con.cursor()
     
    # クエリを実行する
    print(name,columm,comment,file,title)
    cur.execute("""INSERT INTO comment(title,comment,image,poster,columm)
    VALUES(%s,%s,%s,%s,%s)
    """
    ,(title,comment,file,name,columm))
     # 保存を実行
    con.commit()

def popular_db_comment2(id):
    con = MySQLdb.connect(
            user='root',
            passwd='20020123aA',
            host='localhost',
            db='popular',
            charset="utf8")
 
    # カーソルを取得する
    cur= con.cursor()
     
   
    cur.execute('''
    DELETE 
    FROM    comment
    WHERE   id = %s
    '''
    ,(id))
     # 保存を実行
    con.commit()
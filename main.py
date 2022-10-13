from flask import Flask, render_template, redirect,send_file,request,session,jsonify
import MySQLdb
from werkzeug.security import generate_password_hash as gph
from werkzeug.security import check_password_hash as cph
from datetime import timedelta
import secrets
import html
def db_sample(username,password,sexual):
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
    for row in cur:
        data.append(row)
    if len(data)!=0:
        return True    
    # クエリを実行する
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
 
    for row in cur:
        print(row[2])
        flag=cph(row[2],password)
        cash=row
       

    # 保存を実行
    con.commit() 
# 接続を閉じる
    con.close()
    return flag,cash 
def popular_db_sample(username,password,sexual,columm):
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
    # クエリを実行する
    cur.execute("""INSERT INTO popular(name,password,gender,columm)
        VALUES(%s,%s,%s,%s)
    """
    ,(username,password,sexual,columm))
 
    

    # 保存を実行
    con.commit()
    return False
def popular_db_select(username,password,sexual,columm):
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
       

    # 保存を実行
    con.commit() 
# 接続を閉じる
    con.close()
    return flag,cash 
        
app=Flask(__name__)
app.secret_key=secrets.token_urlsafe(16)
app.permanant_session_lifetime=timedelta(minutes=60)
@app.route('/')
def hello_world():
    return redirect('/title')
@app.route('/title')    
def hello_newworld():
    return render_template('title.html')   
   
@app.route('/fannewlogin')
def temple():    
    return render_template('fannewlogin.html')
@app.route('/fannewloginok',methods=['POST'])
def result():
    username=request.form['user'] 
    password=gph(request.form['pass'])
    sexual=request.form['sel']
    flag=db_sample(username,password,sexual)
    if flag:
        return redirect('fannewloginng')  
    return render_template('fannewloginok.html',user=username,word=password,sex=sexual)
@app.route('/fannewloginng')
def ng():
    return render_template('newNG.html')
@app.route('/fanlogin')
def login():    
    return render_template('fanlogin.html',name='赤司岳與',age='20')    
@app.route('/fanloginok',methods=['POST'])
def loginok():
    username=request.form['user'] 
    password=request.form['pass']
    sexual=request.form['sel']
    flag,cash=db_select(username,password,sexual)
    if flag:
        session['id']=cash[0]
        session['name']=cash[1]
        session['password']=cash[2]
        session['sex']=cash[3]
        print(session['id'])       
        return redirect('fanhome')    
    else:
        return redirect('fanloginng') 

@app.route('/fanloginng')
def loginng():
    return render_template('fanNG.html')
        
       
@app.route('/fanhome',methods=['GET'])
def home(): 
    if 'name' in session:
        return render_template('fanhome.html',
                                name=html.escape(session['name']),
                                sex=html.escape(session['sex']))
    else:
        return redirect('title')                            
@app.route('/send',methods=['GET'])
def send():
    dic={}
    dic['id']= session['id']
    dic['name']= session['name']
    dic['password']= session['password']
    dic['sex']= session['sex']
    return jsonify(dic)


#ここまでファンの機能
@app.route('/image')
def dounload():    
    return send_file("success.jpg")   
#ここから有名人の機能
@app.route('/popularnewlogin')
def populartemple():    
    return render_template('popularnewlogin.html')
@app.route('/popularnewloginok',methods=['POST'])
def popularresult():
    username=request.form['user'] 
    password=gph(request.form['pass'])
    sexual=request.form['sel']
    columm=request.form['col']
    flag=popular_db_sample(username,password,sexual,columm)
    if flag:
        return redirect('popularnewloginng')  
    return render_template('popularnewloginok.html',user=username,word=password,sex=sexual,columm=columm)
@app.route('/popularnewloginng')
def popularng():
    return render_template('newNG.html')
@app.route('/popularlogin')
def popularlogin():    
    return render_template('popularlogin.html',name='赤司岳與',age='20')    
@app.route('/popularloginok',methods=['POST'])
def popularloginok():
    username=request.form['user'] 
    password=request.form['pass']
    sexual=request.form['sel']
    columm=request.form['col']
    flag,cash=popular_db_select(username,password,sexual,columm)
    if flag:
        session['id']=cash[0]
        session['name']=cash[1]
        session['password']=cash[2]
        session['sex']=cash[3]
        session['columm']=cash[4]
        print(session['id'])       
        return redirect('popularhome')    
    else:
        return redirect('popularloginng') 

@app.route('/popularloginng')
def popularloginng():
    return render_template('popularNG.html')
        
       
@app.route('/popularhome',methods=['GET'])
def popularhome(): 
    if 'name' in session:
        return render_template('popularhome.html',
                                name=html.escape(session['name']),
                                sex=html.escape(session['sex']),
                                columm=html.escape(session['columm']))
    else:
        return redirect('title')      
if __name__=='__main__':
    app.run(host='0.0.0.0')

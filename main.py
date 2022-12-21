from flask import Flask, render_template, redirect,send_file,request,session,jsonify
import MySQLdb
from werkzeug.security import generate_password_hash as gph
from werkzeug.security import check_password_hash as cph
from datetime import timedelta
import secrets
import html
import module.populardef as pd
import module.fandef as fd
import os
# request フォームから送信した情報を扱うためのモジュール
# redirect  ページの移動
# url_for アドレス遷移
from flask import Flask, request, redirect, url_for
# ファイル名をチェックする関数
from werkzeug.utils import secure_filename
# 画像のダウンロード
from flask import send_from_directory       
def allwed_file(filename):
    # .があるかどうかのチェックと、拡張子の確認
    # OKなら１、だめなら0
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
      
app=Flask(__name__)

app.secret_key=secrets.token_urlsafe(16)
app.permanant_session_lifetime=timedelta(minutes=60)

# アップロードされる拡張子の制限
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])

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
    secret='*'*len(request.form['pass'])
    flag=fd.db_sample(username,password,sexual,secret)
    if flag:
        return redirect('fannewloginng') 
    else: 
 
        return render_template('fannewloginok.html',user=username,word=secret,sex=sexual)
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
    flag,cash=fd.db_select(username,password,sexual)
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
@app.route('/fanlogout',methods=['GET'])
def fanlogout():
    session.clear()
    return redirect('title') 
@app.route('/fanindex',methods=['GET'])
def fanindex():
    return render_template('fanindex.html')
@app.route('/fanindexok',methods=['POST'])
def fanindexok():

    username=request.form['user'] 
    sexual=request.form['sel']
    columm=request.form['col']
    if len(username)==0:
        username=None
    if sexual=='None':
        sexual=None
    if columm=="None":
        columm=None        
    print(username,sexual,columm)
    cash=fd.fan_popular_db_select(username,sexual,columm)
    member=[]
    for i in cash:
        member.append([i[1],i[3],i[4]])
    print(member)
    session['member']=member
    if len(member)==0:
        return render_template('fanindexng.html') 
    else:    
        return render_template('fanindexok.html', arr=member)
@app.route('/fanindexComment',methods=['POST'])
def fanindexComment():

    username=request.form['user_name'] 
    
    if len(username)==0:
        username=None
    cash=fd.fan_popular_db_select_comment(username)
    member=[]
    for i in cash:
        member.append([i[1],i[2],i[3],i[4],i[5]])
    print(member)
    if len(member)==0:
        return render_template('fanindexng.html') 
    else:    
        return render_template('fanindexcomment.html', name=username,arr=member)  
@app.route('/collumindex',methods=['GET'])
def collumindex(): 
    return render_template('colummindex.html') 
@app.route('/collumindexcomment',methods=['POST'])
def collumindexok():  
    columm=request.form['col']
    if columm=="None":
        columm=None   
    cash=fd.columm_popular_db_select_comment(columm)
    member=[]
    for i in cash:
        member.append([i[1],i[2],i[3],i[4],i[5]])
    print(member)
    if len(member)==0:
        return render_template('fanindexng.html') 
    else:    
        return render_template('colummindexcomment.html', arr=member)    
           
@app.route('/fanupload',methods=['GET'])   
def fanupload():
    return render_template('fanupload.html')     
@app.route('/fanuploadfunction',methods=['POST'])   
def fanuploadfunction():
    username=request.form['user'] 
    password=gph(request.form['pass'])
    sexual=request.form['sel']
    print(session['name'])
    name=session['name']
    secret='*'*len(request.form['pass'])
    flag=fd.fan_db_upload(name,username,password,sexual,secret)
    if flag:
        return redirect('newNG')  
    return render_template('fanuploadok.html',user=username,word=secret,sex=sexual)
@app.route('/popularnamesend',methods=['POST'])   
def popularnamesend():
    mylist=session['member']
    print(mylist)
    dic=[]
    for i in mylist:
        dic.append({
            'name': i[0] if len(i) > 0 else '',
            'sex': i[1] if len(i) > 1 else '',
            'columm': i[2] if len(i) > 2 else ''
        })
    
    
    return jsonify(dic)
 
#ここまでファンの機能   
'''
ファンの機能
ファンの機能
ファンの機能
ファンの機能
'''
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
    secret='*'*len(request.form['pass'])
    flag=pd.popular_db_sample(username,password,sexual,columm,secret)
    if flag:
        return redirect('popularnewloginng')  
    return render_template('popularnewloginok.html',user=username,word=secret,sex=sexual,columm=columm)
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
    secret='*'*len(request.form['pass'])
    flag,cash=pd.popular_db_select(username,password,sexual)
    if flag:
        session['id']=cash[0]
        session['name']=cash[1]
        session['password']=secret
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
@app.route('/popularcomment',methods=['GET'])   
def popularcomment():     
    return render_template('popularcomment.html')
@app.route('/popularcommentok',methods=['POST'])   
def popularcommentok():     
    comment=request.form['comment'] 
    columm=request.form['col'] 
    file=request.files['file']
    name=session['name']
    UPLOAD_FOLDER = './static/images/'+ name
    if not os.path.exists(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    if file and allwed_file(file.filename):
        # 危険な文字を削除（サニタイズ処理）
        filename = secure_filename(file.filename)
            # ファイルの保存
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # アップロード後のページに転送
            
    
    title=request.form['title']
    pd.popular_db_comment(name,columm,comment,filename,title)
    return render_template('popularcommentok.html',
                            comment=comment ,
                            columm=columm ,
                            file=filename,
                            name=name,
                            title=title)  
@app.route('/popularupload',methods=['GET'])   
def popularupload():
    return render_template('popularupload.html')     
@app.route('/popularuploadfunction',methods=['POST'])   
def popularuploadfunction():
    username=request.form['user'] 
    password=gph(request.form['pass'])
    sexual=request.form['sel']
    columm=request.form['col']
    print(session['name'])
    name=session['name']
    secret='*'*len(request.form['pass'])
    flag=pd.popular_db_upload(name,username,password,sexual,columm)
    if flag:
        return redirect('popularnewNG')  
    return render_template('popularuploadok.html',user=username,word=secret,sex=sexual,columm=columm)
        
@app.route('/populardelete',methods=['GET'])   
def populardelete():
    username=session['name']
    if len(username)==0:
        username=None
    cash=fd.fan_popular_db_select_comment(username)
    member=[]
    for i in cash:
        member.append([i[0],i[1],i[2],i[3],i[4],i[5]])
    print(member)
    if len(member)==0:
        return render_template('fanindexng.html') 
    else:    
        return render_template('populardelete.html',name=username, arr=member)
@app.route('/populardeletefunction',methods=['POST'])   
def populardeletefunction():
    id=request.form['id']
    print(id)
    pd.popular_db_comment2(id)
    return render_template('populardeleteok.html') 


@app.route('/popularlogout',methods=['GET'])   
def popularlogout(): 
    session.clear()
    return redirect('title')                         
if __name__=='__main__':
    app.run(host="0.0.0.0", port=int("5000"),debug=True)

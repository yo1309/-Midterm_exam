from flask import Flask, session, abort, url_for, redirect, request, render_template, redirect
import logdb, random

app = Flask(__name__)
app.secret_key = b'aaa!111/'

######################로그인전(세션 x)########################
#메인 페이지
@app.route('/')
def index():
    return render_template('main.html')

#로그인
@app.route('/login')
def login():
    return render_template('login.html')

    
@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return 'GET으로 전송이다'
    else:
        id = request.form['id']
        pw = request.form['pw']
        ret = logdb.select_users(id,pw)
        if ret != None:
            session['users'] = id
            return '''<script>alert("로그인 성공!");
        location.href="/"
        </script>
        '''

        else:
            return "아이디나 패스워드가 틀렸습니다."

# 회원가입
@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'GET':
        return render_template('join.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        name = request.form['name']
        logdb.insert_data(id,pw,name)
        return '''<script>alert("회원가입을 축하드립니다!");
        location.href="/"
        </script>
        '''

##################로그인을 할 시에(세션 o)##########################

#회원된 유저정보들
@app.route('/member')
def member():
    if 'users' in session:
        info = logdb.select_all()
        return render_template("showlog.html", data=info)
    else:
        return '''
        <script>alert("로그인을 해야합니다!");
        location.href="/login"
        </script>
        '''

#게임
@app.route("/startGame")
def start():
    if 'users' in session:
        return render_template('game.html')
    else:
        return '''
        <script>alert("로그인 후 이용해주세요!");
        location.href="/login"
        </script>
        '''

@app.route('/playGame', methods=['POST'])
def play():
    if request.method == 'POST':
        name = request.form['suspect']
        print(name)         #내가 지목한 범인 콘솔창에 출력
        with open("static/save.txt","w",encoding='utf-8') as f:
            f.write("%s" % (name))
        return render_template('sure.html', data=name)

@app.route("/image")
def image():
    return render_template('image.html')


@app.route('/result')
def result():
    people = ['도둑', '경찰', '평민', '의사']
    t_suspect = ("%s" % random.choice(people))

    with open("static/test.txt","w",encoding='utf-8') as f:
        f.write("%s" % t_suspect)
    
    with open("static/test.txt","r",encoding='utf-8') as file:      #진짜 범인 파일
        result_suspect = file.read()

    with open("static/save.txt", "r",encoding='utf-8') as file:     #내가 지목한 범인 파일
        p_suspect = file.read()

    print(t_suspect)        #콘솔창 진짜 범인 출력
    
    if result_suspect == p_suspect:
        return render_template('image.html')
    else:
        return render_template('fail.html', data_1= t_suspect, data_2 = p_suspect)
 


#로그 아웃(session 제거)
@app.route('/logout')
def logout():
    session.pop('users', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

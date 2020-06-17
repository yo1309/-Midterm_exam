from flask import Flask, render_template, url_for, request
import random

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/startGame")
def start():
    return render_template('game.html')
    
@app.route('/method', methods=['POST'])
def method():
    if request.method == 'POST':
        name = request.form['suspect']
        print(name)
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
    
    with open("static/test.txt","r",encoding='utf-8') as file:
        result_suspect = file.read()

    with open("static/save.txt", "r",encoding='utf-8') as file:
        p_suspect = file.read()

    if result_suspect == p_suspect:
        return render_template('image.html')
    else:
        return '꽝...당신이 지목한 범인:{}'.format(p_suspect)
 

@app.route('/data')
def data():
    return render_template()
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://sparta:test@cluster0.oloy3yg.mongodb.net/?retryWrites=true&w=majority', tlsCAFile = ca)
db = client.dbsparta

# 리스트 목록
@app.route('/')
def home():
   return render_template('index_list.html')

# 기호님 주소
@app.route('/index_이기호.html')
def ho_page():
    return render_template('index_이기호.html')
# 개인서버로 저장
@app.route("/index_ho", methods=["POST"])
def ho_post():
    detail_receive = request.form['detail_give']
    description_receive = request.form['description_give']

    doc = {
        'name':detail_receive,
        'comment':description_receive
    } 
    db.team_ho.insert_one(doc)

    return jsonify({'msg': '저장완료!'})

# 솔님 주소
@app.route('/index_이솔.html')
def sol_page():
    return render_template('index_이솔.html')
# 개인서버로 저장
@app.route("/index_sol", methods=["POST"])
def sol_post():
    detail_receive = request.form['detail_give']
    description_receive = request.form['description_give']

    doc = {
        'name':detail_receive,
        'comment':description_receive
    } 
    db.team_sol.insert_one(doc)

    return jsonify({'msg': '저장완료!'})

# 정규 주소
@app.route('/index_김정규.html')
def gyu_page():
    return render_template('index_김정규.html')
# 개인서버로 저장
@app.route("/index_gyu", methods=["POST"])
def gyu_post():
    detail_receive = request.form['detail_give']
    description_receive = request.form['description_give']

    doc = {
        'name':detail_receive,
        'comment':description_receive
    } 
    db.team_gyu.insert_one(doc)

    return jsonify({'msg': '저장완료!'})


# 제욱님 주소
@app.route('/index_이제욱.html')
def wook_page():
    return render_template('index_이제욱.html')
# 개인서버로 저장
@app.route("/index_wook", methods=["POST"])
def wook_post():
    detail_receive = request.form['detail_give']
    description_receive = request.form['description_give']

    doc = {
        'name':detail_receive,
        'comment':description_receive
    } 
    db.team_wook.insert_one(doc)

    return jsonify({'msg': '저장완료!'})


if __name__ == '__main__':

    app.run('0.0.0.0', port=5000, debug=True)
# install 안했음 코드수정 테스트


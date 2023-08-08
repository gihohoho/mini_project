from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://sparta:test@cluster0.oloy3yg.mongodb.net/?retryWrites=true&w=majority', tlsCAFile = ca)
db = client.dbsparta

# 메인 index
@app.route('/')
def home():
   return render_template('index_list.html')

# 기호님 주소
@app.route('/index_이기호.html')
def ho_page():
    return render_template('index_이기호.html')

# 솔님 주소
@app.route('/index_이솔.html')
def sol_page():
    return render_template('index_이솔.html')

# 정규 주소
@app.route('/index_김정규.html')
def gyu_page():
    return render_template('index_김정규.html')

# 제욱님 주소
@app.route('/index_이제욱.html')
def wook_page():
    return render_template('index_이제욱.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
# install 안했음 코드수정 테스트
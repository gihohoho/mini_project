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
# 저장 기능
@app.route("/index_ho", methods=["POST"])
def ho_post():
    detail_receive = request.form['detail_give']
    description_receive = request.form['description_give']

    if detail_receive == "" :
        return jsonify({'msg': '목록을 입력해 주세요!'})
    elif description_receive == "" :
        return jsonify({'msg': '목록의 내용을 입력해 주세요!'})
    else :
        doc = {
            'detail':detail_receive,
            'description':description_receive
        } 
        db.team_ho.insert_one(doc)

        return jsonify({'msg': '저장완료!'})
# 수정 기능
@app.route("/index_ho_update", methods=["POST"])
def ho_ud_post():
    ud_detail_receive = request.form['ud_detail_give']
    ud_description_receive = request.form['ud_description_give']

    if ud_detail_receive == "" :
        return jsonify({'msg': '수정할 목록을 입력해 주세요!'})
    elif ud_description_receive == "" :
        return jsonify({'msg': '수정 내용을 입력해 주세요!'})
    elif list(db.team_ho.find({ 'detail' : ud_detail_receive })) == []:
        return jsonify({'msg': '입력하신 목록은 없습니다. 다시 입력해 주세요!'})
    else :
        db.team_ho.update_one({'detail': ud_detail_receive},{'$set':{'description':ud_description_receive}})

        return jsonify({'msg': '수정완료!'})


# ho 서버에 저장한 정보 가져오기
@app.route('/index_ho', methods=['GET'])
def read_ho():
    info = list(db.team_ho.find({}, {'_id': False}))
    return jsonify({'info_ho': info})


# ho 서버에서 정보 삭제하기
@app.route('/index_ho/delete', methods=['POST'])
def delete_info_ho():
    detail_receive = request.form['detail_give']
    db.team_ho.delete_one({'detail': detail_receive})
    return jsonify({'msg': '삭제 완료!'})


# 솔님 주소
@app.route('/index_이솔.html')
def sol_page():
    return render_template('index_이솔.html')
# 저장 기능
@app.route("/index_sol", methods=["POST"])
def sol_post():
    detail_receive = request.form['detail_give']
    description_receive = request.form['description_give']

    if detail_receive == "" :
        return jsonify({'msg': '목록을 입력해 주세요!'})
    elif description_receive == "" :
        return jsonify({'msg': '목록의 내용을 입력해 주세요!'})
    else :
        doc = {
            'detail':detail_receive,
            'description':description_receive
        } 
        db.team_sol.insert_one(doc)

        return jsonify({'msg': '저장완료!'})
# 수정 기능
@app.route("/index_sol_update", methods=["POST"])
def sol_ud_post():
    ud_detail_receive = request.form['ud_detail_give']
    ud_description_receive = request.form['ud_description_give']

    if ud_detail_receive == "" :
        return jsonify({'msg': '수정할 목록을 입력해 주세요!'})
    elif ud_description_receive == "" :
        return jsonify({'msg': '수정 내용을 입력해 주세요!'})
    elif list(db.team_sol.find({ 'detail' : ud_detail_receive })) == []:
        return jsonify({'msg': '입력하신 목록은 없습니다. 다시 입력해 주세요!'})
    else :
        db.team_sol.update_one({'detail': ud_detail_receive},{'$set':{'description':ud_description_receive}})

        return jsonify({'msg': '수정완료!'})

# sol 서버에 저장한 정보 가져오기
@app.route('/index_sol', methods=['GET'])
def read_sol():
    info = list(db.team_sol.find({}, {'_id': False}))
    return jsonify({'info_sol': info})


# sol 서버에서 정보 삭제하기
@app.route('/index_sol/delete', methods=['POST'])
def delete_info_sol():
    detail_receive = request.form['detail_give']
    db.team_sol.delete_one({'detail': detail_receive})
    return jsonify({'msg': '삭제 완료!'})

# 정규 주소
@app.route('/index_김정규.html')
def gyu_page():
    return render_template('index_김정규.html')
# 저장 기능
@app.route("/index_gyu", methods=["POST"])
def gyu_post():
    detail_receive = request.form['detail_give']
    description_receive = request.form['description_give']

    if detail_receive == "" :
        return jsonify({'msg': '목록을 입력해 주세요!'})
    elif description_receive == "" :
        return jsonify({'msg': '목록의 내용을 입력해 주세요!'})
    else :
        doc = {
            'detail':detail_receive,
            'description':description_receive
        } 
        db.team_gyu.insert_one(doc)

        return jsonify({'msg': '저장완료!'})
# 수정 기능
@app.route("/index_gyu_update", methods=["POST"])
def gyu_ud_post():
    ud_detail_receive = request.form['ud_detail_give']
    ud_description_receive = request.form['ud_description_give']

    if ud_detail_receive == "" :
        return jsonify({'msg': '수정할 목록을 입력해 주세요!'})
    elif ud_description_receive == "" :
        return jsonify({'msg': '수정 내용을 입력해 주세요!'})
    elif list(db.team_gyu.find({ 'detail' : ud_detail_receive })) == []:
        return jsonify({'msg': '입력하신 목록은 없습니다. 다시 입력해 주세요!'})
    else :
        db.team_gyu.update_one({'detail': ud_detail_receive},{'$set':{'description':ud_description_receive}})

        return jsonify({'msg': '수정완료!'})

# gyu 서버에 저장한 정보 가져오기
@app.route('/index_gyu', methods=['GET'])
def read_gyu():
    info = list(db.team_gyu.find({}, {'_id': False}))
    return jsonify({'info_gyu': info})


# gyu 서버에서 정보 삭제하기
@app.route('/index_gyu/delete', methods=['POST'])
def delete_info_gyu():
    detail_receive = request.form['detail_give']
    db.team_gyu.delete_one({'detail': detail_receive})
    return jsonify({'msg': '삭제 완료!'})


# 제욱님 주소
@app.route('/index_이제욱.html')
def wook_page():
    return render_template('index_이제욱.html')
# 저장 기능
@app.route("/index_wook", methods=["POST"])
def wook_post():
    detail_receive = request.form['detail_give']
    description_receive = request.form['description_give']

    if detail_receive == "" :
        return jsonify({'msg': '목록을 입력해 주세요!'})
    elif description_receive == "" :
        return jsonify({'msg': '목록의 내용을 입력해 주세요!'})
    else :
        doc = {
            'detail':detail_receive,
            'description':description_receive
        } 
        db.team_wook.insert_one(doc)

        return jsonify({'msg': '저장완료!'})
# 수정 기능
@app.route("/index_wook_update", methods=["POST"])
def wook_ud_post():
    ud_detail_receive = request.form['ud_detail_give']
    ud_description_receive = request.form['ud_description_give']

    if ud_detail_receive == "" :
        return jsonify({'msg': '수정할 목록을 입력해 주세요!'})
    elif ud_description_receive == "" :
        return jsonify({'msg': '수정 내용을 입력해 주세요!'})
    elif list(db.team_wook.find({ 'detail' : ud_detail_receive })) == []:
        return jsonify({'msg': '입력하신 목록은 없습니다. 다시 입력해 주세요!'})
    else :
        db.team_wook.update_one({'detail': ud_detail_receive},{'$set':{'description':ud_description_receive}})

        return jsonify({'msg': '수정완료!'})

# 서버에 저장한 정보 가져오기
@app.route('/index_wook', methods=['GET'])
def read_wook():
    info = list(db.team_wook.find({}, {'_id': False}))
    return jsonify({'info_wook': info})


# 서버에서 정보 삭제하기
@app.route('/index_wook/delete', methods=['POST'])
def delete_info_wook():
    detail_receive = request.form['detail_give']
    db.team_wook.delete_one({'detail': detail_receive})
    return jsonify({'msg': '삭제 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

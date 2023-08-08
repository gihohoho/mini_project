from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('')
db = client.dbsparta

# install 안했음 코드수정 테스트
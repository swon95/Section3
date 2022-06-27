# __init__.py = 파이썬 패키지임을 선언

from flask import Flask
import pickle

# Flask 인스턴스 생성
Project = Flask(__name__) # __ = 더블 언더스코어 == 던더

# if __name__ == '__main__':
#     Project.run(debug=True)   # 비어있는 내용

# 웹에 표현하기 위해 route 메소드 사용
# @ 가 붙는 이유 = decorator(장식자)를 나타냄
# Flask 에서는 장식자가 URL 연결에 활용됨
# 장식자를 사용하면 다음 행의 함수부터 장식자가 적용됨.

with open("D:\CodeStates\Section3\project\model.pkl", "rb") as mp:
    odf2 = pickle.load(mp)

@Project.route('/') # 127.0.0.1:5000 + / = 127.0.0.1:5000/
def index():
    return 'Hello World!'
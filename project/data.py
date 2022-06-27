# import requests
# from bs4 import BeautifulSoup

# response = requests.request('GET', 'https://www.forbes.com/advisor/travel-rewards/top-50-best-places-to-visit/')
# # print(response) # 응답코드 200 번 확인
# # breakpoint()

# soup = BeautifulSoup(response.content, 'html.parser') # print(soup) # 웹 페이지 구성 확인
# # print(soup.title) # Top 50 Best Places To Travel Post-Pandemic
# # print(soup.find)
# # breakpoint()

# def Places_name():

#   name = soup.find_all('h2')
#   name_list = []

#   for a in name:
#     name_list.append(a.get_text())

#   return name_list
# print(Places_name())
# # breakpoint()
# def spot():
#     response = requests.request('GET', 'https://photoguide.com/452')
#     soup = BeautifulSoup(response.content, 'html.parser')

#     name = soup.select('strong > span')

#     name_list = []

#     for a in name:
#         name_list.append(a.get_text())
#     return name_list
# print(spot())
# breakpoint()

# def spot():
#   response = requests.request('GET', 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503771%2C2503781%2C4258168%2C4270442%2C4284970%2C4291517%2C4306835%2C4515404%2C4597339%2C4649665%2C4703207%2C4718357%2C4722900%2C4723331%2C4741664%2C4757164%2C4758194%2C4758493%2C4762561%2C4779784%2C4786958%2C4787395%2C4790928%2C4794648%2C4797697%2C4800879%2C4806994%2C4807468&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0hsqf&dest_state_type=sattd&dest_src=ts&q=%EC%82%AC%EC%A7%84%EC%B0%8D%EA%B8%B0%20%EC%A2%8B%EC%9D%80%20%EC%9E%A5%EC%86%8C%5C&sa=X&ved=2ahUKEwji6Kjnl8T4AhXSfXAKHZVaCZEQuL0BegQIURA4')
#   soup = BeautifulSoup(response.content, 'html.parser')

#   name = soup.find_all('div', class_='skFvHc YmWhbc')
#   name_list = []

#   for a in name:
#     name_list.append(a.get_text())
#   return name_list
# print(spot())

# def review():
#   response = requests.request('GET', 'https://www.google.com/maps/place/%EC%B2%AD%EA%B3%84%EC%B2%9C/data=!4m7!3m6!1s0x357ca2ece3930023:0xbd86fa6e88b74ed4!8m2!3d37.5691015!4d126.9786692!9m1!1b1?hl=ko')
#   soup = BeautifulSoup(response.content, 'html.parser')

#   review_list = []



from multiprocessing.connection import Client
from pymongo import MongoClient
import pandas as pd

# print(MongoClient)

# HOST = 'cluster0.09izr.mongodb.net'
# USER = 'swon95'
# PASSWORD = 'a1231234'
URI = 'mongodb+srv://swon95:a1231234@cluster0.09izr.mongodb.net/?retryWrites=true&w=majority'

Client = MongoClient(URI)

DATABASE = 'project'

database = Client[DATABASE]

# Table = Collection
COLLECTION = 'Project'
collection = database[COLLECTION]

data = pd.read_csv('D:\CodeStates\Section3\project\smoking.csv')
# coll = MongoClient(URI)[DATABASE][COLLECTION]
# coll.remove()
collection.insert_many(data.to_dict('records'))
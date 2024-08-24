from urllib import request
import json
import pandas as pd
import numpy as np
from scipy import stats
from dotenv import load_dotenv
import os

#Option for all the column and row
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

load_dotenv()

#API KEY and URL
API_KEY = os.getenv('KEY')
URL = "https://api.balldontlie.io/v1/stats?per_page=100&dates[]=2024-01-01"
URL_AVG = "https://api.balldontlie.io/v1/season_averages?season=2023&player_ids[]=18&player_ids[]=387"
header = {"Authorization": API_KEY}

#Access the web and get the data
requests = request.Request(URL,headers=header)
response = request.urlopen(requests)
requests_2 = request.Request(URL_AVG,headers = header)
response_2 = request.urlopen(requests_2)

#Load up the data and dataframe it
data = json.load(response)
all_player_data = pd.DataFrame(data['data'])

data_2 = json.load(response_2)
average_data = pd.DataFrame(data_2['data'])
#Variable
data_all = {}
data_2_players = {}
data_average = {}
#Total_game_func
def total_game_stat():
    for key,value in all_player_data.iterrows():
        data_all = all_player_data[['fgm','fga','fta']].to_dict(orient="records")
    return data_all

#Checking the player id and name
# print(all_player_data['team'][0])

# print(json.dumps(data_2,indent=4))

#Player stats func, have to reformat it to make it easier to scrape the data to graph
def player_stats():
    for index,item in all_player_data.iterrows():
        player_ids= all_player_data['player'][index]['id']
        data_2_players[player_ids] = {
            'first_name':all_player_data['player'][index]['first_name'],
            'last_name':all_player_data['player'][index]['last_name'],
            'team_id': all_player_data['player'][index]['team_id'],
            'team_name':all_player_data['team'][index]['name'],
            'pts': item['pts'],
            'fgm':item['fgm'],
            'fga':item['fga'],
            'fta':item['fta']
        }
    return data_2_players

# print(json.dumps(player_stats(),indent=4))
#Average stats 

def avg_player_stats():
    for key,value in average_data.iterrows():
        data_average = average_data[['pts','fgm','fga','fta']].to_dict(orient="records")
    return data_average
#Grab the average point, fga, fgm, and fta 
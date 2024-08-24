<<<<<<< HEAD
from urllib import request
import json
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os


#Option for all the column and row
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

load_dotenv()

#API KEY and URL
API_KEY = os.getenv('KEY')
# URL_ALL_TEAM = "https://api.balldontlie.io/v1/teams"
URL_ALL_PLAYERS = "https://api.balldontlie.io/v1/players?per_page=100"
header = {"Authorization": API_KEY}

#Access the web and get the data
requests = request.Request(URL_ALL_PLAYERS,headers=header)
response = request.urlopen(requests)


#Load up the data and dataframe it
data = json.load(response)
df_data = pd.DataFrame(data['data'])

# print(data)
#Dictionary Variable
basketball_player_dict = {}

#Clean some of the nan column
df_data['draft_year'].fillna(df_data['draft_year'].median(),inplace=True)
df_data['draft_round'].fillna(df_data['draft_round'].median(),inplace = True)
df_data['draft_number'].fillna(df_data['draft_number'].mean(),inplace = True)
# print(df_data)

#Cherry pick the column that are needed and converting weight into numeric
for key,value in df_data.iterrows():
    basketball_player_dict = df_data[['id','first_name','last_name','position','weight','draft_year']].to_dict(orient='records')
    for indices in range(len(basketball_player_dict)):
        basketball_player_dict[indices]['weight'] = int(basketball_player_dict[indices]['weight'])


#Function
def mean_calc_weight():
    weight_list = [value['weight'] for value in basketball_player_dict]
    average_weight = np.mean(weight_list)
    return average_weight
        
   
def count_weight():
    mode_weight_list = [value['weight'] for value in basketball_player_dict]
    mode_weight = np.unique(mode_weight_list, return_counts=True)
    return mode_weight
    
def percentage_in_weight():
    weight_list = [value['weight'] for value in basketball_player_dict]
    total_weight = np.sum(weight_list)
    return weight_list,(weight_list/total_weight)*100
    

=======
from urllib import request
import json
import pandas as pd
import numpy as np



#Option for all the column and row
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#API KEY and URL
API_KEY = "75a1ba3b-699f-4b8d-a799-45e9c5fb5d13"
# URL_ALL_TEAM = "https://api.balldontlie.io/v1/teams"
URL_ALL_PLAYERS = "https://api.balldontlie.io/v1/players?per_page=100"
header = {"Authorization": API_KEY}

#Access the web and get the data
requests = request.Request(URL_ALL_PLAYERS,headers=header)
response = request.urlopen(requests)


#Load up the data and dataframe it
data = json.load(response)
df_data = pd.DataFrame(data['data'])

# print(data)
#Dictionary Variable
basketball_player_dict = {}

#Clean some of the nan column
df_data['draft_year'].fillna(df_data['draft_year'].median(),inplace=True)
df_data['draft_round'].fillna(df_data['draft_round'].median(),inplace = True)
df_data['draft_number'].fillna(df_data['draft_number'].mean(),inplace = True)
# print(df_data)

#Cherry pick the column that are needed and converting weight into numeric
for key,value in df_data.iterrows():
    basketball_player_dict = df_data[['id','first_name','last_name','position','weight','draft_year']].to_dict(orient='records')
    for indices in range(len(basketball_player_dict)):
        basketball_player_dict[indices]['weight'] = int(basketball_player_dict[indices]['weight'])


#Function
def mean_calc_weight():
    weight_list = [value['weight'] for value in basketball_player_dict]
    average_weight = np.mean(weight_list)
    return average_weight
        
   
def count_weight():
    mode_weight_list = [value['weight'] for value in basketball_player_dict]
    mode_weight = np.unique(mode_weight_list, return_counts=True)
    return mode_weight
    
def percentage_in_weight():
    weight_list = [value['weight'] for value in basketball_player_dict]
    total_weight = np.sum(weight_list)
    return weight_list,(weight_list/total_weight)*100
    

>>>>>>> 8892ca080d904b953ea60d966eb39c621b1f38f3

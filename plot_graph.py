import plotly.express as px
from basketball import count_weight, percentage_in_weight
from game_stats import total_game_stat,player_stats,avg_player_stats
import pandas as pd
import numpy as np
#plot 5 graph and render it to the picture and add a template and picture to static
#Getting weight data
unique_value,counts= count_weight()
#Turn into dataframe
value_df = pd.DataFrame(unique_value)
value_df.columns = ["Weight"]
counts_df = pd.DataFrame(counts)
counts_df.columns = ['Count']
#Bind 2 dataframe
group_data=pd.concat([value_df,counts_df],axis = 1,ignore_index=True)
#Rename the columns
group_data.columns = ['Weight', 'Counts']

#Percentage variable
weight,percentage_weight = percentage_in_weight()
df_percentage = pd.DataFrame(percentage_weight)
df_percentage.columns = ['Percentage']

df_weight = pd.DataFrame(weight)
df_weight.columns = ['Weight']
group_weight = pd.concat([df_weight,df_percentage],axis = 1 , ignore_index=True)
group_weight.columns = ['Weight','Percentage']

#Game stats variables
all_stats = total_game_stat()
fgm_value = [values['fgm'] for values in all_stats]
sum_fgm = np.sum(fgm_value)
fga_value = [values['fga'] for values in all_stats]
sum_fga = np.sum(fga_value)
fta_value = [values['fta'] for values in all_stats]
sum_fta = np.sum(fta_value)
#Create data template
data = {'Metric': ['sum_fgm', 'sum_fga', 'sum_fta'],
        'Value': [sum_fgm, sum_fga, sum_fta]}
df_all_stats = pd.DataFrame(data)
# print(df_all_stats)

#Getting player stats and get player_full_name
player_stats_data = player_stats()
player_first_name = pd.DataFrame([values['first_name'] for values in player_stats_data.values()])
player_last_name = pd.DataFrame([values['last_name'] for values in player_stats_data.values()])
player_full_name = pd.concat([player_first_name,player_last_name],axis = 1,ignore_index=True)
player_full_name.columns = ['first_name','last_name']
player_full_name['full_name'] = player_full_name['first_name'] + ' ' + player_full_name['last_name']

#Get all player points
player_points = pd.DataFrame([values['pts'] for values in player_stats_data.values()])
player_points.columns = ['pts']
full_player_stats= pd.concat([player_full_name,player_points],axis = 1, ignore_index=True)
full_player_stats.columns = ['First Name', 'Last Name', 'Full Name', 'Point']
full_player_stats_sorted = full_player_stats.sort_values(by='Point')
full_player_stats_no_zero = full_player_stats_sorted.loc[(full_player_stats_sorted['Point']!=0)]

#Get average player data
avg_data = pd.DataFrame(avg_player_stats())
players_id = pd.DataFrame(player_stats_data.keys())
players_id.columns = ['ID']
player_avg_name_and_ID = pd.concat([players_id,full_player_stats['Full Name']],axis = 1,ignore_index=True)
player_avg_name_and_ID.columns = ['ID','Full_Name']
avg_player_data = pd.concat([player_avg_name_and_ID,avg_data],axis = 1)
two_player_avg_data = avg_player_data.loc[(avg_player_data['ID']==18)|(avg_player_data['ID']==387)]


def player_weight_hist():
    fig = px.histogram(group_data,x="Weight",y = "Counts", title = "All players weight count")
    fig.write_image("static/graph_images/weight_hist.jpg")

def percentage_player_weight_hist():
    fig = px.histogram(group_weight,x="Weight",y="Percentage", title = "All players weight percentage")
    fig.write_image("static/graph_images/percentage_weight_hist.jpg")


def all_stats_bar():
    fig = px.bar(df_all_stats,x = "Metric",y = "Value", title = "All players stats")
    fig.write_image("static/graph_images/all_stats.jpg")
    
def player_stats_bar():
    fig  = px.bar(full_player_stats_no_zero,x='Full Name',y='Point',title = "Players Points")
    fig.write_image("static/graph_images/player_stats_point.jpg")

def player_stats_avg():
    fig = px.bar(two_player_avg_data,x="Full_Name",y = ["pts","fgm","fga","fta"], title = "Stats between 2 players")
    fig.write_image("static/graph_images/avg_player_stats.jpg")


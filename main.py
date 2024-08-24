<<<<<<< HEAD
from flask import Flask,render_template,request
from plot_graph import player_weight_hist,percentage_player_weight_hist,player_stats_bar,all_stats_bar,player_stats_avg

app = Flask(__name__)
@app.route('/')
def index():
    player_weight_hist()
    percentage_player_weight_hist()
    player_stats_bar()
    all_stats_bar()
    player_stats_avg()
    return render_template("index.html")

if __name__ == '__main__':
=======
from flask import Flask,render_template,request
from plot_graph import player_weight_hist,percentage_player_weight_hist,player_stats_bar,all_stats_bar,player_stats_avg

app = Flask(__name__)
@app.route('/')
def index():
    player_weight_hist()
    percentage_player_weight_hist()
    player_stats_bar()
    all_stats_bar()
    player_stats_avg()
    return render_template("index.html")

if __name__ == '__main__':
>>>>>>> 8325578 (Add .gitignore and environment file)
  app.run(host='0.0.0.0', port=5000)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            player_name = request.form["player_name"]
            games_played = int(request.form["games_played"])
            total_score = int(request.form["total_score"])
            
            if games_played > 0:
                average_score = total_score / games_played
            else:
                average_score = 0.0
                
            return render_template("index.html", 
                                   player_name=player_name, 
                                   games_played=games_played, 
                                   total_score=total_score, 
                                   average_score=average_score,
                                   submitted=True)
        except ValueError:
            return render_template("index.html", error="Please enter valid integers for games played and score.")
            
    return render_template("index.html", submitted=False)

if __name__ == "__main__":
    app.run(debug=True)

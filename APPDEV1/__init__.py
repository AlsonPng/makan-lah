from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')



@app.route('/game')
def game_form():

    return render_template('game.html')

@app.route('/redeemRewards')
def redeem_rewards():

    return render_template('redeemRewards.html')

if __name__ == '__main__':
    app.run(debug=True)


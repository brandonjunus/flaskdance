from flask import Flask, redirect, url_for
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
from flask_dance.contrib.spotify import make_spotify_blueprint, spotify

app = Flask(__name__)
app.config['SECRET_KEY'] = "BLAHBLAHBLAH"

twitter_blueprint = make_twitter_blueprint(api_key="AJTFIekcY9wq9n51aS7pLMXpa", api_secret="Rx09f6RCLeS0nJH1McQsMQ6JIHIOWK54HL3KSRZojwisIUov83")
app.register_blueprint(twitter_blueprint, url_prefix='/twitter_login')

spotify_blueprint = make_spotify_blueprint(client_id='4189e9b9724c413690ee4b8294f8099b', client_secret='d64f91ad3f704490801f67a5ac1890cd')
app.register_blueprint(spotify_blueprint, url_prefix= '/spotify_login')

@app.route('/twitter')
def twitter_login():
    if not twitter.authorized:
        return redirect(url_for('twitter.login'))
    account_info = twitter.get('account/settings.json')
    if account_info.ok:
        account_info_json = account_info.json()
        return "<h1>Your twitter name is @{}</h1>".format(account_info_json['screen_name'])
    return '<h1>Request Failed!</h1'

@app.route('/spotify')
def spotify_login():
    if not spotify.authorized:
        return redirect(url_for('spotify.login'))
    account_info = spotify.get('/v1/me.json')
    if account_info.ok:
        account_info_json = account_info.json()
        return account_info_json
    return '<h1>Request Failed!</h1'

if __name__ == "__main__":
    app.run(debug=True)
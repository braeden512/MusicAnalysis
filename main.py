import spotify_api
from flask import Flask, Blueprint, request, render_template
import socket



app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
@app.route("/home", methods=['GET','POST'])
def home():
    if request.method == 'GET':

        return render_template("index.html")
    
    if request.method == 'POST':
        artist_submission = request.form['artist_name']

        token = spotify_api.get_token()
        result = spotify_api.search_for_artist(token, artist_submission)
        artist_id = result["id"]
        songs = spotify_api.get_songs_by_artist(token, artist_id)

        return render_template("data.html", songs=songs, result=result, artist_submission=artist_submission)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

# print ('{0}s top 10 songs: '.format(result["name"]))
# print ("---------------------------------------")
# for idx, song in enumerate(songs):
#     print (f"{idx + 1}. {song['name']}")
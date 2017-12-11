"""web

provides APIs

"""
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from hiddenyoutu_server import youtube

app = Flask(__name__)
CORS(app)


@app.route('/list/<q>')
def search(q):
    api_key = request.args.get('key', None)
    page_token = request.args.get('pageToken', None)
    videos = youtube.search(
        q,
        page_token=page_token,
        api_key=api_key
    )
    return jsonify(videos)


@app.route('/list/related_videos/<video_id>')
def search_related_video(video_id):
    api_key = request.args.get('key', None)
    page_token = request.args.get('pageToken', None)
    related_videos = youtube.search_related_videos(
        video_id,
        page_token=page_token,
        api_key=api_key)
    return jsonify(related_videos)

"""web

provides APIs

"""
from flask import Flask
from flask import request
from flask import jsonify
from hiddenyoutu_server import youtube

app = Flask(__name__)


@app.route('/related_videos/<video_id>')
def search_related_video(video_id):
    next_page_token = request.args.get('next_page_token', None)
    related_videos = youtube.search_related_videos(video_id, next_page_token=next_page_token)
    return jsonify(related_videos)

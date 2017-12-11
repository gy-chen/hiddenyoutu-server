"""youtube

provide functions that relates to Youtube

  - Search related videos

"""
import os
import requests
from hiddenyoutu_server import setting

__ALL__ = [
    'search_related_videos',
    'search']

# see https://developers.google.com/youtube/v3/docs/search/list
LIST_URL = 'https://www.googleapis.com/youtube/v3/search?'
LIST_QS_KEY_Q = 'q'
LIST_QS_KEY_TYPE = 'type'
LIST_QS_KEY_RELATED_VIDEO_ID = 'relatedToVideoId'
LIST_QS_KEY_PART = 'part'
LIST_QS_KEY_API_KEY = 'key'
LIST_QS_KEY_PAGE_TOKEN = 'pageToken'


# TODO add doc string
def search_related_videos(video_id, page_token=None, api_key=None):
    api_key = api_key if api_key else init_api_key()
    if api_key is None:
        raise ValueError("Please provide API key. See: https://console.developers.google.com/")
    params = {
        LIST_QS_KEY_TYPE: 'video',
        LIST_QS_KEY_RELATED_VIDEO_ID: video_id,
        LIST_QS_KEY_PART: 'snippet',
        LIST_QS_KEY_API_KEY: api_key,
        LIST_QS_KEY_PAGE_TOKEN: page_token
    }
    r = requests.get(LIST_URL, params=params)
    # TODO check response status
    return r.json()


def search(q, page_token=None, api_key=None):
    api_key = api_key if api_key else init_api_key()
    if api_key is None:
        raise ValueError("Please provide API key. See: https://console.developers.google.com/")
    params = {
        LIST_QS_KEY_Q: q,
        LIST_QS_KEY_TYPE: 'video',
        LIST_QS_KEY_PART: 'snippet',
        LIST_QS_KEY_API_KEY: api_key,
        LIST_QS_KEY_PAGE_TOKEN: page_token
    }
    r = requests.get(LIST_URL, params=params)
    # TODO check response status
    return r.json()


def init_api_key():
    return os.environ.get('YOUTUBE_API_KEY', setting.YOUTUBE_API_KEY)

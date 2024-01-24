import requests
from urllib.parse import quote, urljoin

from core.settings import FRAMEX_BASE_URL, FRAMEX_REQUEST_TIMEOUT, FRAMEX_VIDEO_NAME
from models.video import Video

# Exceptions


class MissingVideoException(Exception):
    pass


class VideoFrameException(Exception):
    pass


# FrameX Helper

class FrameXHelper:
    def __init__(self, url: str = FRAMEX_BASE_URL):
        self.base_url = url
        self.session = requests.Session()

    def get_video(self, video_name: str = FRAMEX_VIDEO_NAME):
        """
        Get the video from FrameX.
        :param video_name: The video name.
        :return: The video.
        """
        url = urljoin(self.base_url, f"video/{quote(video_name)}")
        response = self.session.get(url, timeout=FRAMEX_REQUEST_TIMEOUT)
        if not response.ok:
            raise MissingVideoException(f"Video {video_name} not found.")

        return Video(**response.json())

    def get_video_frame(self, video_name: str, frame: int):
        """
        Get the video frame from FrameX.
        :param video_name: The video name.
        :param frame: The frame number.
        :return: The video frame.
        """
        url = urljoin(self.base_url, f"video/{quote(video_name)}/frame/{frame}")
        response = self.session.get(url, timeout=FRAMEX_REQUEST_TIMEOUT)
        if not response.ok:
            raise VideoFrameException(f"Video {video_name} not found.")

        return response.content

from dataclasses import dataclass
from typing import List


@dataclass
class Video:
    """
    Xframe Video model
    """

    name: str
    width: int
    height: int
    frames: int
    frame_rate: List[int]
    url: str
    first_frame: str
    last_frame: str

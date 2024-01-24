class Bisect:
    def __init__(self, video_frames):
        self.limit_left = 0
        self.limit_right = video_frames - 1
        self.mid_point = int((self.limit_left + self.limit_right) / 2)
        self.current_step = 0

    def process_step(self, event_happened: bool):
        if event_happened:
            self.limit_right = self.mid_point
        else:
            self.limit_left = self.mid_point

        self.mid_point = int((self.limit_left + self.limit_right) / 2)
        self.current_step += 1

    def is_finished(self):
        return not (self.limit_left + 1 < self.limit_right)

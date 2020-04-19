import config
from Meeting import Meeting
from zoomus import ZoomClient


class Tournament(object):
    def __init__(self):
        self.client = ZoomClient(config.KEY, config.SECRET)
        self.meetings = {}

    def create_rooms(self):
        for room in range(1, config.NUMBER_OF_ROOMS+1):
            self.meetings[room] = (Meeting(room, self.client))

    def delete_rooms(self, *args):
        """
        Delete meetings by room numbers
        :param args: List of room numbers
        """
        for arg in args:
            self.meetings[arg].delete_meeting()
            self.meetings.pop(arg)

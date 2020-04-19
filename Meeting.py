class Meeting(object):
    def __init__(self, room_number, zoom_client):
        self.room_number = room_number
        self.client = zoom_client
        self.meeting_id = None
        self.info = None

    def create_meeting(self):
        info = self.client.meeting.create(user_id="me",
                                          topic="Meeting {}".format(self.room_number)
                                          ).json()
        self.info = info
        self.meeting_id = info['id']

    def get_meeting_info(self):
        print(self.info)

    def delete_meeting(self):
        self.client.meeting.delete(meeting_id=self.meeting_id)

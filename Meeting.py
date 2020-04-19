class Meeting(object):
    def __init__(self, room_number, zoom_client):
        self.room_number = room_number
        self.client = zoom_client
        self.info = self.create_meeting()
        self.join_url = self.info['join_url']
        self.meeting_id = self.info['id']

    def create_meeting(self):
        info = self.client.meeting.create(user_id="me",
                                          topic="Meeting {}".format(self.room_number)
                                          ).json()
        return info

    def get_meeting_info(self):
        print(self.info)

    def get_meeting_url(self):
        print(self.join_url)

    def delete_meeting(self):
        self.client.meeting.delete(id=self.meeting_id)

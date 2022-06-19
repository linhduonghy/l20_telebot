
class TeleUser:
    
    def __init__(self, user_id = None, chat_id = None, first_name = None, last_name = None, username = None):
        self.user_id = user_id
        self.chat_id = chat_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
    
    def __str__(self):
        return ("TeleUser: chat_id: {0}, username: {1}".format(self.chat_id, self.username))
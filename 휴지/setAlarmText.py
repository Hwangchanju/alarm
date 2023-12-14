class UserData:
    def __init__(self):
        self.user_data = {}

    def set_user_data(self, user_id, data):
        self.user_data[user_id] = data

    def get_user_data(self, user_id):
        return self.user_data.get(user_id)

user_data_manager = UserData()
class User:
    
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0


user_1 = User("001", "angela")
user_2 = User("002", "jack")

print(user_1.followers)
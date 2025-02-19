from Models.User import User

class UserService:
    def __init__(self):
        self.users = {}
        
    def add_user(self, name, id, email):
        user = User(name, id, email)
        self.users[id] = user
        return user

    def get_user(self, id):
        return self.users.get(id)
    
    